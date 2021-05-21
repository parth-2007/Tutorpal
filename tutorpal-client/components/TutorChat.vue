
<template>
  <client-only>
    <html
      data-wf-page="5f600218af481481a99ffa6a"
      data-wf-site="5f600218af4814e3759ffa69"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <body style="height: 100vh" class="body">
        <router-link
          to="/inbox"
          aria-current="page"
          style="font-family: Poppins; margin-left: 5%; padding-top: 20px"
          class="link-block w-inline-block w--current"
          >Go back to contacts</router-link
        >
        <div style="border-radius: 8px" class="div-block-80">
          <div class="div-block-71">
            <img
              src="../static/student/images/user-2.png"
              loading="lazy"
              width="130"
              height="130"
              srcset="
                ../static/student/images/user-2.png 500w,
                ../static/student/images/user-2.png 512w
              "
              sizes="74px"
              alt=""
            />
            <div class="div-block-72">
              <h1 class="heading-3" id="fullname" style="font-size: 30px">
                Johnny Lawrence
              </h1>
            </div>
          </div>
        </div>
        <!-- display chat messages -->
        <div class="wrapper" id="chat-items">
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
                      chatMsg ? chatMsg.timestamp : ''
                    }}</em>
                  </div>
                </div>
              </div>
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
import loggedInFetch from '../utils/loggedInFetch'

export default {
  data() {
    return {
      socket: null,
      message: '',
      chatMsgs: [],
      errors: '',
    }
  },
  head() {
    return {
      title: 'Chat with John',
      link: [
        {
          rel: 'stylesheet',
          type: 'text/css',
          href:
            'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/webflow.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/student-main.webflow.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/normalize.css',
        },
      ],
    }
  },
  computed: {
    ...mapGetters({ user: 'getUser' }),
  },
  async created() {
    // const chatMsgs = this.chatMsgs
    const response = await loggedInFetch(
      'api/rooms/' + this.$route.params.id + '/messages/'
    )
    if (response.error) {
      if (
        response.error === 'client error' ||
        (response.error === 'server error' && response.status !== 404)
      ) {
        this.errors = 'Something went wrong :('
      }
      if (response.error === 'server error' && response.status === 404) {
        this.errors = 'Not your chat room'
      }
    } else {
      // const loc = window.location
      // const wsStart = 'ws://'
      // if (this.$route == 'https:') {
      //     wsStart = 'wss://'
      // }
      // const host = loc.host
      const pastMessages = response.results
      console.log(pastMessages)
      this.chatMsgs = pastMessages
      this.connect()
    }
  },
  methods: {
    // RUN DOCKER AND REDIS !!!!!!
    connect() {
      const chatMsgs = this.chatMsgs
      const endpoint =
        'ws://localhost:5000/api/ws/chat/' + this.$route.params.id + '/'

      this.socket = new WebSocket(endpoint)
      // const chatMsgs = this.chatMsgs

      this.socket.onmessage = function (e) {
        console.log('message', e)
        const chatDataMsg = JSON.parse(e.data)
        if (!chatDataMsg.error) {
          console.log('chatmsgs: ', chatMsgs)
          chatMsgs.push(chatDataMsg)
        } else {
          console.warn(chatDataMsg)
        }
      }
      this.socket.onopen = (e) => {
        console.log('open', e)
      }
      this.socket.onerror = (e) => {
        console.log('error', e)
      }
      this.socket.onclose = (e) => {
        console.log('close', e)
        // setTimeout(() => {
        //   this.connect()
        // }, 1000)
      }
    },
    // escapeOutput(toOutput) {
    //   return toOutput
    //     .replace(/&/g, '&amp;')
    //     .replace(/</g, '&lt;')
    //     .replace(/>/g, '&gt;')
    //     .replace(/"/g, '&quot;')
    //     .replace(/'/g, '&#x27')
    //     .replace(/\//g, '&#x2F')
    // },
    handleFormSubmit() {
      // const jsonData = JSON.stringify({ message: this.message })
      console.log(this.message)
      this.socket.send(this.message)
      this.message = ''
    },
  },
}
</script>
<style scoped>
.wrapper {
  overflow-y: auto;
  margin-top: 20px;
  margin-right: 10%;
  margin-left: 10%;
  padding-top: 20px;
  padding-bottom: 20px;
  background-color: #fff;
  padding-left: 20%;
  padding-right: 20%;
  border-radius: 8px;
  height: 58%;
}
</style>