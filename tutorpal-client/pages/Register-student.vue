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
          media="print"
          onload="this.media='all'"
        />
      </head>
      <div v-if="user.isStudent"></div>
      <div v-else-if="user.isTutor"></div>
      <body v-else style="min-height: 100vh" class="registerbody">
        <div style="height: 150vh" class="registersection">
          <div
            style="font-family: Poppins; width: 500px; overflow-y: auto;"
            class="registerdiv-block"
          >
            <div style="margin-top: 15px" class="registerdiv-block-4">
              <h1 class="registerheading">Create a student account</h1>
            </div>
            <div class="registerdiv-block-2">
              <div class="registertext-block">Already have an account?</div>
              <router-link to="/login" class="registerlink"
                >Sign In</router-link
              >
            </div>
            <div style="margin-top: 20px" class="registerdiv-block-3">
              <div>
                <form
                  method="post"
                  enctype="multipart/form-data"
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
                    <p style="color: hsla(0, 100%, 64%, 1); margin-left: 15px;">
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
                  <p style="margin-top: 10px; font-family: Poppins; font-size: 16px;color: #008000;">{{success}}</p>
                </form>
                <button
                  style="margin-bottom: 20px"
                  class="btn btn-primary"
                  @click="handleSubmit"
                >
                  Register
                </button>
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
        toc: ''
      },
      success:"",
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
  },
  methods: {
    ...mapGetters(['getUser']),
    ...mapActions(['fetchUser']),
    handleFile(e) {
      // decrease file size before processing
      const image = e.target.files || e.dataTransfer.files
      this.src = URL.createObjectURL(e.target.files[0])
      this.profilePic = image.length > 0 ? image : null
      if (e.target.files[0].size > 100000) {
        this.errors.profilePic =
          'File size is too high! Please upload a file less than 100 Kilobytes'
        this.errors.global = "There seems to be a problem with your request, scroll up to see whats wrong."
      } else {
        this.errors.profilePic = ''
        this.errors.global=''
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
      let counter = 0
      const requiredFields = [
        'email',
        'firstName',
        'lastName',
        'parentEmail',
        'password',
        'confirmPassword',
      ]
      requiredFields.forEach((field) => {
        if (this[field].length < 1) {
          this.errors[field] = 'This field is required'
        } else {
          this.errors[field] = ''
          counter+=1
        }
      })
      if (!this.toc) {
        this.errors.toc = 'Please read and agree to the Terms of Condition'
      } else {
        this.errors.global = ''
        counter+=1
      }
      const birthday = new Date(this.birthDate)
      const age = Math.floor((Date.now() - birthday) / 31557600000)
      if(age<0){
        this.errors.birthDate = "Hmmm...our data shows us you haven't been born yet"
      }
      else if(age>70){
        this.errors.birthDate = "Sorry but our platform doesn't accept students above the age of 70 for technical reasons. If you like, you can contact our support team: info@tutorpal.org"
      }
      else if(age<15){
        this.errors.birthDate = "You must be at least 15 years old to register as a tutor."
      }
      else if(isNaN(age)){
        this.errors.birthDate = "We're not detecting a birthdate here..."
      }
      else {
        counter+=1
        this.errors.birthDate = ""
      }
      const emailValidation =
        /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/i
      if (!emailValidation.test(this.email)) {
        this.errors.email = 'Invalid email'
      } else {
        this.errors.email = ''
        counter+=1
      }
      if (!emailValidation.test(this.parentEmail)) {
        this.errors.parentEmail = 'Invalid parent email'
      } else {
        this.errors.parentEmail = ''
        counter+=1
      }
      if (!this.password.length > 5) {
        this.errors.password =
          'The Password length must be greater than 5 characters'
      } else {
        this.errors.password = ''
        counter+=1
      }
      if (this.password !== this.confirmPassword) {
        this.errors.password =
          'The Password and Confirm Password must be the same'
        this.errors.confimPassword =
          'Password and Confirm Password must be the same'
      } else {
        this.errors.password = ''
        this.errors.confirmPassword = ''
        counter+=1
      }
      if (this.firstName.length < 1) {
        this.errors.firstName = 'Invalid first name'
      } else {
        this.errors.firstName = ''
        counter+=1
      }
      if (this.lastName.length < 1) {
        this.errors.lastName = 'Invalid last name'
      } else {
        this.errors.lastName = ''
        counter+=1
      }
      if (counter!==14){
        this.errors.global = "There seems to be a problem with your request, scroll up to see whats wrong."
        this.success = ""
      }
      else if(counter===14){
        this.success = "You have successfully created a student account!"
        this.errors.global = ''
      }
    },
    async handleSubmit(e) {
      this.validateData()
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
        const data = await fetch(
          process.env.API_URL + '/auth/register-student/',
          {
            credentials: 'include',
            method: 'POST',
            headers: {
              'X-CSRFToken': (await getCSRF()).success,
            },
            body: formData,
          }
        )
          .then((res) => {
            if (res.status >= 400 && res.status < 600) {
             this.errors.global = "There seems to be a problem with your request, scroll up to see whats wrong."
            }
            return res.json()
          })
          .catch(() => {
            this.errors.global = "There seems to be a problem with your request, scroll up to see whats wrong."
          })
        if (data && data.error) {
          this.errors.global = data.error
          this.errors.global = "There seems to be a problem with your request, scroll up to see whats wrong."
        } else {
          this.success = "You have successfully created a student account!"
          this.$router.push('/checkemail')
        }
      }
    },
  },
}
</script>
