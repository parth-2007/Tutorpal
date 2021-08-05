<template>
  <client-only>
    <html
      data-wf-page="5f59b13f87c4474926e0f928"
      data-wf-site="5f5844923df4f032aa587322"
    >
      <div v-if="user.isStudent">
      </div>
      <div v-else-if="user.isTutor">
      </div>
      <body v-else style="height: 110vh" class="body">
        <div style="height: 170vh" class="section">
          <div
            style="font-family: Poppins; height: 950px; width: 500px"
            class="div-block"
          >
            <div style="margin-top: 15px" class="div-block-4">
              <h1 class="heading">Create a student account</h1>
            </div>
            <div class="div-block-2">
              <div class="text-block">Already have an account?</div>
              <router-link to="/login" class="link">Sign In</router-link>
            </div>
            <div style="margin-top: 20px" class="div-block-3">
              <div>
                <form
                  method="post"
                  enctype="multipart/form-data"
                  @submit="handleSubmit"
                >
                  <div class="row">
                    <div class="col">
                      <label for="firstname" class="form-label"
                        >First Name</label
                      >
                      <input
                        v-model="firstName"
                        id="firstname"
                        type="text"
                        class="form-control"
                        aria-label="First name"
                        required
                      />
                      <p style="color: hsla(0, 100%, 64%, 1)">
                        {{ errors.firstName }}
                      </p>
                    </div>
                    <div style="padding-left: 0px" class="col">
                      <label for="lastname" class="form-label">Last Name</label>
                      <input
                        v-model="lastName"
                        id="lastname"
                        type="text"
                        class="form-control"
                        aria-label="Last name"
                        required
                      />
                      <p style="color: hsla(0, 100%, 64%, 1)">
                        {{ errors.lastName }}
                      </p>
                    </div>
                  </div>
                  <div style="margin-top: 15px" class="mb-3">
                    <label for="emailaddress" class="form-label"
                      >Email Address</label
                    >
                    <input
                      v-model="email"
                      type="email"
                      class="form-control"
                      id="emailaddress"
                      required
                    />
                    <p style="color: hsla(0, 100%, 64%, 1)">
                      {{ errors.email }}
                    </p>
                  </div>
                  <div class="row">
                    <div class="col">
                      <label for="password" class="form-label">Password</label>
                      <input
                        v-model="password"
                        type="password"
                        class="form-control"
                        id="password"
                        required
                      />
                      <p style="color: hsla(0, 100%, 64%, 1)">
                        {{ errors.password }}
                      </p>
                    </div>
                    <div style="padding-left: 0px" class="col">
                      <label for="confirmpassword" class="form-label"
                        >Confirm Password</label
                      >
                      <input
                        v-model="confirmPassword"
                        type="password"
                        id="confirmpassword"
                        class="form-control"
                        required
                      />
                      <p style="color: hsla(0, 100%, 64%, 1)">
                        {{ errors.confirmPassword }}
                      </p>
                    </div>
                  </div>
                  <div
                    style="margin-top: 0px; margin-bottom: 0px; float: left"
                    class="row"
                  >
                    <div
                      style="position: relative; text-align: center"
                      class="col"
                    >
                      <p>
                        <input
                          accept="image/*"
                          type="file"
                          name="image"
                          id="file"
                          style="display: none"
                          @change="handleFile($event)"
                        />
                      </p>
                      <label for="file" style="cursor: pointer"
                        ><p>
                          <img
                            style="border-radius: 400px"
                            :src="src"
                            id="output"
                            width="100"
                            height="100"
                          /></p
                      ></label>
                      <label
                        style="
                          position: absolute;
                          top: 50%;
                          left: 50%;
                          transform: translate(-50%, -50%);
                        "
                        class="form-label"
                        >Upload</label
                      >
                    </div>
                    <p style="color: hsla(0, 100%, 64%, 1)">
                      {{ errors.profilePic }}
                    </p>
                  </div>
                  <div style="margin-top: 0px" class="mb-3">
                    <input
                      id="parentemail"
                      v-model="parentEmail"
                      type="email"
                      class="form-control"
                      placeholder="Enter Parent Email"
                      required
                    />
                  </div>
                  <p style="color: hsla(0, 100%, 64%, 1)">
                    {{ errors.parentEmail }}
                  </p>
                  <div class="form-group row">
                    <label for="birthdate" class="col-2 col-form-label"
                      >Birthdate</label
                    >
                    <div class="col-10">
                      <input
                        v-model="birthDate"
                        id="birthdate"
                        class="form-control"
                        type="date"
                        required
                      />
                    </div>
                    <p style="color: hsla(0, 100%, 64%, 1)">
                      {{ errors.birthDate }}
                    </p>
                  </div>
                  <div
                    style="margin-top: 15px; margin-bottom: 15px"
                    class="form-check"
                  >
                    <input
                      v-model="toc"
                      id="toc"
                      class="form-check-input"
                      nam="checkbox"
                      type="checkbox"
                      required
                    />
                    <label class="form-check-label" for="toc">
                      I agree with the
                      <router-link to="/toc">Terms of Service</router-link>
                    </label>
                    <p style="color: hsla(0, 100%, 64%, 1)">
                      {{ errors.toc }}
                    </p>
                  </div>
                  <p style="color: hsla(0, 100%, 64%, 1)">
                    {{ errors.global }}
                  </p>
                  <button
                    style="margin-bottom: 20px"
                    class="btn btn-primary"
                    type="submit"
                  >
                    Register
                  </button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </body>
    </html>
  </client-only>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import getCSRF from '../utils/getCSRF'
