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
import MainHome from '../components/MainHome'
import StudentHome from '../components/StudentHome'
import TutorHome from '../components/TutorHome'

export default {
  components: {
    MainHome,
    StudentHome,
    TutorHome,
  },
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
