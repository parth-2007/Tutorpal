
<template>
  <client-only>
    <html>
      <body>
        <input v-model="message" @keyup.enter="handleFormSubmit()" />
      </body>
    </html>
  </client-only>
</template>
<script>
import { mapGetters } from 'vuex'

export default {
  data() {
    return {
      socket: null,
      message: '',
      chatMsgs: [],
    }
  },
  head() {
    return {
      title: 'Test Chat',
    }
  },
  computed: {
    ...mapGetters({ user: 'getUser' }),
  },
  created() {
    // const chatMsgs = this.chatMsgs
    const endpoint =
      'ws://localhost:5000/api/ws/chat/' + this.$route.params.id + '/'
    this.socket = new WebSocket(endpoint)

    this.socket.onmessage = function (e) {
      console.log('message', e)
      const chatDataMsg = JSON.parse(e.data)
      if (!chatDataMsg.error) {
        // const cleanMsg = escapeOutput(chatDataMsg.message)
        // const cleanName = escapeOutput(chatDataMsg.full_name)
        this.chatMsgs = [chatDataMsg, ...this.chatMsgs]
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
    }
  },
  methods: {
    connect() {
      const endpoint =
        'ws://localhost:8000/api/ws/chat/' + this.$route.params.id + '/'
      this.socket = new WebSocket(endpoint)

      this.socket.onmessage = function (e) {
        console.log('message', e)
        const chatDataMsg = JSON.parse(e.data)
        if (!chatDataMsg.error) {
          this.chatMsgs = [chatDataMsg, ...this.chatMsgs]
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
    handleFormSubmit() {
      console.log(this.message)
      this.socket.send(this.message)
      this.message = ''
    },
  },
}
</script>