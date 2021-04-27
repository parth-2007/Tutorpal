<template>
  <div id="main">
    <div v-if="user.unauthenticated">
      <HomeMain></HomeMain>
    </div>
    <div v-else-if="user.is_student">
      <HomeStudent></HomeStudent>
    </div>
    <div v-else-if="user.is_tutor">
      <HomeTutor></HomeTutor>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import HomeMain from '../components/HomeMain'
import HomeStudent from '../components/HomeStudent'
import HomeTutor from '../components/HomeTutor'

export default {
  components: {
    HomeMain,
    HomeStudent,
    HomeTutor,
  },
  head() {
    return {
      title: 'Home - TutorPal',
    }
  },
  computed: mapGetters({ user: 'getUser' }),
  async created() {
    await this.fetchUser()
    const user = this.getUser()
    if (user.unauthenticated) {
      require('../components/main/css/webflow.css')
      require('../components/main/css/homepage-12.webflow.css')
      require('../components/main/css/normalize.css')
    } else if (user.is_student) {
      require('../components/student/css/webflow.css')
      require('../components/student/css/student-main.webflow.css')
      require('../components/student/css/normalize.css')
    } else if (user.is_tutor) {
      require('../components/tutor/css/webflow.css')
      require('../components/tutor/css/tutor-main.webflow.css')
      require('../components/tutor/css/normalize.css')
    }
  },
  methods: {
    ...mapGetters(['getUser']),
    ...mapActions(['fetchUser']),
  },
}
</script>
