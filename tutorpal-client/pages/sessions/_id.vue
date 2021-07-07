<template>
    <div v-if="user.unauthenticated">
      <Forbidden></Forbidden>
    </div>
    <div v-else-if="user.isStudent">
      <StudentWorkspace></StudentWorkspace>
    </div>
    <div v-else-if="user.isTutor">
      <TutorWorkspace></TutorWorkspace>
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