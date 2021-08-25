<template>
  <div style="font-family: Poppins; margin-top: 60px">
    <h1 style="font-size: 28px; text-align: center;">Please refresh if you were not automatically redirected</h1>
    <p style="font-size: 16px; text-align: center;">Or click here: <router-link to="/" style="font-family: Poppins; color: #41a8d3;">Continue</router-link></p>
  </div>
</template>
<script>
import { mapActions } from 'vuex'

export default {
  head() {
    return {
      title: 'Logging Out',
    }
  },
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