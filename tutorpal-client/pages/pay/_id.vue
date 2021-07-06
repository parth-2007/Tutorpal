<template>
    <div v-if="user.unauthenticated || user.isTutor">
      <NotFound></NotFound> <!-- Forbidden -->
    </div>
    <div v-else-if="user.isStudent">
      <StudentPay></StudentPay>
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