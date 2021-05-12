<template>
  <div id="main">
    <div v-if="user.unauthenticated">
      <NotFound></NotFound>
    </div>
    <div v-else-if="user.isStudent">
      <StudentPayments></StudentPayments>
    </div>
    <div v-else-if="user.isTutor">
      <TutorPayments></TutorPayments>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import NotFound from '../components/NotFound'
import StudentPayments from '../components/StudentPayments'
import TutorPayments from '../components/TutorPayments'

export default {
  components: {
    NotFound,
    TutorPayments,
    StudentPayments,
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
