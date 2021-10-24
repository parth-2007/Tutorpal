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
          {{ errors.firstName }}
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
          {{ errors.lastName }}
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
        {{ errors.email }}
      </div>
      <div style="margin-top: 15px; float: left" class="row">
        <div style="position: relative; text-align: center" class="col">
          <p>
            <input
              @change="handleFile"
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
                :src="src"
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
        {{ errors.parentEmail }}
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
          {{ errors.birthDate }}
        </div>
      </div>
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
      src: '',
    }
  },
  async created() {
    await this.fetchStudent()
    await this.fetchUser()
    this.student = { ...this.getStudent() }
    this.user = { ...this.getUser() }
    this.src = this.user.profilePic
  },
  methods: {
    ...mapActions(['fetchStudent', 'fetchUser', 'updateStudent', 'updateUser']),
    ...mapGetters(['getUser', 'getStudent']),
    handleFile(e) {
      const image = e.target.files || e.dataTransfer.files
      this.src = URL.createObjectURL(e.target.files[0])
      this.profilePic = image.length > 0 ? image : null
      if (e.target.files[0].size > 100000) {
        this.errors.profilePic =
          'File size is too high! Please upload a file less than 100 Kilobytes'
      } else {
        this.errors.profilePic = ''
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
      const emailValidation =
        /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/i
      if (!emailValidation.test(this.user.email)) {
        this.errors.email = 'Invalid user email'
      } else {
        this.errors.email = ''
      }

      if (!emailValidation.test(this.student.parentEmail)) {
        this.errors.parentEmail = 'Invalid parent email'
      } else {
        this.errors.parentEmail = ''
      }

      if (this.user.firstName.length < 1) {
        this.errors.firstName = 'Invalid first name'
      } else {
        this.errors.firstName = ''
      }

      if (this.user.lastName.length < 1) {
        this.errors.lastName = 'Invalid last name'
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
        const csrfToken = await getCSRF()
        if (csrfToken.success !== null && csrfToken.success !== undefined) {
          const formData = new FormData()
          if (this.profilePic) {
            formData.append('profile_pic', this.profilePic[0])
          }
          formData.append(
            'student',
            JSON.stringify(keysToSnake(unpackStudent({ ...this.student })))
          )
          formData.append(
            'user',
            JSON.stringify(keysToSnake(unpackUser({ ...this.user })))
          )
          const data = await fetch('/api/auth/update-student/', {
            credentials: 'include',
            method: 'PATCH',
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
          } else {
            if (!objectsEqual(this.student, this.getStudent())) {
              this.updateStudent({ ...this.student })
            }
            if (!objectsEqual(this.user, this.getUser())) {
              this.updateUser({ ...this.user })
            }
            this.$emit('modalSubmit')
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