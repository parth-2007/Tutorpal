<template>
  <div v-if="user.unauthenticated">
    <NotFound></NotFound>
  </div>
  <div v-else-if="user.isStudent">
    <StudentPayments></StudentPayments>
  </div>
  <div v-else-if="user.isTutor">
    <TutorPayments></TutorPayments>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
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
