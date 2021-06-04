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
      `api/auth/activate-account/${this.$route.params.uid}/${this.$route.params.token}/`
    )
      .then((res) => {
        if (res.status === 200) {
          this.$router.push('/login')
        } else if (res.status >= 400 && res.status < 600) {
          this.error = 'server error'
        }
        return res.json()
      })
      .catch(() => {
        return { error: 'client error' }
      })
  },
}
</script>
