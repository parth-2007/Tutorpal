<template>
  <div v-if="!user.unfetched" id="main">
    <div v-if="user.isTutor || user.isStudent">
      <ChatRoom :other-user="otherUser"></ChatRoom>
    </div>
    <div v-else>
      <Forbidden></Forbidden>
    </div>
  </div>
  <div v-else>
    <Loader></Loader>
  </div>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'
// import loggedInFetch from '../../utils/loggedInFetch'
import { keysToCamel } from '../../utils/changeObjectNaming'

export default {
  data() {
    return { otherUser: {} }
  },
  head() {
    return {}
  },
  computed: mapGetters({ user: 'getUser' }),
  async created() {
    // console.log('hi')
    await this.fetchUser()
    const response = await fetch('/api/rooms/' + this.$route.params.id + '/', {
      credentials: 'include',
    })
      .then((res) => {
        if (res.status === 403 || res.status === 404) {
          return { unauthenticated: true }
        } else if (res.status >= 400 && res.status < 600) {
          return { error: 'server error', status: res.status }
        }
        return res.json()
      })
      .catch((e) => {
        // console.warn(e)
        return { error: 'client error' }
      })
    if (response.error) {
      if (
        response.error === 'client error' ||
        (response.error === 'server error' && response.status !== 404)
      ) {
        this.errors = 'Something went wrong :('
      }
      if (
        response.error === 'server error' &&
        (response.status === 404 || response.status === 403)
      ) {
        this.errors = 'Not your chat room'
      }
    }
    if (this.getUser().isTutor) {
      const student = keysToCamel(response.student)
      this.otherUser = student.user
      // console.log('otherUser', this.otherUser)
      // console.log('in the _id.vue: ', this.otherUser)
    } else if (this.getUser().isStudent) {
      const tutor = keysToCamel(response.tutor)
      this.otherUser = tutor.user
      // console.log('otherUser', this.otherUser)
    }
  },
  methods: {
    ...mapGetters(['getUser']),
    ...mapActions(['fetchUser']),
  },
}
</script>
