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
  },
  methods: {
    ...mapGetters(['getUser']),
    ...mapActions(['fetchUser']),
  },
}
</script>