export default {
  data() {
    return {
      toc: false,
      email: '',
      firstName: '',
      lastName: '',
      password: '',
      confirmPassword: '',
      profilePic: null,
      parentEmail: '',
      birthDate: '',
      errors: {
        email: '',
        firstName: '',
        lastName: '',
        password: '',
        confirmPassword: '',
        profilePic: '',
        parentEmail: '',
        birthDate: '',
        global: '',
      },
      src: 'https://image.flaticon.com/icons/png/512/149/149071.png',
    }
  },
  head() {
    return {
      title: 'Student Registration',
      link: [
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/register/css/webflow.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/register/css/2tor4u-2-0.webflow.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/register/css/normalize.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css',
        },
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
    handleFile(e) {
      // decrease file size before processing
      const image = e.target.files || e.dataTransfer.files
      this.src = URL.createObjectURL(e.target.files[0])
      this.profilePic = image.length > 0 ? image : null
      if (e.target.files[0].size > 100000){
        this.errors.profilePic = "File size is too high! Please upload a file less than 100 Kilobytes"
      }
      else{
        this.errors.profilePic = ""
      }
    },
    checkErrors() {
      let isError = false
      Object.keys(this.errors).forEach((key) => {
        if (this.errors[key].length > 0) {
          isError = true
        }
      })
      return isError
    },
    validateData() {
      if (!this.toc) {
        this.errors.global = 'Please read and agree to the Terms of Condition'
      } else {
        this.errors.global = ''
      }
      const birthday = +new Date(this.birthDate)
      const age = Math.floor((Date.now() - birthday) / 31557600000)
      if (age < 6) {
        this.errors.birthDate =
          'You must at least 6 years old to register as a student'
      }
      const emailValidation =
        /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/i
      if (!emailValidation.test(this.email)) {
        this.errors.email = 'Invalid email'
      } else {
        this.errors.email = ''
      }
      if (!emailValidation.test(this.parentEmail)) {
        this.errors.parentEmail = 'Invalid parent email'
      } else {
        this.errors.parentEmail = ''
      }
      if (!this.password.length > 5) {
        this.errors.password =
          'The Password length must be greater than 5 characters'
      } else {
        this.errors.password = ''
      }
      if (this.password !== this.confirmPassword) {
        this.errors.password =
          'The Password and Confirm Password must be the same'
        this.errors.confimPassword =
          'Password and Confirm Password must be the same'
      } else {
        this.errors.password = ''
        this.errors.confirmPassword = ''
      }
      if (this.firstName.length < 1) {
        this.errors.firstName = 'Invalid first name'
      } else {
        this.errors.firstName = ''
      }
      if (this.lastName.length < 1) {
        this.errors.lastName = 'Invalid last name'
      } else {
        this.errors.lastName = ''
      }
    },
    async handleSubmit(e) {
      e.preventDefault()
      if (!this.checkErrors()) {
        const formData = new FormData()
        const user = {
          email: this.email,
          password: this.password,
          first_name: this.firstName,
          last_name: this.lastName,
        }
        if (this.profilePic) {
          formData.append('profile_pic', this.profilePic[0])
        }
        formData.append('user', JSON.stringify(user))
        formData.append(
          'student',
          JSON.stringify({
            parent_email: this.parentEmail,
            birth_date: this.birthDate,
          })
        )
        const data = await fetch('https://api.tutorpal.org/auth/register-student/', {
          method: 'POST',
          headers: {
            'X-CSRFToken': (await getCSRF()).success,
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
        } else {
          this.$router.push('/checkemail')
        }
      }
    },
  },
}
</script>
