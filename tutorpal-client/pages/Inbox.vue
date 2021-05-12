<template>
  <div id="main">
    <div v-if="user.unauthenticated">
      <NotFound></NotFound>
    </div>
    <div v-else-if="user.isStudent">
      <StudentInbox></StudentInbox>
    </div>
    <div v-else-if="user.isTutor">
      <TutorInbox></TutorInbox>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import NotFound from '../components/NotFound'
import StudentInbox from '../components/StudentInbox'
import TutorInbox from '../components/TutorInbox'

export default {
  components: {
    NotFound,
    StudentInbox,
    TutorInbox,
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
