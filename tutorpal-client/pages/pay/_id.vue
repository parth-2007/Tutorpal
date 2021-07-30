<template>
    <div v-else-if="user.isStudent">
      <StudentPay></StudentPay>
    </div>
    <div v-else>
      <Forbidden></Forbidden>
    <div
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
