<template>
  <div id="main">
    <div v-if="user.unauthenticated">
      <NotFound></NotFound>
    </div>
    <div v-else-if="user.is_student">
      <StudentAccount></StudentAccount>
    </div>
    <div v-else-if="user.is_tutor">
      <TutorAccount></TutorAccount>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import NotFound from '../components/NotFound'
import StudentAccount from '../components/StudentChangeInfo'
import TutorAccount from '../components/TutorChangeInfo'

export default {
  components: {
    NotFound,
    StudentAccount,
    TutorAccount,
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
