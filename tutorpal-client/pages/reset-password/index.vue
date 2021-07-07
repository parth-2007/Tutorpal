<template>
  <client-only>
  <div>
    <form style="margin-left: 25px; margin-top: 25px; font-family: Poppins; " @submit="onSubmit">
      <p style="font-size: 16px; color: #bb0a1e;" v-if="errors">{{ errors }}</p>
      <p v-if="show" style="font-size: 16px; color: green;">We have sent an email with information to reset your account's password. It will be in your inbox shortly</p>
      <div style="width: 600px" class="input-group mb-3">
        <input v-model="email" type="text" class="form-control" placeholder="Enter the email of your account">
        <button style="margin-left: 5px" class="btn btn-primary" @click="onSubmit">Submit</button>    
      </div>
    </form>
  </div>
  </client-only>
</template>
<script>
import getCSRF from '../../utils/getCSRF'
export default {
  data() {
    return {
      email: '',
      errors: '',
      show: false
    }
  },
  head() {
    return {
      title: 'Forgot Password',
      link: [{rel: 'stylesheet', type: 'text/css', href:'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css'}],
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
            this.show = true
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