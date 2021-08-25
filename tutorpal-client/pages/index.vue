<template>
  <div v-if="!user.unfetched" id="main">
    <div v-if="user.isStudent">
      <StudentHome></StudentHome>
    </div>
    <div v-else-if="user.isTutor">
      <TutorHome></TutorHome>
    </div>
    <div v-else>
      <MainHome></MainHome>
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
