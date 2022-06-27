<template>
  <div v-if="!user.unfetched" id="main">
      <div v-if="user.isStudent">
      <TutorSeminar></TutorSeminar>
    </div>
    <div v-else-if="user.isTutor">
      <TutorSeminar></TutorSeminar>
    </div>
    <div v-else>
      <body>
        <router-link to="/" class="outcastlink-block-4 w-inline-block"
          ><img src="../static/student/images/logo.jpg" loading="lazy" width="200" alt=""
        /></router-link>
        <div class="outcastcolumns-6 w-row">
          <div class="outcastcolumn-6 w-col w-col-6">
            <div class="outcastdiv-block-41">
              <h1 style="font-size: 140px" class="outcastheading-3">Oops!</h1>
              <p class="outcastparagraph-8">
                It seems you are attempting to join one of our seminars without a pre-existing student account to join with. Please <router-link to="/login">login</router-link> or <router-link to="/register-student"> register</router-link> a new student account in order to join this seminar.
              </p>
            </div>
          </div>
          <div class="w-col w-col-6">
            <img src="../static/outcast/images/404-image.png" width="600" />
          </div>
        </div>
      </body>
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
