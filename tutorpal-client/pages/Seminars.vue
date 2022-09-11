<template>
  <div v-if="!user.unfetched" id="main">
      <div v-if="user.isStudent">
    </div>
    <div v-else-if="user.isTutor">
      <TutorSeminar></TutorSeminar>
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
      title: 'Seminars',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
        { rel:"stylesheet", type:"text/css", href: "/student/css/student-main.webflow.css" },
      ]
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
