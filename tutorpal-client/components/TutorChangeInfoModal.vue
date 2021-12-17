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
          maxlength="200"
          required
        />
      </div>
      <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.email }}</p>
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
      <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.paypalEmail }}</p>
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
      <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.birthDate }}</p>
      <div class="mb-3">
        <label for="birthdate" class="form-label">Gender</label>
        <select
          v-model="tutor.gender"
          class="form-select"
          id="gender"
          aria-label="Default select example"
        >
          <option value="Male">Male</option>
          <option value="Female">Female</option>
          <option value="Other">Other</option>
          <option value="Prefer Not To Say">Prefer Not To Say</option>
        </select>
      </div>
      <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.gender }}</p>
      <div class="mb-3">
        <label for="firstname" class="form-label">First Name</label>
        <input
          v-model="user.firstName"
          class="form-control"
          id="firstname"
          maxlength="200"
          required
        />
      </div>
      <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.firstName }}</p>
      <div class="mb-3">
        <label for="lastname" class="form-label">Last Name</label>
        <input
          v-model="user.lastName"
          class="form-control"
          id="lastname"
          maxlength="200"
          required
        />
      </div>
      <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.lastName }}</p>
      <div class="mb-3">
        <label for="occupation" class="form-label">Occupation</label>
        <input
          v-model="tutor.occupation"
          class="form-control"
          id="occupation"
          maxlength="200"
          required
        />
      </div>
      <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.occupation }}</p>
      <div class="mb-3">
        <label for="subject" class="form-label">Subjects</label>
        <input
          v-model="tutor.subjects"
          class="form-control"
          id="subject"
          maxlength="200"
          required
        />
      </div>
      <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.subjects }}</p>
      <div class="text-block-5"><b>Class Description (Curriculum)</b></div>
      <textarea
        v-model="tutor.whatYouTeach"
        style="height: 250px"
        class="form-control"
        id="description"
        rows="3"
        maxlength="3000"
      ></textarea>
      <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.whatYouTeach }}</p>
      <div style="margin-top: 15px" class="row">
        <div class="col">
          <label for="major" class="form-label">Major</label>
          <input
            v-model="tutor.major"
            type="text"
            class="form-control"
            id="major"
            maxlength="200"
            required
          />
        </div>
        <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.major }}</p>
        <div style="padding-left: 0px; margin-left: 15px;" class="col">
          <label for="gpa" class="form-label">GPA</label>
          <input
            v-model="tutor.gpa"
            type="number"
            id="gpa"
            min="0"
            max="6"
            class="form-control"
          />
        </div>
        <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.gpa }}</p>
        <div style="padding-left: 0px; margin-left: 15px;" class="col">
          <label for="education" class="form-label">Education</label>
          <select
            v-model="tutor.education"
            style="margin-top: 0px"
            class="form-select"
            id="education"
            aria-label="Default select example"
          >
            <option value="High School">High School</option>
            <option value="Bachelors Degree">Bachelors Degree</option>
            <option value="Masters Degree">Masters Degree</option>
            <option value="Ph.D.">Ph.D.</option>
          </select>
        </div>
        <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.education }}</p>
        <div style="padding-left: 0px; margin-left: 15px;" class="col">
          <label for="school" class="form-label">School/College</label>
          <input
            v-model="tutor.school"
            type="text"
            class="form-control"
            id="school"
            maxlength="200"
            required
          />
        </div>
        <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.school }}</p>
      </div>
      <strong>Qualifications</strong>
      <textarea
        v-model="tutor.qualifications"
        style="height: 250px; margin-top: 10px"
        class="form-control"
        placeholder="Qualifications"
        id="educationdescription"
        rows="3"
        maxlength="3000"
      ></textarea>
      <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.qualifications }}</p>
      <div style="margin-top: 15px; margin-bottom: 5px" class="text-block-5">
        <b>Linkedin Profile Link(Optional)</b>
      </div>
      <input
        v-model="tutor.linkedIn"
        class="form-control"
        id="linkedin"
        maxlength="200"
        placeholder="https://www.linkedin.com/in/johndoe"
      />
      <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.linkedIn }}</p>
      <strong style="padding-top: 25px;">Tell us a bit about yourself</strong>
      <div class="row">
        <div class="col">
          <textarea
            v-model="tutor.bio"
            style="height: 250px; margin-top: 10px"
            class="form-control"
            id="bio"
            placeholder="Eg. My hobbies are..."
            rows="3"
            maxlength="2000"
          ></textarea>
        </div>
        <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.bio }}</p>
        <div style="padding-left: 0px" class="col">
          <div style="position: relative; text-align: center" class="col">
            <p>
              <input
                type="file"
                accept="image/+"
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
        <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.profilePic }}</p>
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
      <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.rates }}</p>
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
            max="50"
            class="form-control"
          />
        </div>
        <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.teachExp }}</p>
        <div style="padding-left: 0px; margin-left: 15px;" class="col">
          <label for="profexp" class="form-label"
            >Years of Professional Experience</label
          >
          <input
            v-model="tutor.profExp"
            id="profexp"
            type="number"
            min="0"
            max="50"
            class="form-control"
          />
        </div>
      </div>
      <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.profExp }}</p>
      <label style="margin-top: 15px" for="availability" class="form-label"
        >Availability</label
      >
      <input
        v-model="tutor.availability"
        class="form-control"
        id="availability"
        maxlength="200"
        placeholder="Mondays, 4:00 PM - 6:00 PM"
      />
      <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.availability }}</p>
    </form>
    <button
      @click="handleSubmit()"
      style="margin-top: 15px; font-family: Poppins; margin-left: 0px"
      class="btn btn-primary"
    >
      Update Profile
    </button>
    <p style="margin-top: 10px; color: hsla(0, 100%, 64%, 1)">{{errors.global}}</p>
    <p style="margin-top: 10px; color: #008000;">{{success}}</p>
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
      success: '',
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
      if (e.target.files[0].size > 5000000) {
        this.errors.profilePic =
          'File size is too high! Please upload a file less than 5 Megabytes'
        this.errors.global = "There seems to be a problem with your request, scroll up to see whats wrong."
      } else {
        this.errors.profilePic = ''
        this.errors.global='';
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
        'tutor.subjects',
        'tutor.rates',
        'tutor.gpa',
        'tutor.school',
        'tutor.education'
      ]
      let counter = 0
      requiredFields.forEach((field) => {
        if (this[field.split('.')[0]][field.split('.')[1]].length < 1) {
          this.errors[field] = 'This field is required'
        } else {
          this.errors[field] = ''
          counter+=1
        }
      })
      this.errors.email = this.errors['user.email']
      this.errors.firstName = this.errors['user.firstName']
      this.errors.lastName = this.errors['user.lastName']
      this.errors.gender = this.errors['tutor.gender']
      this.errors.subjects = this.errors['tutor.subjects']
      this.errors.rates = this.errors['tutor.rates']
      this.errors.gpa = this.errors['tutor.gpa']
      this.errors.school = this.errors['tutor.school']
      this.errors.education = this.errors['tutor.education']
      const emailValidation =
        /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/i
      if (!emailValidation.test(this.user.email)) {
        this.errors.email = 'Invalid email'
      } else {
        this.errors.email = ''
        counter+=1
      }
      if (
        this.tutor.paypalEmail.length > 0 &&
        !emailValidation.test(this.tutor.paypalEmail)
      ) {
        this.errors.paypalEmail = 'Invalid email'
      } else {
        this.errors.paypalEmail = ''
        counter+=1
      }
      const birthday = new Date(this.tutor.birthDate)
      const age = Math.floor((Date.now() - birthday) / 31557600000)
      /* eslint-disable */
      if(age<0){
        this.errors.birthDate = "Hmmm...our data shows us you haven't been born yet"
      }
      else if(age>70){
        this.errors.birthDate = "Sorry but our platform doesn't accept tutors above the age of 70 for technical reasons. If you like, you can contact our support team: info@tutorpal.org"
      }
      else if(age<15){
        this.errors.birthDate = "You must be at least 15 years old to register as a tutor."
      }
      else {
        counter+=1
        this.errors.birthDate = ""
      }

      if(this.tutor.gpa>6 || this.tutor.gpa<0){
        this.errors.gpa = "Our site is only allowing for GPAS on the 4.0, 5.0, and 6.0 scale. Anything higher than that or lower than 0 is not accepted."
      }
      else{
        counter+=1
      }
      
      if(parseInt(this.tutor.rates)>1000 || parseInt(this.tutor.rates)<0){
        this.errors.rates="We are not accepting negative fees or fees higher than $1000 per hour"
      }
      else{
        counter+=1
      }

      if (counter!==14){
        this.errors.global = "There seems to be a problem with your request, scroll up to see whats wrong."
        this.success = ""
      }
      else if(counter===14){
        this.success = "You have successfully updated your account info!"
        this.errors.global = ''
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
        if (this.tutor.linkedIn !== '') {
          let httpCheck = this.tutor.linkedIn.substr(0, 8)
          if (httpCheck !== 'https://') {
            httpCheck = 'https://'
            this.tutor.linkedIn = httpCheck.concat(this.tutor.linkedIn)
          }
        }
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
          const data = await fetch(
            process.env.API_URL + '/auth/update-tutor/',
            {
              credentials: 'include',
              method: 'PATCH',
              headers: {
                'X-CSRFToken': csrfToken.success,
              },
              body: formData,
            }
          )
            .then((res) => {
              if (res.status >= 400 && res.status < 600) {
                this.errors.global = "There seems to be a problem with your request, scroll up to see whats wrong."
                this.success = ""
              }
              else if(res.status ===200){
                this.success = "You have successfully updated your account info!"
                this.errors.global = ''
              }
              return res.json()
            })
            .catch(() => {
              this.errors.global = "There seems to be a problem with your request, scroll up to see whats wrong."
              this.success = ""
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
          }
        } else {
          this.errors.global = 'Something went wrong :('
        }
      }
    },
  },
}
</script>