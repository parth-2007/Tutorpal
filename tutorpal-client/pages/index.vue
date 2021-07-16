<template>
  <div id="main">
    <div v-if="user.unauthenticated">
      <MainHome></MainHome>
    </div>
    <div v-else-if="user.isStudent">
      <StudentHome></StudentHome>
    </div>
    <div v-else-if="user.isTutor">
      <TutorHome></TutorHome>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  head() {
    return {
      title: 'Home - TutorPal',
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
