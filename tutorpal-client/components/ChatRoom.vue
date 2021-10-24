
<template>
  <client-only>
    <html
      data-wf-page="5f600218af481481a99ffa6a"
      data-wf-site="5f600218af4814e3759ffa69"
    >
      <head>
        <meta charset="utf-8" />
        <link
          rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          media="print"
          onload="this.media='all'"
        />
      </head>
      <body style="min-height: 100vh" class="body">
        <router-link
          to="/inbox"
          aria-current="page"
          style="font-family: Poppins; margin-left: 5%; padding-top: 20px"
          class="link-block w-inline-block w--current"
          >Go back to contacts</router-link
        >
        <div style="border-radius: 8px" class="div-block-80">
          <div style="" class="div-block-71">
            <img
              style="margin-left: auto; border-radius: 100px"
              :src="
                otherUser
                  ? otherUser.profilePic
                  : '../static/student/images/user-2.png'
              "
              loading="lazy"
              width="130"
              height="130"
              sizes="74px"
              alt="Student profile picture"
            />
            <div style="margin-right: auto" class="div-block-72">
              <h1 class="heading-3" id="fullname" style="font-size: 30px">
                {{ otherUser ? otherUser.firstName : '' }}
                {{ otherUser ? otherUser.lastName : '' }}
              </h1>
            </div>
          </div>
        </div>
        <div class="chatroomcontainer" style="width: 100%">
          <div
            ref="chatcont"
            @scroll="getNextMessages()"
            style="
              height: 55vh;
              overflow-y: auto;
              display: flex;
              flex-direction: column-reverse;
            "
            class="wrapper"
          >
            <div>
              <p style="margin-bottom: 15px" class="paragraph-2-copy">
                This is the beginning of your chat message history with
                {{ otherUser ? otherUser.firstName : '' }}
              </p>
              <!-- eslint-disable-next-line -->
              <div v-for="chatMsg in chatMsgs">
                <div :key="chatMsg ? chatMsg.id : null">
                  <div
                    :class="
                      (chatMsg ? chatMsg.author : null) == user.id
                        ? 'chat_item_here'
                        : 'chat_item_away'
                    "
                  >
                    <div
                      :class="
                        (chatMsg ? chatMsg.author : null) == user.id
                          ? 'div-block-61-copy'
                          : 'div-block-61'
                      "
                    >
                      <p class="paragraph-6">
                        {{ chatMsg ? chatMsg.message : '' }}
                      </p>
                      <div class="text-block-40">
                        <em class="italic-text">{{
                          convertTime2(chatMsg.timestamp)
                        }}</em>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div ref="container" />
            </div>
          </div>
        </div>
        <input
          v-model="message"
          style="
            width: 80%;
            margin-right: 10%;
            margin-left: 10%;
            font-family: Poppins;
            margin-bottom: 15px;
            margin-top: 20px;
          "
          class="form-control"
          placeholder="Send a message"
          @keyup.enter="handleFormSubmit()"
        />
      </body>
    </html>
  </client-only>
</template>
<script>
import { mapGetters } from 'vuex'
import convertTime2 from '../utils/convertTime2'

export default {
  props: {
    otherUser: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      socket: null,
      message: '',
      chatMsgs: [],
      errors: '',
      response: [],
    }
  },
  head() {
    return {
      title: `Chat with ${this.otherUser.firstName}`,
      link: [
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/webflow.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/normalize.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/student-main.webflow.css',
        },
      ],
    }
  },
  computed: {
    ...mapGetters({ user: 'getUser' }),
  },

  async created() {
    this.response = await fetch(
      process.env.API_URL + '/rooms/' + this.$route.params.id + '/messages/',
      {
        credentials: 'include',
      }
    )
      .then((res) => {
        if (res.status === 403 || res.status === 404) {
          return { unauthenticated: true }
        } else if (res.status >= 400 && res.status < 600) {
          return { error: 'server error', status: res.status }
        }
        return res.json()
      })
      .catch(() => {
        return { error: 'client error' }
      })
    if (this.response.error) {
      if (
        this.response.error === 'client error' ||
        (this.response.error === 'server error' && this.response.status !== 404)
      ) {
        this.errors = 'Something went wrong :('
      }
      if (
        this.response.error === 'server error' &&
        this.response.status === 404
      ) {
        this.errors = 'You are not in this chat room'
      }
    } else {
      const pastMessages = this.response.results
      this.chatMsgs = pastMessages.reverse()
    }
    this.connect()
  },
  beforeDestroy() {
    this.socket.close()
  },
  methods: {
    convertTime2,
    // RUN DOCKER AND REDIS !!!!!!
    async getNextMessages() {
      const container = this.$refs.chatcont
      const pos = container.scrollTop
      const maxScrollPosition = container.scrollHeight - container.clientHeight
      if (Math.ceil(Math.abs(pos)) === maxScrollPosition) {
        if (this.response.next !== null) {
          const data = await fetch(this.response.next, {
            credentials: 'include',
          }).then((res) => res.json())
          this.response = data
          const chatMsgs = this.chatMsgs
          data.results.forEach(function (x) {
            chatMsgs.unshift(x)
          })
        }
      }
    },
    connect() {
      const chatMsgs = this.chatMsgs
      const endpoint =
        'wss://chat.tutorpal.org/ws/chat/' + this.$route.params.id + '/'
      this.socket = new WebSocket(endpoint)
      this.socket.onmessage = function (e) {
        const chatDataMsg = JSON.parse(e.data)
        if (!chatDataMsg.error) {
          chatMsgs.push(chatDataMsg)
        }
      }
      this.socket.onclose = () => {
        if (this.$route.path.includes('chat')) {
          alert('This chat session has ended. Please refresh to continue')
        }
      }
    },
    handleFormSubmit() {
      this.socket.send(this.message)
      this.message = ''
      const el = this.$refs.container
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'end' })
      }
    },
    addChatMsg(msg) {
      this.chatMsgs.push(msg)
    },
  },
}
</script>
<style scoped>
.wrapper {
  margin-top: 20px;
  margin-right: 10%;
  margin-left: 10%;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 25px;
  padding-right: 25px;
  background-color: #fff;
  border-radius: 8px;
}
</style>