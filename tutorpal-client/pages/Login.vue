<template>
  <client-only>
    <html
      data-wf-page="5f59b13f87c4474926e0f928"
      data-wf-site="5f5844923df4f032aa587322"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <div v-if="user.isStudent">
      </div>
      <div v-else-if="user.isTutor">
      </div>
      <body v-else class="body">
        <div class="div-block-3">
          <router-link
            style="margin-top: 0px; margin-bottom: -30px"
            to="/"
            class="link-block w-inline-block"
            ><img
              src="../static/main/images/logo.jpg"
              width="250"
              alt=""
              class="image"
          /></router-link>
          <div class="div-block-4">
            <router-link
              style="z-index: 2"
              to="/login"
              aria-current="page"
              class="link-2-copy w--current"
              >login</router-link
            >
          </div>
          <router-link style="z-index: 2" to="/register" class="button w-button"
            >register</router-link
          >
        </div>
        <div
          style="margin-top: 200px; margin-bottom: 40px"
          class="div-block-23"
        >
          <div class="div-block-20">
            <div class="div-block-21">
              <div class="text-block-4">Sign-In</div>
              <p style="color: hsla(0, 100%, 64%, 1); font-family: Poppins">
                {{ errors.global }}
              </p>
              <div style="margin-top: 20px" class="div-block-22">
                <form style="font-family: Poppins" @submit="submitHandler">
                  <div class="mb-3">
                    <label for="email" class="form-label">Email address</label>
                    <input
                      type="email"
                      class="form-control"
                      id="email"
                      v-model="email"
                    />
                  </div>
                  <p style="color: hsla(0, 100%, 64%, 1); font-family: Poppins">
                    {{ errors.email }}
                  </p>
                  <div class="mb-3">
                    <label for="password" class="form-label">Password</label>
                    <input
                      type="password"
                      class="form-control"
                      id="password"
                      v-model="password"
                    />
                  </div>
                  <p style="color: hsla(0, 100%, 64%, 1); font-family: Poppins">
                    {{ errors.password }}
                  </p>
                  <button class="button-11 w-button" @click="submitHandler">
                    Continue
                  </button>
                </form>
              </div>
              <router-link
                to="/reset-password"
                aria-current="page"
                style="font-family: Poppins; margin-top: 20px; width: auto"
                class="link-block w-inline-block w--current"
                >Forgot Password?</router-link
              >
              <div class="text-block-6">
                By continuing, you agree to TutorPal&#x27;s
                <router-link to="/toc">Terms of Conditions.</router-link>
              </div>
            </div>
            <div class="text-block-7">New to TutorPal?</div>
            <router-link to="/register" class="button-12 w-button"
              >Create an account</router-link
            >
          </div>
        </div>
      </body>
    </html>
  </client-only>
</template>
 
<script type="text/javascript">
import { mapGetters, mapActions } from 'vuex'
import getCSRF from '../utils/getCSRF'

export default {
  data() {
    return {
      email: '',
      password: '',
      errors: {
        email: '',
        password: '',
        global: '',
      },
    }
  },
  head() {
    return {
      title: 'Login',
      link: [
        { rel:"stylesheet", type:"text/css", href: "/main/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href: '/main/css/homepage-12.webflow.css' },
        { rel:"stylesheet", type:"text/css", href: "/main/css/normalize.css" },
        { rel: "stylesheet", type: "text/css", href: "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" },
      ],
    }
  },
  computed: mapGetters({ user: 'getUser' }),
  async created() {
    await this.fetchUser()
  },
  methods: {
    ...mapGetters(['getUser']),
    ...mapActions(['fetchUser']),
    validateData() {
      const emailValidation = /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/i
      if (!emailValidation.test(this.email)) {
        this.errors.email = 'Invalid email'
      } else {
        this.errors.email = ''
      }
      if (!this.password.length > 4) {
        this.errors.password = 'Invalid password'
      } else {
        this.errors.password = ''
      }
    },
    async submitHandler(e) {
      e.preventDefault()
      this.validateData()
      if (!this.errors.email && !this.errors.password) {
        const formData = new FormData()
        formData.append('email', this.email)
        formData.append('password', this.password)
        const csrfToken = await getCSRF()
        const data = await fetch('https://api.tutorpal.org/auth/login/', {
          credentials: 'include',
          method: 'POST',
          headers: {
            'X-CSRFToken': csrfToken.success,
            
          },
          body: formData,
        })
        .then((res) => {
          if (res.status >= 400 && res.status < 600) {
            this.errors.global = 'Something went wrong :('
          }
          return res.json()
        })
        .catch(() => {
          this.errors.global = 'Something went wrong :('
        })
        if (data && data.error) {
          this.errors.global = data.error
        }
        if (data && data.success === 'Successfully logged in user') {
          await this.refreshUser()
          await this.refreshTutor()
          await this.refreshStudent()
          this.$router.push('/')
        }
      }
    },
    ...mapActions(['refreshUser', 'refreshTutor', 'refreshStudent']),
  },
}
</script>
<style>
</style>

