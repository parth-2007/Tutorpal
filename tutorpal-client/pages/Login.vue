<template>
<client-only>
<html data-wf-page="5f59b13f87c4474926e0f928" data-wf-site="5f5844923df4f032aa587322">
<head>
  <meta charset="utf-8">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous">
</head>
<body class="body">
  <div class="div-block-3"><a style="z-index: 2;" href="/" class="w-inline-block"><img src="../components/main/images/logo.jpg" loading="lazy" width="307" srcset="../components/main/images/logo-p-500.jpeg 500w, ../components/main/images/logo-p-800.jpeg 800w, ../components/main/images/logo-p-1080.jpeg 1080w, ../components/main/images/logo.jpg 1432w" sizes="(max-width: 479px) 100vw, (max-width: 767px) 27vw, (max-width: 991px) 24vw, (max-width: 1439px) 21vw, (max-width: 1919px) 16vw, 13vw" alt="" class="image-14"></a>
    <div class="div-block-4"><a style="z-index: 2;"  href="/login" aria-current="page" class="link-2-copy w--current">login</a></div><a style="z-index: 2;"  href="register.html" class="button w-button">register</a></div>
  <div style="margin-top: 200px; margin-bottom: 40px;" class="div-block-23">
    <div class="div-block-20">
      <div class="div-block-21">
        <div class="text-block-4">Sign-In</div>
        <div style="margin-top: 20px;" class="div-block-22">
          <form style="font-family: Poppins;">
            <div class="mb-3">
              <label for="email" class="form-label">Email address</label>
              <input type="email" class="form-control" id="email" v-model="email" >
              <p style="color: hsla(0, 100%, 64%, 1)">{{errors.email}}</p>
            </div>
            <div class="mb-3">
              <label for="password" class="form-label">Password</label>
              <input type="password" class="form-control" id="password" v-model="password">
              <p style="color: hsla(0, 100%, 64%, 1)">{{errors.password}}</p>
            </div>
          </form>
          <button class="button-11 w-button" v-on:click="submitHandler()">Continue</button>
        </div>
        <a href="/password_reset" aria-current="page" style="font-family: Poppins; padding-top: 20px;" class="link-block w-inline-block w--current">Forgot Password?</a>
        <div class="text-block-6">By continuing, you agree to tutorPal&#x27;s <a href="toc.html">Terms of Conditions.</a></div>
      </div>
      <div class="text-block-7">New to TutorPal?</div><a href="register.html" class="button-12 w-button">Create an account</a></div>
  </div>
</body>
</html>
</client-only>
</template>
<style>

</style>
<script>
import getCSRF from '../utils/getCSRF'

export default {
  head () {
    return {
      title: "Login",
    }
  },
  data() {
    return {
      email: '',
      password: '',
      errors: {
        email: '',
        password: '',
      }
    }
  },
  methods: {
    async submitHandler() {
      const emailValidation = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i
      if (!emailValidation.test(this.email)) {
        console.log('failed regex email validation');
        this.errors.email = 'Invalid email'
      } else {
        this.errors.email = ''
      }

      if (!this.password.length > 0) {
        console.log('failed basic password validation');
        this.errors.password = 'Invalid password'
      } else {
        this.errors.password = ''
      }

      if (!this.errors.email && !this.errors.password) {
        const formData = new FormData();
        formData.append('email', this.email);
        formData.append('password', this.password);

        const data = await fetch('api/auth/login/', {
          method: 'POST',
          headers: {
            'X-CSRFToken': getCSRF()
          },
          body: formData
        })
        .then((res) => {
          if (res.status >= 400 && res.status < 600) {
            this.errors.email = 'Something went wrong :('
          }
          return res.json()
        })
        .catch((err) => {
          this.errors.email = 'Something went wrong :('
          return
        })

        if (data && data.error) {
          this.errors.email = data.error
        }

        if (data && data.success === 'Successfully logged in user') {
          this.$router.push('/')
        }
      }
    }
  }
}
require('../components/main/css/webflow.css');
require('../components/main/css/homepage-12.webflow.css');
require('../components/main/css/normalize.css');

</script>
