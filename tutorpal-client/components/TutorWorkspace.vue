<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <div v-if="session.student_paid === true && session.started === false">
        <p style="font-size: 18px; font-family: Poppins; margin: 15px">
          This class has not been started yet, your job as a tutor is to start
          meetings when the proper times and date occur.
        </p>
      </div>
      <div
        v-else-if="session.student_paid === false || session.finished === true"
      >
      </div>
      <div v-else-if="session.tutor_pk !== user.tutorPk">
      </div>
      <body
        v-else
        id="body"
        style="background-color: rgba(65, 168, 211, 0.2)"
        class="body-5"
      >
        <div
          :style="updateModal"
          style="padding-bottom: 0px"
          class="div-block-22"
        >
          <div
            style="
              border-radius: 8px;
              padding-bottom: 20px;
              height: 240px;
              width: 375px;
              font-family: Poppins;
            "
            class="div-block-23"
          >
            <div v-if="session.student_joined === true" class="div-block-25">
              <strong
                >You have {{ dateToString(timerDisplay) }} left in this class,
                are you sure you want to end it?</strong
              >
              <br />Clicking "confirm" will confirm to us that this class has
              been finished. You will be paid shortly after. Thank you for
              tutoring with TutorPal!
            </div>
            <div
              v-else
              style="margin-left: 10px; margin-top: 10px; margin-right: 10px"
            >
              Your student has not joined this class, therefore, we are not
              allowing you to end this class. If there are any issues, please
              contact us at support@tutorpal.org. We are very sorry for the
              inconvienence and hope you will continue to tutor on this
              platform.
            </div>
            <button
              v-if="session.student_joined === true"
              @click="endclass()"
              style="
                background-color: green;
                margin-left: 10px;
                margin-top: 10px;
                font-size: 14px;
              "
              class="button-10-copy-copy w-button"
            >
              Confirm</button
            ><button
              @click="updateModalValue()"
              style="
                background-color: #bb0a1e;
                margin-left: 10px;
                margin-top: 10px;
                font-size: 14px;
              "
              class="button-10-copy-copy w-button"
            >
              Cancel
            </button>
          </div>
        </div>
        <div id="main">
          <div class="section">
            <router-link to="/" class="link-block w-inline-block"
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
            <div class="div-block-4">
              <div class="div-block-43">
                <div class="name_profile_pic">
                  <img
                    :src="user.profilePic"
                    id="image"
                    width="60"
                    height="60"
                    sizes="60px"
                    alt=""
                    class="image-7"
                  />
                  <div
                    data-hover=""
                    data-delay="0"
                    class="dropdown-3 w-dropdown"
                  >
                    <div
                      @click="logoutclick()"
                      class="dropdown-toggle-2-copy w-dropdown-toggle"
                    >
                      <div id="name" class="text-block-18">
                        {{ user.firstName }} {{ user.lastName }}
                      </div>
                      <div class="text-block-20">Tutor</div>
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
        </div>
        <div class="columns-2-copy w-row">
          <div class="column w-col w-col-6">
            <button
              v-if="buttonShow === true"
              @click="updateModalValue()"
              class="button-10-copy-copy w-button"
              style="
                margin-top: 10px;
                margin-bottom: 10px;
                margin-left: 20px;
                background-color: #bb0a1e;
              "
            >
              End this Class
            </button>
          </div>
          <div style="float: right; margin-right: 20px">
            <h1
              style="
                font-family: Poppins;
                margin-left: 20px;
                margin-top: 10px;
                margin-bottom: 10px;
                font-size: 24px;
                color: black;
              "
            >
              <strong>Countdown Timer: {{ dateToString(timerDisplay) }}</strong>
            </h1>
          </div>
        </div>
        <iframe
          style="width: 100vw; height: 78.5vh"
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
        { rel: 'stylesheet', type: 'text/css', href: '/tutor/css/webflow.css' },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/tutor/css/tutor-main.webflow.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/tutor/css/normalize.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css',
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
    ...mapGetters({ user: 'getUser', pastSessions: 'getPastSessions' }),
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
            'There are ten minutes remaining in this class. We suggest wrapping things up!'
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
    const url =
      'https://api.tutorpal.org/sessions/' + this.$route.params.id + '/'
    this.session = await fetch(url, {
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
    const a = hms.split(':')
    const timerSeconds = +a[0] * 60 * 60 + +a[1] * 60 + +a[2]
    this.timerCount = timerSeconds
    await this.fetchUser()
    await this.fetchSessions('pastSessions')
  },
  methods: {
    dateToString,
    logoutclick() {
      this.clicked = !this.clicked
    },
    async updateModalValue() {
      this.session = await fetch(
        'https://api.tutorpal.org/sessions/' + this.$route.params.id + '/',
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
      const url ='https://api.tutorpal.org/finish_session/' + this.$route.params.id + '/'
      await fetch(url, {
        method: 'POST',
        credentials: 'include',
        headers: {
          'X-CSRFToken': (await getCSRF()).success,
          'Content-Type': 'application/json',
        },
      }).then(() => {
        this.removeSession([this.session, 'pastSessions'])
        this.$router.push('/')
      })
    },
    ...mapActions(['fetchUser', 'fetchSessions', 'removeSession',]),
    ...mapGetters(['getPastSessions'])
  },
}
</script>
<style>
.div-block-80 {
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
 

