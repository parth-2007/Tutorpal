<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <div v-if="session.student_paid === true && session.started === false">
        <p style="font-size: 18px; font-family: Poppins; margin: 15px">
          This class has not been started yet, your job as a tutor is to start
          meetings when the proper times and date occur.
        </p>
      </div>
      <div
        v-else-if="session.student_paid === false || session.finished === true"
      ></div>
      <div v-else-if="session.tutor_pk !== user.tutorPk"></div>
      <body
        v-else
        id="body"
        style="background-color: rgba(65, 168, 211, 0.2)"
        class="tutorbody-5"
      >
        <div
          :style="updateModal"
          style="padding-bottom: 0px"
          class="tutordiv-block-22"
        >
          <div
            style="
              border-radius: 8px;
              padding-bottom: 20px;
              height: 240px;
              width: 375px;
              font-family: Poppins;
            "
            class="tutordiv-block-23"
          >
            <div
              v-if="session.student_joined === true && this.buttonShow === true"
              class="tutordiv-block-25"
            >
              <strong
                >You have {{ dateToString(timerDisplay) }} left in this class,
                are you sure you want to end it?</strong
              >
              <br />Clicking "confirm" will confirm to us that this class has
              been finished. You will be paid shortly after. Thank you for
              tutoring with TutorPal!
              <button
                @click="endclass()"
                style="
                  background-color: green;
                  margin-left: 10px;
                  margin-top: 10px;
                  font-size: 14px;
                "
                class="tutorbutton-10-copy-copy w-button"
              >
                Confirm
              </button>
            </div>
            <div
              v-else-if="session.student_joined === false"
              style="margin-left: 10px; margin-top: 10px; margin-right: 10px"
            >
              Your student has not joined this class, therefore, we are not
              allowing you to end it. If there are any issues, please contact us
              at support@tutorpal.org. We are very sorry for the inconvienence.
            </div>
            <div
              v-else-if="this.buttonShow === false"
              style="margin-left: 10px; margin-top: 10px; margin-right: 10px"
            >
              You are only allowed to end this class during the last ten minutes
              of the meeting. We suggest continuing with the meeting until the
              last ten minutes. Thank you.
            </div>
            ><button
              @click="updateModalValue()"
              style="
                background-color: #bb0a1e;
                margin-left: 10px;
                margin-top: 10px;
                font-size: 14px;
              "
              class="tutorbutton-10-copy-copy w-button"
            >
              Cancel
            </button>
          </div>
        </div>
        <div id="main">
          <div class="tutorsection">
            <router-link to="/" class="tutorlink-block w-inline-block"
              ><img
                src="../static/tutor/images/logo.jpg"
                loading="lazy"
                width="260"
                srcset="
                  ../static/tutor/images/logo-p-500.jpeg   500w,
                  ../static/tutor/images/logo-p-800.jpeg   800w,
                  ../static/tutor/images/logo-p-1080.jpeg 1080w,
                  ../static/tutor/images/logo.jpg         1432w
                "
                sizes="(max-width: 479px) 100vw, (max-width: 767px) 34vw, (max-width: 991px) 25vw, (max-width: 1439px) 21vw, (max-width: 1919px) 15vw, 12vw"
                alt=""
            /></router-link>
            <div class="tutordiv-block-4">
              <div class="tutordiv-block-43">
                <div class="tutorname_profile_pic">
                  <img
                    :src="user.profilePic"
                    id="image"
                    width="60"
                    height="60"
                    sizes="60px"
                    alt=""
                    class="tutorimage-7"
                  />
                  <div
                    data-hover=""
                    data-delay="0"
                    class="tutordropdown-3 w-dropdown"
                  >
                    <div
                      @click="logoutclick()"
                      class="tutordropdown-toggle-2-copy w-dropdown-toggle"
                    >
                      <div id="name" class="tutortext-block-18">
                        {{ user.firstName }} {{ user.lastName }}
                      </div>
                      <div class="tutortext-block-20">Tutor</div>
                    </div>
                    <nav :style="logout" class="tutornavigation-dropdown-2">
                      <div class="tutordropdown-pointer-2">
                        <div class="tutordropdown-wrapper-2">
                          <router-link
                            to="/logout"
                            id="logout"
                            class="tutordropdown-link-2 w-inline-block"
                          >
                            <div class="tutornav-content-wrap-2">
                              <div class="tutordropdown-title-2">Logout</div>
                            </div>
                          </router-link>
                          <router-link
                            to="/account"
                            class="tutordropdown-link-2 w-inline-block"
                          >
                            <div class="tutornav-content-wrap-2">
                              <div class="tutordropdown-title-2">Account</div>
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
        </div>
        <div
          style="
            float: right;
            font-family: Poppins;
            background-color: white;
            height: 100%;
            width: 23vw;
            margin-top: 25px;
            margin-bottom: 25px;
            margin-right: 8px;
            border-radius: 8px;
            padding: 10px;
          "
        >
          <div>
            <p style="font-size: 16px">
              Here are some tools you can use to help:
            </p>
            <a target="_blank" href="https://www.google.com/docs/about/"
              >Google Docs, Sheets, Forms, Slides</a
            >
            <br />
            <a target="_blank" href="https://jamboard.google.com/"
              >Google Jamboard</a
            >
            <br />
            <a
              target="_blank"
              href="https://colab.research.google.com/notebooks/intro.ipynb"
              >Google Colab</a
            >
            <br />
            <a target="_blank" href="https://docs.google.com/drawings/"
              >Google Drawings</a
            >
            <br />
            <a target="_blank" href="https://kahoot.com/">Kahoot</a>
            <br />
            <a target="_blank" href="https://www.hackerrank.com/">Hackerrank</a>
            <p style="margin-top: 10px">
              Tips: 1) Leaving the call will NOT end this class as it is not
              directly connected to our platform. Remember to end the class by
              clicking the red button below. 2) Please do not need to share the
              meeting link with anybody, including the student. 3) The video
              calling system is most compatible with Google Chrome
            </p>
            <h1
              style="
                font-family: Poppins;
                margin-top: 10px;
                margin-bottom: 10px;
                font-size: 20px;
                color: black;
              "
            >
              <strong>Countdown Timer: {{ dateToString(timerDisplay) }}</strong>
            </h1>
            <button
              @click="updateModalValue()"
              class="tutorbutton-10-copy-copy w-button"
              style="
                margin-top: 10px;
                margin-bottom: 10px;
                background-color: #bb0a1e;
              "
            >
              End this Class
            </button>
          </div>
        </div>
        <iframe
          style="width: 75vw; height: 100vh"
          allow="camera;microphone"
          :src="'https://meet.jit.si/TutorpalSession' + session.call_url"
        ></iframe>
      </body>
    </html>
  </client-only>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'
