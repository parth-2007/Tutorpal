<template>
  <div v-if="!user.unfetched" id="main">
    <div v-if="user.isStudent">
      <StudentPayments></StudentPayments>
    </div>
    <div v-else-if="user.isTutor">
      <TutorPayments></TutorPayments>
    </div>
    <div v-else>
      <NotFound></NotFound>
    </div>
  </div>
  <div v-else>
    <Loader></Loader>
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
