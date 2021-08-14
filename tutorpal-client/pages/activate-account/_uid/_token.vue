<template>
  <h3 v-if="!error">Redirecting to login...</h3>
  <h3 v-else>There was an error in activating your account</h3>
</template>
<script>
export default {
  data() {
    return {
      error: null,
    }
  },
  async created() {
    await fetch(
      `https://api.tutorpal.org/auth/activate-account/${this.$route.params.uid}/${this.$route.params.token}/`
    )
      .then((res) => {
        if (res.status === 200) {
          this.$router.push('/login')
        } else if (res.status >= 400 && res.status < 600) {
          this.error = 'There has been an error'
        }
        return res.json()
      })
      .catch(() => {
        this.error = 'There has been an error'
      })
  },
}
</script>
