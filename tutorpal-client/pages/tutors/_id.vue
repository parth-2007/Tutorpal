<template>
  <div id="main">
    <div v-if="user.unauthenticated">
      <MainTutorProfile></MainTutorProfile>
    </div>
    <div v-else-if="user.isStudent">
      <StudentTutorProfile></StudentTutorProfile>
    </div>
    <div v-else-if="user.isTutor">
      <MainTutorProfile></MainTutorProfile>
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