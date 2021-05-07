<template>
  <div id="main">
    <div v-if="user.unauthenticated">
      <NotFound></NotFound>
    </div>
    <div v-else-if="user.is_student">
      <StudentRequests></StudentRequests>
    </div>
    <div v-else-if="user.is_tutor">
      <NotFound></NotFound>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import StudentRequests from '../components/StudentRequests'
import NotFound from '../components/NotFound'

export default {
  components: {
    StudentRequests,
    NotFound,
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
    ...mapActions(['fetchUser']),
  },
}
</script>
