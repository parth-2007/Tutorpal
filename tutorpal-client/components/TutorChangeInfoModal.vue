<template>
  <div>
    <form>
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
      <div style="margin-top: 15px" class="mb-3">
        <label for="paypalemailaddress" class="form-label"
          >PayPal Email Address</label
        >
        <input
          v-model="tutor.paypalEmail"
          type="email"
          class="form-control"
          id="paypalemailaddress"
          required
        />
      </div>
      <div class="mb-3">
        <label for="birthdate" class="form-label">Birthdate</label>
        <input
          v-model="tutor.birthDate"
          class="form-control"
          type="date"
          id="birthdate"
          required
        />
      </div>
      <div class="mb-3">
        <label for="birthdate" class="form-label">Gender</label>
        <select
          v-model="tutor.gender"
          class="form-select"
          id="gender"
          aria-label="Default select example"
        >
          <option value="1">Prefer Not To Say</option>
          <option value="2">Male</option>
          <option value="3">Female</option>
          <option value="4">Other</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="firstname" class="form-label">First Name</label>
        <input
          v-model="user.firstName"
          class="form-control"
          id="firstname"
          required
        />
      </div>
      <div class="mb-3">
        <label for="lastname" class="form-label">Last Name</label>
        <input
          v-model="user.lastName"
          class="form-control"
          id="lastname"
          required
        />
      </div>
      <div class="mb-3">
        <label for="occupation" class="form-label">Occupation</label>
        <input
          v-model="tutor.occupation"
          class="form-control"
          id="occupation"
          required
        />
      </div>
      <div class="mb-3">
        <label for="subject" class="form-label">Subjects</label>
        <input
          v-model="tutor.subjects"
          class="form-control"
          id="subject"
          required
        />
      </div>
      <div class="text-block-5"><b>Class Description</b></div>
      <textarea
        v-model="tutor.whatYouTeach"
        style="height: 250px"
        class="form-control"
        id="description"
        rows="3"
      ></textarea>
      <div style="margin-top: 15px" class="row">
        <div class="col">
          <label for="major" class="form-label">Major</label>
          <input
            v-model="tutor.major"
            type="text"
            class="form-control"
            id="major"
            required
          />
        </div>
        <div style="padding-left: 0px" class="col">
          <label for="gpa" class="form-label">GPA</label>
          <input
            v-model="tutor.gpa"
            type="number"
            id="gpa"
            min="0"
            max="5"
            class="form-control"
          />
        </div>
        <div style="padding-left: 0px" class="col">
          <label for="education" class="form-label">Education</label>
          <select
            v-model="tutor.education"
            style="margin-top: 0px"
            class="form-select"
            id="education"
            aria-label="Default select example"
          >
            <option selected>Select</option>
            <option value="High School">High School</option>
            <option value="Bachelors Degree">Bachelors Degree</option>
            <option value="Masters Degree">Masters Degree</option>
            <option value="Ph.D.">Ph.D.</option>
          </select>
        </div>
        <div style="padding-left: 0px" class="col">
          <label for="school" class="form-label">School/College</label>
          <input
            v-model="tutor.school"
            type="text"
            class="form-control"
            id="school"
            required
          />
        </div>
      </div>
      <textarea
        v-model="tutor.qualifications"
        style="height: 250px; margin-top: 25px"
        class="form-control"
        placeholder="Qualifications"
        id="educationdescription"
        rows="3"
      ></textarea>
      <div style="margin-top: 15px; margin-bottom: 5px" class="text-block-5">
        <b>Linkedin Profile Link(Optional)</b>
      </div>
      <input
        v-model="tutor.linkedIn"
        class="form-control"
        id="linkedin"
        placeholder="https://www.linkedin.com/in/johndoe"
      />
      <div class="row">
        <div class="col">
          <textarea
            v-model="tutor.bio"
            style="height: 250px; margin-top: 25px"
            class="form-control"
            id="bio"
            placeholder="Eg. My hobbies are..."
            rows="3"
          ></textarea>
        </div>
        <div style="padding-left: 0px" class="col">
          <div style="position: relative; text-align: center" class="col">
            <p>
              <input
                type="file"
                accept="image/"
                name="image"
                id="file"
                @change="handleFile"
                style="display: none"
              />
            </p>
            <label for="file" style="cursor: pointer"
              ><p>
                <img
                  style="border-radius: 400px"
                  :src="src"
                  id="output"
                  width="250"
                  height="250"
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
      </div>
      <label
        style="margin-top: 15px"
        for="rates"
        id="pricedisplay"
        class="form-label"
        >Pricing:</label
      >
      <input
        v-model="tutor.rates"
        type="number"
        min="0"
        max="1000"
        class="form-control"
        id="rates"
      />
      <div style="margin-top: 15px" class="row">
        <div class="col">
          <label for="teachexp" class="form-label"
            >Years of Teaching Experience</label
          >
          <input
            v-model="tutor.teachExp"
            type="number"
            id="teachexp"
            min="0"
            max="30"
            class="form-control"
          />
        </div>
        <div style="padding-left: 0px" class="col">
          <label for="profexp" class="form-label"
            >Years of Professional Experience</label
          >
          <input
            v-model="tutor.profExp"
            id="profexp"
            type="number"
            min="0"
            max="30"
            class="form-control"
          />
        </div>
      </div>
      <label style="margin-top: 15px" for="availability" class="form-label"
        >Availability</label
      >
      <input
        v-model="tutor.availability"
        class="form-control"
        id="availability"
        placeholder="Mondays, 4:00 PM - 6:00 PM"
      />
    </form>
    <button
      @click="handleSubmit"
      style="margin-top: 15px; font-family: Poppins; margin-left: 0px"
      class="btn btn-primary"
    >
      Update Profile
    </button>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import getCSRF from '../utils/getCSRF'
