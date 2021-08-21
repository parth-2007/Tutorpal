<template>
  <client-only>
    <html
      data-wf-page="5f600218af481481a99ffa6a"
      data-wf-site="5f600218af4814e3759ffa69"
    >
      <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="https://www.tutorpal.org/student/css/student-main.webflow.css" media="print" onload="this.media='all'">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" media="print" onload="this.media='all'">
      </head>
      <body>
        <div id="main">
          <div
            style="z-index: 25"
            :style="updatemodal"
            class="div-block-22-copy"
          >
            <div
              style="
                border-radius: 8px;
                padding-bottom: 20px;
                height: 85vh;
                overflow-y: auto;
              "
              class="div-block-23"
            >
              <div class="div-block-24">
                <img
                  @click="updatemodalvalue()"
                  src="../static/student/images/close-1.png"
                  width="20"
                  alt=""
                />
              </div>
              <h1 style="margin-top: 15px" class="heading-10">
                Schedule a Class
              </h1>
              <div class="div-block-25">
                <form id="form-wrapper" style="font-family: Poppins">
                  <div class="form-group row">
                    <p style="color: #008000; font-size: 16px">
                      {{ predictedprice }}
                    </p>
                    <label for="date-time" class="col-2 col-form-label"
                      >Date and Start Time</label
                    >
                    <div class="col-10">
                      <input
                        v-model="date_startTime"
                        class="form-control"
                        type="datetime-local"
                        id="date-time"
                        required
                      />
                    </div>
                    <label for="date-time" class="col-2 col-form-label"
                      >Duration in Minutes</label
                    >
                    <div class="col-10">
                      <input
                        @change="predictprice()"
                        v-model="duration"
                        type="number"
                        id="duration"
                        class="form-control"
                        required
                      />
                    </div>
                    <label for="date-time" class="col-2 col-form-label"
                      >Subject(specify the topic)</label
                    >
                    <div class="col-10">
                      <input v-model="subjects" class="form-control" required />
                    </div>
                  </div>
                  <textarea
                    v-model="description"
                    style="height: 250px; margin-top: 25px; margin-bottom: 15px"
                    class="form-control"
                    id="classdescription"
                    placeholder="Describe what you want to learn, cover, or what you need help with."
                    rows="3"
                    required
                  ></textarea>
                  <div
                    style="margin-top: 15px; margin-bottom: 15px"
                    class="form-check"
                  >
                    <input
                      @click="trial()"
                      class="form-check-input"
                      nam="checkbox"
                      type="checkbox"
                      id="trial"
                    />
                    <label class="form-check-label" for="trial">
                      I want this class to be a trial class
                    </label>
                  </div>
                </form>
                <button
                  @click="addSessionHandler"
                  class="btn btn-primary"
                  name="session"
                >
                  Send request
                </button>
              </div>
            </div>
          </div>
          <div class="div-block-55">
            <div class="section">
              <router-link to="/" class="link-block-3 w-inline-block"
                ><img
                  src="../static/student/images/logo.jpg"
                  loading="lazy"
                  width="200"
                  srcset="
                    ../static/student/images/logo.jpg  500w,
                    ../static/student/images/logo.jpg  800w,
                    ../static/student/images/logo.jpg 1080w,
                    ../static/student/images/logo.jpg 1432w
                  "
                  sizes="200px"
                  alt=""
              /></router-link>
              <div class="div-block-4">
                <form action="/search" class="stuff w-form">
                  <img
                    src="../static/student/images/search-1.png"
                    loading="lazy"
                    width="25"
                    height="25"
                    srcset="
                      ../static/student/images/search-1-p-500.png 500w,
                      ../static/student/images/search-1.png       512w
                    "
                    sizes="(max-width: 767px) 20px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw"
                    alt=""
                    class="image-2"
                  /><input
                    type="search"
                    class="search-3 w-input"
                    maxlength="256"
                    name="q"
                    placeholder="Search by subject"
                    id="search"
                    required=""
                  /><input
                    type="submit"
                    value="Search"
                    class="button-8 _100 _5px-left w-button"
                  />
                </form>
                <div class="div-block-43">
                  <div class="name_profile_pic">
                    <img
                      :src="user.profilePic"
                      width="60"
                      height="60"
                      sizes="(max-width: 479px) 15vw, (max-width: 767px) 8vw, 60px"
                      alt=""
                      class="image-7"
                    />
                    <div>
                      <div
                        @click="logoutclick()"
                        class="dropdown-toggle-2-copy w-dropdown-toggle"
                      >
                        <div id="name" class="text-block-18">
                          {{ user.firstName }} {{ user.lastName }}
                        </div>
                        <div class="text-block-20">Student</div>
                      </div>
                      <nav :style="logout" class="navigation-dropdown-2">
                        <div class="dropdown-pointer-2">
                          <div class="dropdown-wrapper-2">
                            <router-link
                              to="/logout"
                              id="logout"
                              class="dropdown-link-2 w-inline-block"
                            >
                              <div class="nav-content-wrap-2">
                                <div class="dropdown-title-2">Logout</div>
                              </div>
                            </router-link>
                            <router-link
                              to="/account"
                              class="dropdown-link-2 w-inline-block"
                            >
                              <div class="nav-content-wrap-2">
                                <div class="dropdown-title-2">Account</div>
                              </div>
                            </router-link>
                          </div>
                        </div>
                      </nav>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="div-block-6">
              <div
                data-collapse="none"
                data-animation="default"
                data-duration="400"
                role="banner"
                class="navbar-2 w-nav"
              >
                <div class="container-2 w-container">
                  <nav role="navigation" class="nav-menu-3 w-nav-menu">
                    <router-link
                      to="/"
                      aria-current="page"
                      class="nav-link-4 w-nav-link"
                      >Explore</router-link
                    ><router-link to="/inbox" class="nav-link-4 w-nav-link"
                      >Messages<span class="badge">{{
                        user.unread
                      }}</span></router-link
                    ><router-link to="/requests" class="nav-link-4 w-nav-link"
                      >Requests</router-link
                    ><router-link to="/payments" class="nav-link-4 w-nav-link"
                      >Payments</router-link
                    >
                  </nav>
                  <div class="menu-button-2 w-nav-button">
                    <div class="icon-2 w-icon-nav-menu"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="div-block-70">
            <div class="div-block-71">
              <img
                :src="data.user !== undefined ? data.user.profile_pic : ''"
                loading="lazy"
                width="74"
                height="74"
                sizes="74px"
                alt=""
              />
              <div class="div-block-72">
                <h1 class="heading-3" id="subjects">{{ data.subjects }}</h1>
                <div class="div-block-68">
                  <div class="text-block-32">
                    <strong id="fullname" class="bold-text-8"
                      >{{
                        data.user !== undefined ? data.user.first_name : ''
                      }}
                      {{
                        data.user !== undefined ? data.user.last_name : ''
                      }}</strong
                    >
                  </div>
                </div>
              </div>
            </div>
            <p style="padding-top: 20px" class="paragraph-8">
              <strong>Degree: </strong>{{ data.education }}<br /><strong
                >Birthdate: </strong
              >{{ data.birth_date }}<br /><strong
                >Qualification Description: </strong
              >{{ data.qualifications }}<br />
              <strong>Education: </strong>{{ data.major }} at {{ data.school }},
              GPA of {{ data.gpa }}<br /><strong
                >Professional Experience: </strong
              >{{ data.prof_exp }} years<br /><strong
                >Teaching Experience: </strong
              >{{ data.teach_exp }} years<br />
              <strong>Average Review:</strong>
              {{ data.average_reviews }} Stars<br /><strong>Occupation: </strong
              >{{ data.occupation }}<br /><strong>Gender: </strong
              >{{ data.gender }}<br />
              <strong>Price: </strong>${{ data.rates }} hourly <br /><strong
                >Bio: </strong
              >{{ data.bio }}<br /><strong>Course Description: </strong
              >{{ data.what_you_teach }}<br /><strong>Availability: </strong
              >{{ data.availability }} <br /><a
                style="font-family: Poppins"
                :href="data.linkedIn"
                target="_blank"
                ><strong>Linkedin Account:</strong></a
              >
            </p>
            <a @click="updatemodalvalue()" class="button-9 w-button"
              >Schedule a class</a
            >
            <a
              href="/inbox"
              style="margin-left: 20px; cursor: pointer"
              @click="createroom()"
              class="button-9 w-buttion"
              >Send a message</a
            >
          </div>
          <div class="div-block-56">
            <h1 class="heading-11">Reviews</h1>
            <div v-for="review in reviews.results" :key="review.id" id="posts">
              <div class="review_bundle">
                <div class="review_item">
                  <img
                    :src="review.student.user.profile_pic"
                    loading="lazy"
                    width="40"
                    sizes="40px"
                    alt=""
                    class="image-12"
                  />
                  <div class="text-block-33">
                    {{ review.student.user.first_name }}
                    {{ review.student.user.last_name }}
                  </div>
                  <div class="text-block-34">
                    Review: <strong>{{ review.stars }} Stars</strong>
                  </div>
                </div>
                <p class="paragraph-9">{{ review.description }}</p>
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
import { add, str } from 'timelite/time'
import getCSRF from '../utils/getCSRF'
export default {
  data() {
    return {
      clicked: false,
      clicked1: false,
      url: '',
      data: [],
      date_startTime: '',
      duration: '',
      description: '',
      free: false,
      subjects: '',
      reviews: [],
      predictedprice: '',
    }
  },
  async fetch() {
    this.url = 'https://api.tutorpal.org/tutors/' + this.$route.params.id + '/'
    this.data = await fetch(this.url, {
      credentials: 'include',
    }).then((res) => res.json())
    await this.fetchUser()
  },
  head() {
    return {
      title: 'Tutor Profile',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/main/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/main/css/normalize.css" },
      ]
    }
  },
  computed: {
    updatemodal() {
      return {
        display: this.clicked ? 'flex' : 'none',
      }
    },
    logout() {
      return {
        display: this.clicked1 ? 'flex' : 'none',
      }
    },
    ...mapGetters({ user: 'getUser', pendingOnTutor: 'getPendingOnTutor' }),
  },
  async created() {
    const url =
      'https://api.tutorpal.org/tutors/' + this.$route.params.id + '/reviews/'
    this.reviews = await fetch(url, {
      credentials: 'include',
    }).then((res) => res.json())
    await this.fetchSessions('pendingOnTutor')
  },
  methods: {
    ...mapGetters(['getUser', 'getPendingOnTutor']),
    ...mapActions(['fetchUser', 'addSession', 'fetchSessions']),
    updatemodalvalue() {
      this.clicked = !this.clicked
    },
    logoutclick() {
      this.clicked1 = !this.clicked1
    },
    trial() {
      this.free = !this.free
      this.predictedprice = 'Predicted Class Amount: $0.00'
    },
    predictprice() {
      this.predictedprice =
        'Predicted Class Amount: $' +
        Math.floor((this.data.rates / 60) * parseInt(this.duration) * 100) / 100
    },
    async createroom() {
      const room = {
        tutor_pk: parseInt(this.$route.params.id),
        student_pk: parseInt(this.user.studentPk),
        tutor: parseInt(this.$route.params.id),
        student: parseInt(this.user.studentPk),
      }
      const csrfToken = await getCSRF()
      await fetch('https://api.tutorpal.org/rooms/', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken.success,
        },
        body: JSON.stringify(room),
      })
    },
    async addSessionHandler() {
      const sessionDate = (this.date_startTime || '').substring(0, 10)
      const startTime = (this.date_startTime || '').substring(11, 18)
      const hours = parseInt(this.duration) / 60
      let rhours = Math.floor(hours)
      const minutes = (hours - rhours) * 60
      let rminutes = Math.round(minutes)
      if (rminutes < 10) {
        rminutes = '0' + rminutes
      }
      if (rhours < 10) {
        rhours = '0' + rhours
      }
      const sessionDuration = rhours + ':' + rminutes + ':00'
      const sessionPrice =
        Math.floor((this.data.rates / 60) * parseInt(this.duration) * 100) / 100
      let endTime = add([startTime, sessionDuration])
      endTime = str(endTime)
      endTime = endTime.substring(0, 5)
      const sessionData = {
        student_pk: this.user.studentPk,
        tutor: parseInt(this.$route.params.id),
        date: sessionDate,
        time_start: startTime,
        time_end: endTime,
        duration: sessionDuration,
        price: sessionPrice,
        free: this.free,
        description: this.description,
        call_url: '',
        subjects: this.subjects,
        accepted: false,
        rejected: false,
        started: false,
        finished: false,
        canceled: false,
        student_paid: false,
        tutor_paid: false,
        tutor_emailed: false,
        student_emailed: false,
        parent_emailed: false,
        accessable: false,
      }
      const csrfToken = await getCSRF()
      this.addSession([sessionData, 'pendingOnTutor'])
      await fetch('https://api.tutorpal.org/sessions/', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'X-CSRFToken': csrfToken.success,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(sessionData),
      }).then((res) => {
        if (res.status === 400) {
          this.predictedprice =
            'Oops! Something went wrong, please check your inputs again.'
        } else if (res.status === 500) {
          this.predictedprice =
            'There seems to be an internal error, we are working on the issue.'
        } else if (res.status === 201) {
          this.predictedprice =
            'Thank you for successfully creating a session. Good luck!'
          this.subjects = ''
          this.free = false
          this.description = ''
          this.duration = ''
          this.date_startTime = ''
        }
      })
    },
  },
}
</script>
<style>
.div-block-22-copy {
  position: fixed;
  z-index: 21;
  width: 100vw;
  display: none;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.3);
  -o-object-fit: contain;
  object-fit: contain;
}
.badge {
  position: absolute;
  top: 13px;
  right: 3px;
  padding: 4px 7px;
  border-radius: 1000px;
  background-color: red;
  color: white;
  font-family: Poppins;
  font-size: 12px;
}
</style>