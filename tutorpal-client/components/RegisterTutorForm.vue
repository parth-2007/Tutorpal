<template>
  <div>
    <form id="registerform" style="font-family: Poppins">
      <div class="div-block-7-copy">
        <h1 class="heading-4">Account Info</h1>
        <h1 class="heading-4-copy">Account Info</h1>
        <div class="text-block-4">
          This is all of your account information. Use this to keep track of all
          your information, to login, etc. Keep in mind that this can be changed
          later.
        </div>
        <div class="columns-2 w-row">
          <div class="column w-col w-col-6">
            <div class="text-block-5">Full Name</div>
          </div>
          <div style="width: 50%" class="row">
            <div class="col">
              <label for="firstname" class="form-label">First Name</label>
              <input
                v-model="firstName"
                type="text"
                class="form-control"
                id="firstname"
                aria-label="First name"
                maxlength="200"
                required
              />
              <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.firstName }}</p>
            </div>
            <div style="padding-left: 0px" class="col">
              <label for="lastname" class="form-label">Last Name</label>
              <input
                v-model="lastName"
                type="text"
                class="form-control"
                id="lastname"
                aria-label="Last name"
                required
                maxlength="200"
              />
              <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.lastName }}</p>
            </div>
          </div>
        </div>
        <div class="columns-2-copy w-row">
          <div class="column w-col w-col-6">
            <div class="text-block-5">Password and confirmation</div>
          </div>
          <div style="width: 50%" class="row">
            <div class="col">
              <label for="password" class="form-label">Password</label>
              <input
                v-model="password"
                type="password"
                class="form-control"
                id="password"
                required
              />
              <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.password }}</p>
            </div>
            <div style="padding-left: 0px" class="col">
              <label for="confirmpassword" class="form-label"
                >Confirm Password</label
              >
              <input
                v-model="confirmPassword"
                type="password"
                class="form-control"
                id="confirmpassword"
                required
              />
              <p style="color: hsla(0, 100%, 64%, 1)">
                {{ errors.confirmPassword }}
              </p>
            </div>
          </div>
        </div>
        <div class="columns-2-copy w-row">
          <div class="column w-col w-col-6">
            <div class="text-block-5">Email Address</div>
          </div>
          <div class="w-col w-col-6">
            <div style="margin-top: 15px" class="mb-3">
              <label for="emailaddress" class="form-label">Email Address</label>
              <input
                v-model="email"
                type="email"
                class="form-control"
                id="emailaddress"
                maxlength="200"
                required
              />
              <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.email }}</p>
            </div>
          </div>
        </div>
        <div class="columns-2-copy w-row">
          <div class="column w-col w-col-6">
            <div class="text-block-5">
              PayPal Email Address (Put the email address you would like to
              accept payments from. This is a crucial part of being a tutor on our platform unless you are a volunteer tutor. If left blank, this will be set to your
              default email address. If you are underage, you can use your parent's paypal email instead. )
            </div>
          </div>
          <div class="w-col w-col-6">
            <div style="margin-top: 15px" class="mb-3">
              <label for="paypalemail" class="form-label"
                >PayPal Email Address</label
              >
              <input
                v-model="paypalEmail"
                type="email"
                class="form-control"
                id="paypalemail"
                maxlength="200"
                required
              />
              <p style="color: hsla(0, 100%, 64%, 1)">
                {{ errors.paypalEmail }}
              </p>
            </div>
          </div>
        </div>
      </div>
      <div class="columns-2-copy w-row">
        <div style="margin-left: 60px" class="column w-col w-col-6">
          <div class="text-block-5">Birthdate</div>
        </div>
        <div style="margin-right: 60px" class="w-col w-col-6">
          <div class="form-group row">
            <label for="birthdate" class="col-2 col-form-label"
              >Birthdate</label
            >
            <div class="col-10">
              <input
                v-model="birthDate"
                class="form-control"
                type="date"
                id="birthdate"
                required
              />
              <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.birthDate }}</p>
            </div>
          </div>
        </div>
      </div>
      <div class="columns-2-copy w-row">
        <div class="column w-col w-col-6">
          <div style="margin-left: 60px" class="text-block-5">Gender</div>
        </div>
        <div style="margin-right: 0px" class="w-col w-col-6">
          <select
            v-model="gender"
            style="margin-top: 15px; width: 92%"
            class="form-select"
            id="gender"
            aria-label="Default select example"
          >
            <option value="Male" selected="selected">Male</option>
            <option value="Female">Female</option>
            <option value="Other">Other</option>
            <option value="Prefer Not To Say">Prefer Not To Say</option>
          </select>
          <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.gender }}</p>
        </div>
      </div>
      <div class="div-block-7">
        <h1 class="heading-4-copy">Professional Info</h1>
        <div class="text-block-4">
          Tell us a bit about yourself. This information will appear on your
          public profile, so that potential students can get to know you better.
        </div>
        <div class="columns-2 w-row">
          <div class="column w-col w-col-6">
            <div class="text-block-5">
              Occupation (If unemployed or in school, please type "none")
            </div>
          </div>
          <div class="w-col w-col-6">
            <div style="margin-top: 15px" class="mb-3">
              <input
                v-model="occupation"
                class="form-control"
                id="occupation"
                required
                maxlength="200"
              />
              <p style="color: hsla(0, 100%, 64%, 1)">
                {{ errors.occupation }}
              </p>
            </div>
          </div>
        </div>
        <div class="columns-2-copy w-row">
          <div class="column w-col w-col-6">
            <div class="text-block-5">
              Subject(s) (multiple subjects are valid eg. Physics - Mathematics)
            </div>
          </div>
          <div class="w-col w-col-6">
            <div style="margin-top: 15px" class="mb-3">
              <input
                v-model="subjects"
                class="form-control"
                id="subjects"
                maxlength="200"
                required
              />
              <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.subjects }}</p>
            </div>
          </div>
        </div>
      </div>
      <div class="columns-2-copy w-row">
        <div class="column w-col w-col-6">
          <div style="margin-left: 60px" class="text-block-5">
            Class Curriculum (please be as detailed as possible)
          </div>
        </div>
        <div class="w-col w-col-6">
          <textarea
            v-model="whatYouTeach"
            style="height: 250px"
            class="form-control"
            id="description"
            rows="3"
            maxlength="3000"
          ></textarea>
          <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.whatYouTeach }}</p>
        </div>
      </div>
      <div class="columns-2-copy w-row">
        <div class="column w-col w-col-6">
          <div style="margin-left: 60px" class="text-block-5">
            Qualifications (eg. awards, accomplishments, achievements)
          </div>
        </div>
        <div class="w-col w-col-6">
          <div class="row">
            <div class="col">
              <label for="major" class="form-label">Major (leave blank if none)</label>
              <input
                v-model="major"
                type="text"
                class="form-control"
                maxlength="200"
                id="major"
                required
              />
              <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.major }}</p>
            </div>
            <div style="padding-left: 0px" class="col">
              <label for="gpa" class="form-label">GPA</label>
              <input
                v-model="gpa"
                type="number"
                id="gpa"
                min="0"
                max="6"
                class="form-control"
              />
              <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.gpa }}</p>
            </div>
            <div style="padding-left: 0px" class="col">
              <label for="education" class="form-label">Education</label>
              <select
                v-model="education"
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
              <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.education }}</p>
            </div>
            <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.linkedIn }}</p>
            <div style="padding-left: 0px" class="col">
              <label for="school" class="form-label">School/College</label>
              <input
                v-model="school"
                type="text"
                class="form-control"
                id="school"
                maxlength="200"
                required
              />
              <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.school }}</p>
            </div>
          </div>
          <textarea
            v-model="qualifications"
            style="height: 250px; margin-top: 25px"
            class="form-control"
            id="t_education"
            rows="3"
            maxlength="3000"
          ></textarea>
          <p style="color: hsla(0, 100%, 64%, 1)">
            {{ errors.qualifications }}
          </p>
        </div>
      </div>
      <div class="columns-2-copy w-row">
        <div class="column w-col w-col-6">
          <div style="margin-left: 60px" class="text-block-5">
            Linkedin Profile Link(optional)
          </div>
        </div>
        <div class="w-col w-col-6">
          <input
            v-model="linkedIn"
            class="form-control"
            id="linkedin"
            placeholder="linkedin.com/in/johndoe"
            maxlength="200"
          />
          <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.linkedIn }}</p>
        </div>
      </div>
      <div class="columns-2-copy w-row">
        <div class="column w-col w-col-6">
          <div style="margin-left: 60px" class="text-block-5">
            Tell us a bit about yourself
          </div>
        </div>
        <div class="w-col w-col-6">
          <div class="row">
            <div class="col">
              <textarea
                v-model="bio"
                style="height: 250px; margin-top: 25px"
                class="form-control"
                id="bio"
                placeholder="eg. my hobbies are..."
                rows="3"
                maxlength="2000"
              ></textarea>
              <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.bio }}</p>
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

                <p style="color: hsla(0, 100%, 64%, 1)">
                  {{ errors.profilePic }}
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
        </div>
      </div>
      <div class="columns-2-copy w-row">
        <div class="column w-col w-col-6">
          <div style="margin-left: 60px" class="text-block-5">
            Pricing Per Hour (in terms of USD) <br>(to claim volunteer hours you MUST set this value to 0)
          </div>
        </div>
        <div class="w-col w-col-6">
          <label for="number" class="form-label">Pricing</label>
          <input
            v-model="rates"
            type="number"
            id="pricing"
            min="0"
            max="1000"
            class="form-control"
          />
          <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.rates }}</p>
        </div>
      </div>
      <div class="columns-2-copy w-row">
        <div class="column w-col w-col-6">
          <div style="margin-left: 60px" class="text-block-5">Experience</div>
        </div>
        <div class="w-col w-col-6">
          <div class="row">
            <div class="col">
              <label for="teachexp" class="form-label"
                >Years of Teaching Experience</label
              >
              <input
                v-model="teachExp"
                type="number"
                id="teachexp"
                min="0"
                max="50"
                class="form-control"
              />
              <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.teachExp }}</p>
            </div>
            <div style="padding-left: 0px" class="col">
              <label for="profexp" class="form-label"
                >Years of Professional Experience</label
              >
              <input
                v-model="profExp"
                id="profexp"
                type="number"
                min="0"
                max="50"
                class="form-control"
              />
              <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.profExp }}</p>
            </div>
          </div>
        </div>
      </div>
      <div class="columns-2-copy w-row">
        <div class="column w-col w-col-6">
          <div style="margin-left: 60px" class="text-block-5">
            Availability
          </div>
        </div>
        <div class="w-col w-col-6">
          <input
            v-model="availability"
            class="form-control"
            id="availability"
            maxlength="200"
            placeholder="Mondays, 4:00 PM - 6:00 PM"
          />
          <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.availability }}</p>
        </div>
      </div>
      <div class="columns-2-copy w-row">
        <div class="column w-col w-col-6">
          <div style="margin-left: 60px" class="text-block-5">
            Agree to legal terms
          </div>
        </div>
        <div class="w-col w-col-6">
          <div style="margin-top: 15px; margin-bottom: 15px" class="form-check">
            <input
              v-model="toc"
              class="form-check-input"
              nam="checkbox"
              type="checkbox"
              id="toc"
              required
            />
            <label class="form-check-label" for="toc">
              I have read and agree with TutorPal's
              <router-link to="/toc">Terms of Service</router-link> and will not
              hold them liable for personal losses. I also acknowldge that
              TutorPal takes a 5% fee of the payments I receive.
            </label>
            <p style="color: hsla(0, 100%, 64%, 1)">{{ errors.toc }}</p>
          </div>
        </div>
      </div>
    </form>
    <p style="color: hsla(0, 100%, 64%, 1); font-family: Poppins; font-size: 16px; margin-left: 60px;">{{ errors.global }}</p>
    <p style="margin-top: 10px; font-family: Poppins; font-size: 16px; margin-left: 60px; color: #008000;">{{success}}</p>
    <button
      @click="handleSubmit"
      style="margin-top: 40px; margin-bottom: 20px; margin-left: 60px"
      class="btn btn-primary"
    >
      Register
    </button>
  </div>
