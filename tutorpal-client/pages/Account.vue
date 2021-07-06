<template>
  <div id="main">
    <div v-if="user.unauthenticated">
      <NotFound></NotFound>
    </div>
    <div v-else-if="user.isStudent">
      <StudentAccount></StudentAccount>
    </div>
    <div v-else-if="user.isTutor">
      <TutorAccount></TutorAccount>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  computed: mapGetters({ user: 'getUser' }),
  async created() {
    await this.fetchUser()
  },
  methods: {
    ...mapGetters(['getUser']),
    ...mapActions(['fetchUser']),
  },
}
</script>
