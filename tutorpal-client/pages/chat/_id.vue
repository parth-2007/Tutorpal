<template>
  <div v-if="user.isTutor || user.isStudent">
    <ChatRoom :other-user="otherUser"></ChatRoom>
  </div>
  <div v-else>
    <Forbidden></Forbidden>
   </div>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'
import loggedInFetch from '../../utils/loggedInFetch'
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
    await this.fetchUser()
    const response = await loggedInFetch(
      'api/rooms/' + this.$route.params.id + '/'
    )
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
      // console.log('in the _id.vue: ', this.otherUser)
    } else if (this.getUser().isStudent) {
      const tutor = keysToCamel(response.tutor)
      this.otherUser = tutor.user
    }
  },
  methods: {
    ...mapGetters(['getUser']),
    ...mapActions(['fetchUser']),
  },
}
</script>
