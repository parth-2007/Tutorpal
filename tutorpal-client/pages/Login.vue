<template>
  <client-only>
    <html
      data-wf-page="5f59b13f87c4474926e0f928"
      data-wf-site="5f5844923df4f032aa587322"
    >
      <head>
        <meta charset="utf-8" />
        <link
          rel="stylesheet"
          href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        />
        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
        />
      </head>
      <div v-if="user.isStudent">
        <Loader />
      </div>
      <div v-else-if="user.isTutor">
        <Loader />
      </div>
      <body v-else class="homebody">
        <div class="homediv-block-3">
          <router-link
            style="margin-top: 0px; margin-bottom: -30px"
            to="/"
            class="homelink-block w-inline-block"
            ><img
              src="../static/student/images/logo.jpg"
              width="250"
              alt=""
              class="homeimage"
          /></router-link>
          <div class="homediv-block-4">
            <router-link
              style="z-index: 2"
              to="/login"
              aria-current="page"
              class="homelink-2-copy w--current"
              >login</router-link
            >
          </div>
          <router-link
            style="z-index: 2"
            to="/register"
            class="homebutton w-button"
            >register</router-link
          >
        </div>
        <div
          style="margin-top: 200px; margin-bottom: 40px"
          class="homediv-block-23"
        >
          <div class="homediv-block-20">
            <div class="homediv-block-21">
              <div class="hometext-block-4">Sign-In</div>
              <p style="color: hsla(0, 100%, 64%, 1); font-family: Poppins">
                {{ errors.global }}
              </p>
              <div style="margin-top: 20px" class="homediv-block-22">
                <form style="font-family: Poppins" @submit="submitHandler">
                  <div class="homemb-3">
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
                  <div class="homemb-3">
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
                  <button
                    class="homebutton-11 w-button"
                    @click="submitHandler"
                    type="submit"
                  >
                    Continue
                  </button>
                </form>
              </div>
              <router-link
                to="/reset-password"
                aria-current="page"
                style="font-family: Poppins; margin-top: 20px; width: auto"
                class="homelink-block w-inline-block w--current"
                >Forgot Password?</router-link
              >
              <div class="hometext-block-6">
                By continuing, you agree to TutorPal&#x27;s
                <router-link to="/toc">Terms of Conditions.</router-link>
              </div>
            </div>
            <div class="hometext-block-7">New to TutorPal?</div>
            <router-link to="/register" class="homebutton-12 w-button"
              >Create an account</router-link
            >
          </div>
        </div>
        <a
          style="
            position: fixed;
            bottom: 0px;
            right: 10px;
            font-family: Poppins;
            color: red;
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
          "
          href="https://www.youtube.com/channel/UCTbysqe_AM_eY9N3eVpiY6A"
          target="_blank"
          ><i class="fa fa-youtube-play" style="font-size: 36px"></i
          ><a style="margin-left: 10px; text-decoration: none">Tutorials</a></a
        >
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
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/webflow.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/normalize.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/student-main.webflow.css',
        },
      ],
    }
  },
  computed: mapGetters({ user: 'getUser' }),
  async created() {
    await this.fetchUser()
    console.log(process.env.API_URL)
  },
  methods: {
    ...mapGetters(['getUser']),
    ...mapActions(['fetchUser']),
    validateData() {
      const emailValidation =
        /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/i
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
        const data = await fetch(process.env.API_URL + '/auth/login/', {
          credentials: 'include',
          method: 'POST',
          headers: {
            'X-CSRFToken': csrfToken.success,
          },
          body: formData,
        })
          .then((res) => {
            if (res.error === 'this email is taken') {
              this.errors.email = 'this email is taken'
            }
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

