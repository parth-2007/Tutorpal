<template>
  <p>Please refresh if you were not automatically redirect</p>
</template>
<script>
import { mapActions } from 'vuex'

export default {
  created() {
    this.logoutUser()
    this.$router.push('/')
  },
  methods: {
    ...mapActions(['logoutUser']),
  },
}
</script>