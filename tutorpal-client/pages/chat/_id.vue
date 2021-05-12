<template>
    <div v-if="user.unauthenticated">
      <NotFound></NotFound>
    </div>
    <div v-else-if="user.isStudent">
      <StudentChat></StudentChat>
    </div>
    <div v-else-if="user.isTutor">
      <TutorChat></TutorChat>
    </div>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  head() {
    return {}
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