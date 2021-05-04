<template>
  <div id="main">
    <div v-if="user.unauthenticated">
      <TutorAccount></TutorAccount>
    </div>
    <div v-else-if="user.is_student">
      <NotFound></NotFound>
    </div>
    <div v-else-if="user.is_tutor">
      <StudentAccount></StudentAccount>
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
