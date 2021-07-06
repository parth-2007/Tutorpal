<template>
  <client-only>
    <form @submit="onSubmit">
      <input type="text" v-model="email" />
      <p v-if="errors">{{ errors }}</p>
      <button @click="onSubmit">Submit</button>
    </form>
  </client-only>
</template>
<script>
import getCSRF from '../../utils/getCSRF'
export default {
  data() {
    return {
      email: '',
      errors: '',
    }
  },
  methods: {
    async onSubmit(e) {
      e.preventDefault()
      const emailValidation = /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/i
      if (!this.email || !emailValidation.test(this.email)) {
        this.errors = 'This is an invalid email address'
      } else {
        this.errors = ''
        const formData = new FormData()
        formData.append('email', this.email)

        await fetch('api/auth/reset-password/', {
          method: 'POST',
          headers: {
            'X-CSRFToken': (await getCSRF()).success,
          },
          body: formData,
        })
        .then((res) => {
          if (res.status === 400) {
            this.errors = 'This is not an existing email address'
          } else if (res.status === 200) {
            this.$router.push('/checkemail')
          } else if (res.status >= 400 && res.status < 600) {
            this.errors = 'Something went wrong :('
          }
        })
        .catch(() => {
          this.errors = 'Something went wrong :('
        })
      }
    },
  },
}
</script>