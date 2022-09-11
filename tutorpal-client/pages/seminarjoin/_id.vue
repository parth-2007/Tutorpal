<template>
  <div v-if="!user.unfetched" id="main">
    <div v-if="user.isStudent">
      <StudentJoinSeminars></StudentJoinSeminars>
    </div>
    <div v-else-if="user.isTutor">
      <TutorJoinSeminars></TutorJoinSeminars>
    </div>
    <div v-else>
      <Forbidden></Forbidden>
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
