<template>
  <div v-if="user.unfetched===undefined" id="main">
    <div v-if="user.isStudent">
      <SetTimezone></SetTimezone>
    </div>
    <div v-else-if="user.isTutor">
      <SetTimezone></SetTimezone>
    </div>
    <div v-else>
      <NotFound></NotFound>
    </div>
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
