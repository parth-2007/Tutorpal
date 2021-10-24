<template>
  <client-only>
    <head>
      <meta charset="utf-8" />
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
        media="print"
        onload="this.media='all'"
      />
    </head>
    <form
      style="font-family: Poppins; margin-top: 25px; margin-left: 25px"
      @submit="handleSubmit"
    >
      <p style="font-size: 16px; color: #bb0a1e" v-if="error">{{ error }}</p>
      <div style="width: 1000px" class="input-group mb-3">
        <input
          placeholder="Enter password here"
          class="form-control"
          type="password"
          v-model="password"
        />
        <input
          placeholder="Confirm password here"
          style="margin-right: 5px; margin-left: 5px"
          class="form-control"
          type="password"
          v-model="confirmPassword"
        />
        <button class="btn btn-primary" @click="handleSubmit">Submit</button>
      </div>
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
  head() {
    return {
      title: 'Password Reset',
    }
  },
  methods: {
    async handleSubmit(e) {
      e.preventDefault()
      if (this.password.length < 5) {
        this.error = 'Invalid password, password is less than 5 characters long'
      } else if (this.password !== this.confirmPassword) {
        this.error = 'Password and Confirm password should match.'
      } else {
        await fetch(
          process.env.API_URL +
            'auth/password-reset/' +
            this.$route.params.uid +
            '/' +
            this.$route.params.token +
            '/',
          {
            credentials: 'include',
            method: 'POST',
            headers: {
              'X-CSRFToken': (await getCSRF()).success,
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