import objectsEqual from '../utils/objectsEqual'
import { unpackTutor, unpackUser } from '../utils/unPackObjects'
import { keysToSnake } from '../utils/changeObjectNaming'

export default {
  data() {
    return {
      tutor: {},
      user: {},
      profilePic: null,
      src: '',
      errors: {
        email: '',
        firstName: '',
        lastName: '',
        profilePic: '',
        paypalEmail: '',
        birthDate: '',
        gender: '',
        occupation: '',
        subjects: '',
        whatYouTeach: '',
        major: '',
        gpa: '',
        education: '',
        school: '',
        qualifications: '',
        linkedIn: '',
        bio: '',
        rates: '',
        teachExp: '',
        profExp: '',
        availability: '',
        global: '',
      },
    }
  },
  async created() {
    await this.fetchTutor()
    await this.fetchUser()
    this.tutor = { ...this.getTutor() }
    this.user = { ...this.getUser() }
    this.src = this.user.profilePic
  },
  methods: {
    ...mapActions(['fetchTutor', 'fetchUser', 'updateTutor', 'updateUser']),
    ...mapGetters(['getUser', 'getTutor']),

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
      const requiredFields = [
        'user.email',
        'user.firstName',
        'user.lastName',
        'tutor.gender',
        'tutor.occupation',
        'tutor.subjects',
        'tutor.whatYouTeach',
        'tutor.qualifications',
        'tutor.bio',
        'tutor.rates',
        'tutor.teachExp',
        'tutor.profExp',
      ]
      requiredFields.forEach((field) => {
        if (this[field.split('.')[0]][field.split('.')[1]].length < 1) {
          this.errors[field] = 'This field is required'
        } else {
          this.errors[field] = ''
        }
      })

      const emailValidation =
        /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/i
      if (!emailValidation.test(this.user.email)) {
        this.errors.email = 'Invalid email'
      } else {
        this.errors.email = ''
      }

      if (
        this.tutor.paypalEmail.length > 0 &&
        !emailValidation.test(this.tutor.paypalEmail)
      ) {
        this.errors.paypalEmail = 'Invalid email'
      } else {
        this.errors.paypalEmail = ''
      }
    },
    async handleSubmit() {
      this.validateData()
      if (
        !this.checkErrors() &&
        (!objectsEqual(this.tutor, this.getTutor()) ||
          !objectsEqual(this.user, this.getUser()))
      ) {
        const csrfToken = await getCSRF()
        if (csrfToken.success !== null && csrfToken.success !== undefined) {
          const formData = new FormData()
          if (this.profilePic) {
            formData.append('profile_pic', this.profilePic[0])
          }
          formData.append(
            'tutor',
            JSON.stringify(keysToSnake(unpackTutor({ ...this.tutor })))
          )
          formData.append(
            'user',
            JSON.stringify(keysToSnake(unpackUser({ ...this.user })))
          )
          const data = await fetch('/api/auth/update-tutor/', {
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
            if (!objectsEqual(this.tutor, this.getTutor())) {
              this.updateTutor({ ...this.tutor })
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