<template>
  <div id="main">
    <div v-if="user.unauthenticated">
      <NotFound></NotFound>
    </div>
    <div v-else-if="user.is_student">
      <StudentAccount></StudentAccount>
    </div>
    <div v-else-if="user.is_tutor">
      <TutorAccount></TutorAccount>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import NotFound from '../components/NotFound'
import StudentAccount from '../components/StudentChangeInfo'
import TutorAccount from '../components/TutorChangeInfo'

export default {
  components: {
    NotFound,
    StudentAccount,
    TutorAccount,
  },
  head() {
    return {
    }
  },
  computed: mapGetters({ user: 'getUser' }),
  async created() {
    await this.fetchUser()
    const user = this.getUser()
    if (user.unauthenticated) {
      require('../components/outcast/css/webflow.css')
      require('../components/outcast/css/last-project-afcf8d.webflow.css')
      require('../components/outcast/css/normalize.css')
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
