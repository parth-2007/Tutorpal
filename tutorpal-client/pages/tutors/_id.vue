<template>
  <div id="main">
    <div v-if="user.unauthenticated">
      <HomeTutorProfile></HomeTutorProfile>
    </div>
    <div v-else-if="user.isStudent">
      <StudentTutorProfile></StudentTutorProfile>
    </div>
    <div v-else-if="user.isTutor">
      <HomeTutorProfile></HomeTutorProfile>
    </div>
  </div>
</template>
<script>
import HomeTutorProfile from '@/components/HomeTutorProfile'
import StudentTutorProfile from '@/components/StudentTutorProfile'
import { mapGetters, mapActions } from 'vuex'

export default {
   components: {
    HomeTutorProfile,
    StudentTutorProfile,
  },
  head() {
    return {
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