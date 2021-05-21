<template>
  <p>Please refresh if you were not automatically redirect</p>
</template>
<script>
import { mapActions } from 'vuex'

export default {
  created() {
    this.logoutUser()
    this.logoutStudent()
    this.logoutTutor()
    this.$router.push('/')
  },
  methods: {
    ...mapActions(['logoutUser', 'logoutTutor', 'logoutStudent']),
  },
}
</script>