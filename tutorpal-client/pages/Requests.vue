<template>
  <div v-if="!user.unfetched" id="main">
    <div v-if="user.isStudent">
      <StudentRequests></StudentRequests>
    </div>
    <div v-else-if="user.isTutor">
      <NotFound></NotFound>
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

export default {
  head() {
    return {
      title: 'Requests'
    }
  },
  computed: mapGetters({ user: 'getUser' }),
  async created() {
    await this.fetchUser()
  },
  methods: {
    ...mapActions(['fetchUser']),
  },
}
</script>
