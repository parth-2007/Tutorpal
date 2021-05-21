<template>
  <div>
    <form style="font-family: Poppins; padding-bottom: 20px">
      <div class="row">
        <div class="col">
          <label for="firstname" class="form-label">First Name</label>
          <input
            v-model="user.firstName"
            type="text"
            class="form-control"
            id="firstname"
            aria-label="First name"
            required
          />
        </div>
        <div style="padding-left: 0px" class="col">
          <label for="lastname" class="form-label">Last Name</label>
          <input
            v-model="user.lastName"
            type="text"
            class="form-control"
            id="lastname"
            aria-label="Last name"
            required
          />
        </div>
      </div>
      <div style="margin-top: 15px" class="mb-3">
        <label for="emailaddress" class="form-label">Email Address</label>
        <input
          v-model="user.email"
          type="email"
          class="form-control"
          id="emailaddress"
          required
        />
      </div>
      <div style="margin-top: 15px; float: left" class="row">
        <div style="position: relative; text-align: center" class="col">
          <p>
            <input
              type="file"
              accept="image/*"
              name="image"
              id="file"
              onchange="loadFile(event)"
              style="display: none"
            />
          </p>
          <label for="file" style="cursor: pointer"
            ><p>
              <img
                :src="user.profilePic"
                style="border-radius: 400px"
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
      </div>
      <div style="margin-top: 25px" class="mb-3">
        <input
          v-model="student.parentEmail"
          type="email"
          class="form-control"
          id="parentemail"
          placeholder="Enter Parent Email"
          required
        />
      </div>
      <div class="form-group row">
        <label for="birthdate" class="col-2 col-form-label">Birthdate</label>
        <div class="col-10">
          <input
            v-model="student.birthDate"
            class="form-control"
            type="date"
            id="birthdate"
            required
          />
        </div>
      </div>
      <!-- <label for="password" class="form-label">Verify Password</label>
    <input
      style="margin-bottom: 15px"
      type="password"
      class="form-control"
      id="password"
      required
    /> -->
    </form>
    <button @click="handleSubmit()" class="btn btn-primary">
      Update Information
    </button>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import getCSRF from '../utils/getCSRF'
import objectsEqual from '../utils/objectsEqual'
import { unpackUser, unpackStudent } from '../utils/unPackObjects'
import { keysToSnake } from '../utils/changeObjectNaming'

export default {
  data() {
    return {
      student: {},
      user: {},
      errors: {
        email: '',
        firstName: '',
        lastName: '',
        profilePic: '',
        parentEmail: '',
        birthDate: '',
      },
    }
  },
  async created() {
    await this.fetchStudent()
    await this.fetchUser()
    this.student = { ...this.getStudent() }
    this.user = { ...this.getUser() }
  },
  methods: {
    ...mapActions(['fetchStudent', 'fetchUser', 'updateStudent', 'updateUser']),
    ...mapGetters(['getUser', 'getStudent']),

    handleFile(e) {
      const image = e.target.files || e.dataTransfer.files
      image.src = URL.createObjectURL(image)
      this.profilePic = image.length > 0 ? image : null
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
      const emailValidation = /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/i
      if (!emailValidation.test(this.user.email)) {
        this.errors.email = 'Invalid email'
      } else {
        this.errors.email = ''
      }

      if (!emailValidation.test(this.student.parentEmail)) {
        this.errors.parentEmail = 'Invalid email'
      } else {
        this.errors.parentEmail = ''
      }

      if (this.user.firstName.length < 1) {
        this.errors.firstName = 'Invalid name'
      } else {
        this.errors.firstName = ''
      }

      if (this.user.lastName.length < 1) {
        this.errors.lastName = 'Invalid name'
      } else {
        this.errors.lastName = ''
      }
    },
    async handleSubmit() {
      this.validateData()

      if (
        !this.checkErrors() &&
        (!objectsEqual(this.student, this.getStudent()) ||
          !objectsEqual(this.user, this.getUser()))
      ) {
        // const formData = new FormData()
        // formData.append(
        //   'tutor',
        //   JSON.stringify({ ...this.tutor, user: { ...this.user } })
        // )
        const csrfToken = await getCSRF()
        if (csrfToken.success !== null && csrfToken.success !== undefined) {
          const data = await fetch('api/students/me/', {
            method: 'PATCH',
            headers: {
              'X-CSRFToken': csrfToken.success,
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              student: { ...keysToSnake(unpackStudent(this.student)) },
              user: { ...keysToSnake(unpackUser(this.user)) },
            }),
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
            if (!objectsEqual(this.student, this.getStudent())) {
              this.updateStudent({ ...this.student })
            }
            if (!objectsEqual(this.user, this.getUser())) {
              this.updateUser({ ...this.user })
            }
            this.$emit('modalSubmit')
            // this.errors.global = 'Something went wrong :('
          }
        } else {
          this.errors.global = 'Something went wrong :('
        }
      } else {
        this.$emit('modalSubmit')
      }
    },
  },
}
</script>