import { sub, str } from 'timelite/time'
import getCSRF from '../utils/getCSRF'
import dateToString from '../utils/dateToString'

export default {
  data() {
    return {
      clicked: false,
      clicked1: false,
      session: [],
      timerCount: '',
      timerDisplay: '',
      buttonShow: false,
    }
  },
  head() {
    return {
      title: 'Tutor Workspace',
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
  computed: {
    logout() {
      return {
        display: this.clicked ? 'flex' : 'none',
      }
    },
    updateModal() {
      return {
        display: this.clicked1 ? 'flex' : 'none',
      }
    },
    ...mapGetters({
      user: 'getUser',
      pastSessions: 'getPastSessions',
      startedSessions: 'getStartedSessions',
    }),
  },
  watch: {
    timerCount: {
      handler(value) {
        if (value > 0) {
          setTimeout(() => {
            this.timerCount--
            if (this.timerCount === 600 || this.timerCount < 600) {
              this.buttonShow = true
            }
          }, 1000)
        } else if (value === 600) {
          alert(
            'You can now end this class. There are still ten minutes remaining in your meeting.'
          )
        } else if (value === 0) {
          alert("This meeting's time is up, please end the meeting shortly.")
        }
        const t = new Date(1970, 0, 1)
        t.setSeconds(value)
        this.timerDisplay = t.toString()
      },
      immediate: true,
    },
  },
  async created() {
    this.session = await fetch('/api/sessions/' + this.$route.params.id + '/', {
      credentials: 'include',
    }).then((res) => {
      if (res.status === 500) {
        this.$router.push('/')
      }
      return res.json()
    })
    const time = new Date()
    let hours = time.getHours()
    let minutes = time.getMinutes()
    let seconds = time.getSeconds()
    if (hours < 10) {
      hours = '0' + hours.toString()
    } else if (minutes < 10) {
      minutes = '0' + minutes.toString()
    } else if (seconds < 10) {
      seconds = '0' + seconds.toString()
    }
    const now = hours + ':' + minutes + ':' + seconds
    const hms = str(sub([this.session.time_end, now]))
    console.log(this.session.time_end, now, hms)
    const a = hms.split(':')
    const timerSeconds = +a[0] * 60 * 60 + +a[1] * 60 + +a[2]
    console.log(a, timerSeconds)
    this.timerCount = timerSeconds
    await this.fetchUser()
    await this.fetchSessions('pastSessions')
    await this.fetchSessions('startedSessions')
  },
  methods: {
    dateToString,
    logoutclick() {
      this.clicked = !this.clicked
    },
    async updateModalValue() {
      this.session = await fetch(
        '/api/sessions/' + this.$route.params.id + '/',
        {
          credentials: 'include',
        }
      ).then((res) => {
        if (res.status === 500) {
          this.$router.push('/')
        }
        return res.json()
      })
      this.clicked1 = !this.clicked1
    },
    async endclass() {
      await fetch('/api/finish_session/' + this.$route.params.id + '/', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'X-CSRFToken': (await getCSRF()).success,
          'Content-Type': 'application/json',
        },
      }).then(() => {
        this.removeSession([this.session, 'startedSessions'])
        this.addSession([this.session, 'pastSessions'])
        this.$router.push('/')
      })
    },
    ...mapActions([
      'fetchUser',
      'fetchSessions',
      'removeSession',
      'addSession',
    ]),
    ...mapGetters(['getPastSessions', 'getStartedSessions']),
  },
}
</script>
<style>
.tutordiv-block-80 {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  margin: 10px 5%;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 20px;
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
  border-radius: 8px;
  background-color: #fff;
  box-shadow: 0 8px 20px 0 rgba(0, 0, 0, 0.15);
}
</style>
 

