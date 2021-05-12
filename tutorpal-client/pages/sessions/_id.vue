<template>
    <div v-if="user.unauthenticated">
      <HomeTutorProfile></HomeTutorProfile>
    </div>
    <div v-else-if="user.isStudent">
      <StudentTutorProfile></StudentTutorProfile>
    </div>
    <div v-else-if="user.isTutor">
      <HomeTutorProfile></HomeTutorProfile>
    </div>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  head() {
    return {}
  },
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