</template>
<script>
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
      paypalEmail: '',
      birthDate: '',
      gender: '',
      occupation: '',
      subjects: '',
      whatYouTeach: '',
      major: '',
      gpa: 0,
      education: '',
      school: '',
      qualifications: '',
      linkedIn: '',
      bio: '',
      rates: 0,
      teachExp: 0,
      profExp: 0,
      availability: '',
      errors: {
        toc: '',
        email: '',
        firstName: '',
        lastName: '',
        password: '',
        confirmPassword: '',
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
      success: "",
      src: 'https://image.flaticon.com/icons/png/512/149/149071.png',
    }
  },
  head() {
    return {
      title: 'Tutor Registration',
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
      ],
    }
  },
  methods: {
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
        let counter = 0
        if (!this.toc) {
          this.errors.toc = 'Please read and agree to our Terms of Conditions'
        } else {
          this.errors.toc = ''
          counter+=1
        }
        if (this.linkedIn !== '') {
          let httpCheck = this.linkedIn.substr(0, 8)
          if (httpCheck !== 'https://') {
            httpCheck = 'https://'
            this.linkedIn = httpCheck.concat(this.linkedIn)
          }
        }

        const birthday = new Date(this.birthDate)
        const age = Math.floor((Date.now() - birthday) / 31557600000)
        if(age<0){
          this.errors.birthDate = "Hmmm...our data shows us you haven't been born yet"
        }
        else if(age>70){
          this.errors.birthDate = "Sorry but our platform doesn't accept tutors above the age of 70 for technical reasons. If you like, you can contact our support team: info@tutorpal.org"
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

        const requiredFields = [
          'email',
          'firstName',
          'lastName',
          'gender',
          'subjects',
          'education',
          'school',
          'rates',
          'password',
        ]

        requiredFields.forEach((field) => {
          if (this[field].length < 1) {
            this.errors[field] = 'This field is required'
          } else {
            this.errors[field] = ''
            counter+=1
          }
        })

        if(this.gpa>6 || this.gpa<0){
          this.errors.gpa = "Our site is only allowing for GPAS on the 4.0, 5.0, and 6.0 scale. Anything higher than that or lower than 0 is not accepted."
        }
        else{
          counter+=1
        }
        
        if(parseInt(this.rates)>1000 || parseInt(this.rates)<0){
          this.errors.rates="We are not accepting negative fees or fees higher than $1000 per hour"
        }
        else{
          counter+=1
        }

        const emailValidation =
          /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/i
        if (!emailValidation.test(this.email)) {
          this.errors.email = 'Invalid email'
        } else {
          this.errors.email = '';
          counter+=1
        }
        if (
          this.paypalEmail.length > 0 &&
          !emailValidation.test(this.paypalEmail)
        ) {
          this.errors.paypalEmail = 'Invalid email'
        } else {
          this.errors.paypalEmail = ''
          this.paypalEmail = this.email;
          counter+=1
        }

        if (this.password !== this.confirmPassword) {
          this.errors.password =
            'Password and Confirm Password must be the same'
          this.errors.confirmPassword =
            'Password and Confirm Password must be the same'
        }
        else if(this.password.length===0){
          this.errors.password="This field is required"
          this.errors.confirmPassword="This field is required"
        }
        else {
          this.errors.password = ''
          this.errors.confirmPassword = ''
          counter+=1
        }
        
        if(parseInt(this.profExp) < 0 || parseInt(this.profExp) > 50){
          this.errors.profExp="Sorry but we aren't allowing for more than 50 or negative years in professional experience"
        }
        else{
          this.errors.profExp=""
          counter+=1
        }

        if(parseInt(this.teachExp) < 0 || parseInt(this.teachExp) > 50){
          this.errors.teachExp="Sorry but we aren't allowing for more than 50 or negative years in teaching experience"
        }
        else{
          this.errors.teachExp=""
          counter+=1
        }
      
        if (counter!==18){
          this.errors.global = "There seems to be a problem with your request, scroll up to see whats wrong."
          this.success = ""
        }
        else if(counter===18){
          this.errors.global = ''
        }
        console.log(this.gpa, this.teachExp, this.profExp)
    },
    async handleSubmit() {
      this.validateData()
      if (!this.checkErrors()) {
        // eslint-disable-next-line
        console.log('sending data...')
        const formData = new FormData()
        const user = {
          email: this.email,
          password: this.password,
          first_name: this.firstName,
          last_name: this.lastName,
        }
        if (this.profilePic) {
          // eslint-disable-next-line
          formData.append('profile_pic', this.profilePic[0])
        }
        formData.append('user', JSON.stringify(user))
        const tutor = {
          paypal_email: this.paypalEmail,
          birth_date: this.birthDate,
          gender: this.gender,
          occupation: this.occupation,
          subjects: this.subjects,
          what_you_teach: this.whatYouTeach,
          major: this.major,
          gpa: this.gpa,
          education: this.education,
          school: this.school,
          qualifications: this.qualifications,
          linkedIn: this.linkedIn,
          bio: this.bio,
          rates: this.rates,
          teach_exp: this.teachExp,
          prof_exp: this.profExp,
          availability: this.availability,
        }
        if (this.linkedIn.length > 0) {
          tutor.linkedIn = this.linkedIn
        }
        formData.append('tutor', JSON.stringify(tutor))
        const data = await fetch(
          process.env.API_URL + '/auth/register-tutor/',
          {
            credentials: 'include',
            method: 'POST',
            headers: {
              'X-CSRFToken': getCSRF(),
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
        }
        if (data && data.success === 'Successfully created tutor') {
          this.success = "You have successfully created a tutor account!"
          this.$router.push('/checkemail')
        }
      }
      else{
        this.errors.global = "There seems to be a problem with your request, scroll up to see whats wrong."
        this.success = ""
      }
    },
  },
}
</script>