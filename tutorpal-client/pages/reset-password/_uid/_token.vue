<template>
  <client-only>
    <form @submit="handleSubmit">
      <input type="password" v-model="password" />
      <input type="password" v-model="confirmPassword" />
      <p v-if="error">{{ error }}</p>
      <button @click="handleSubmit">Submit</button>
    </form>
  </client-only>
</template>
<script>
import getCSRF from '../../../utils/getCSRF'
export default {
  data() {
    return {
      error: null,
      password: '',
      confirmPassword: '',
    }
  },
  methods: {
    async handleSubmit(e) {
      e.preventDefault()
      if (this.password.length < 1) {
        this.error = 'Invalid password'
      } else if (this.password !== this.confirmPassword) {
        this.error = 'Password and Confirm password should match'
      } else {
        await fetch(
          `api/auth/password-reset/${this.$route.params.uid}/${this.$route.params.token}/`,
          {
            method: 'POST',
            headers: {
              'X-CSRFToken': await (await getCSRF()).success,
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ password: this.password }),
          }
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
      }
    },
  },
}
</script>
