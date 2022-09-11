<template>
  <client-only>
    <html
      data-wf-page="5f5d0db29d3d2a83a01fb34a"
      data-wf-site="5f5d0db29d3d2a6ab81fb349"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <div v-if="showButton === true" style="font-family: Poppins;" class="d-grid gap-2">
        <router-link to="/seminars" class="btn btn-primary" type="button">Join Current Seminar</router-link>
      </div>
      <body id="body" style="min-height: 100vh" class="tutorbody">
        <div id="main">
          <div class="tutorsection">
            <router-link to="/" class="tutorlink-block w-inline-block"
              ><img
                src="../static/tutor/images/logo.jpg"
                loading="lazy"
                width="260"
                srcset="
                  ../static/tutor/images/logo.jpg  500w,
                  ../static/tutor/images/logo.jpg  800w,
                  ../static/tutor/images/logo.jpg 1080w,
                  ../static/tutor/images/logo.jpg 1432w
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
          <div class="tutordiv-block-6">
            <div
              data-collapse="none"
              data-animation="default"
              data-duration="400"
              role="banner"
              class="tutornavbar-2 w-nav"
            >
              <div class="tutorcontainer-2 w-container">
                <nav role="navigation" class="tutornav-menu-3 w-nav-menu">
                  <router-link
                    to="/"
                    aria-current="page"
                    class="tutornav-link-4 w-nav-link w--current"
                    >Requests
                  </router-link
                  ><router-link
                    to="/seminars"
                    class="tutornav-link-4 w-nav-link w--current"
                    >Seminars
                  </router-link
                  ><router-link to="/inbox" class="tutornav-link-4 w-nav-link"
                    >Messages
                    <span v-if="user.unread > 0" class="tutorbadge">{{
                      user.unread
                    }}</span> </router-link
                  ><router-link
                    to="/payments"
                    class="tutornav-link-4 w-nav-link"
                    >Payments</router-link>
                  <router-link
                    to="/volunteering"
                    class="tutornav-link-4 w-nav-link"
                    >Volunteering</router-link>
                  <router-link to="/calendar" class="nav-link-4 w-nav-link"
                    >Calendar</router-link>
                    <router-link to="/donations" class="nav-link-4 w-nav-link"
                      >Donate</router-link>
                </nav>
                <div class="tutormenu-button-2 w-nav-button">
                  <div class="tutoricon-2 w-icon-nav-menu"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="columns-4 w-row">
          <div class="w-col w-col-8">
            <div class="tutordiv-block-44">
              <div class="tutordiv-block-45">
                <img
                  src="../static/tutor/images/question.png"
                  loading="lazy"
                  width="30"
                  alt=""
                /><a
                  href="mailto:info@tutorpal.org"
                  class="tutorlink-2"
                  >Need help? Send us an email</a
                >
              </div>
              <h1 class="tutorheading">Student Requests</h1>
              <div class="tutordiv-block-48">
                <div class="tutortext-block-23">Inbox</div>
                <p class="tutorparagraph">
                  Please accept or deny these requests based off of your comfort
                  ability.
                </p>
              </div>
              <div v-if="requests.unfetched === undefined">
                <div
                  v-for="session in requests"
                  :key="session.id"
                  id="inbox"
                  class="tutorloop"
                >
                  <div class="tutoritem">
                    <div class="tutordiv-block-51">
                      <img
                        :src="
                          session.student !== undefined
                            ? session.student.user.profilePic
                            : ''
                        "
                        loading="lazy"
                        width="60"
                        sizes="64px"
                        alt=""
                        class="tutorimage-9"
                      />
                    </div>
                    <p
                      style="font-size: 20px; margin-bottom: 15px"
                      class="tutorparagraph-2"
                    >
                      {{
                        session.student !== undefined
                          ? session.student.user.firstName
                          : ''
                      }}
                      {{
                        session.student !== undefined
                          ? session.student.user.lastName
                          : ''
                      }}
                    </p>
                    <p class="tutorparagraph-2">
                      <strong class="tutorbold-text"
                        >Class Information<br /></strong
                      >First Session: {{ session.date }}<br />Duration:
                      {{ convertTime(session.timeStart) }} -
                      {{ convertTime(session.timeEnd) }}<br />Trial:
                      {{ session.free }}<br />Amount: ${{ session.price }}
                    </p>
                    <p class="tutorparagraph-2">
                      <strong class="tutorbold-text">Student Information</strong>
                      <br />Topic: {{ session.subjects }}
                      <br />Description: {{ session.description }}
                    </p>
                    <div class="tutortext-block-27">
                      Remember, you only have 24 hours from since this request
                      was sent to accept or deny.
                    </div>
                    <div style="margin-bottom: 20px;" class="tutordiv-block-52">
                      <a
                        @click="accept(session.id, session)"
                        style="z-index: 5"
                        aria-current="page"
                        class="tutorbutton-3 w-button w--current"
                        >Accept</a
                      ><a
                        @click="deny(session.id, session)"
                        style="z-index: 5"
                        aria-current="page"
                        class="tutorbutton-3-copy w-button w--current"
                        >Deny</a
                      >
                    </div>
                    <router-link
                      to="/inbox"
                      style="
                        font-family: Poppins;
                        font-size: 14px;
                        color: #41a8d3;
                        text-decoration: underline;
                      "
                      >Message this student</router-link
                    >
                  </div>
                </div>
                <a
                  @click="fetchNewRequests()"
                  v-if="next !== null"
                  style="
                    font-family: Poppins;
                    font-size: 14px;
                    color: #41a8d3;
                    text-decoration: underline;
                  "
                  >Click to view more pending requests</a
                >
              </div>
            </div>
          </div>
          <div class="tutorcolumn-15 w-col w-col-4">
            <div style="margin-bottom: 20px" class="tutordiv-block-53">
              <h1 class="tutorheading-2">Starting:</h1>
              <div
                v-if="started.unfetched === undefined"
                class="tutorupcoming_loop"
              >
                <div
                  style="margin-bottom: 50px"
                  v-for="session in started"
                  :key="session.id"
                  id="started"
                >
                  <div class="tutorupcoming_item">
                    <p class="tutorparagraph-3">
                      Date: {{ session.date }}<br />Time:
                      {{ convertTime(session.timeStart) }} -
                      {{ convertTime(session.timeEnd) }}<br />Student:
                      {{
                        session.student !== undefined
                          ? session.student.user.firstName
                          : ''
                      }}
                      {{
                        session.student !== undefined
                          ? session.student.user.lastName
                          : ''
                      }}<br />Topic: {{ session.subjects }}<br />Class
                      Description: {{ session.description }}‍<br />
                    </p>
                    <router-link
                      :to="'/sessions/' + session.id"
                      class="tutorbutton-4 w-button"
                      >Join Meeting</router-link
                    >
                  </div>
                </div>
              </div>
            </div>
            <div
              style="height: 300px; margin-bottom: 20px"
              class="tutordiv-block-53"
            >
              <h1 class="tutorheading-2">Upcoming Classes:</h1>
              <div
                v-if="upcoming.unfetched === undefined"
                class="tutorupcoming_loop"
              >
                <div
                  style="margin-bottom: 50px"
                  v-for="session in upcoming"
                  :key="session.id"
                  id="upcoming"
                >
                  <img
                    @click="canceledHandler(session.id, session)"
                    style="cursor: pointer"
                    src="../static/student/images/close-1.png"
                    align="right"
                    width="12.5"
                    alt=""
                  />
                  <div class="tutorupcoming_item">
                    <p class="tutorparagraph-3">
                      Date: {{ session.date }}<br />Time:
                      {{ convertTime(session.timeStart) }} -
                      {{ convertTime(session.timeEnd) }}<br />Student:
                      {{
                        session.student !== undefined
                          ? session.student.user.firstName
                          : ''
                      }}
                      {{
                        session.student !== undefined
                          ? session.student.user.lastName
                          : ''
                      }}<br />Topic: {{ session.subjects }}<br />‍Class
                      Description: {{ session.description }}‍
                    </p>
                    <button
                      @click="startclass(session.id, session)"
                      class="tutorbutton-4 w-button"
                    >
                      Start this meeting
                    </button>
                  </div>
                </div>
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
import { add, sub } from 'timelite/time'
import convertTime from '../utils/convertTime'
import getCSRF from '../utils/getCSRF'
export default {
  data() {
    return {
      clicked: false,
      requests1: [],
      next: '',
      showButton: false,
      countPendingRequests: 0,
    }
  },
  async fetch() {
    await this.fetchUser()
    await this.fetchSessions('upcoming')
    await this.fetchSessions('pendingOnTutor')
    console.log(this.user.id)
    const range = ["2:50", "4:10"];
    const value = (new Date().toLocaleTimeString()).substring(0, 4)
    const dayOfWeekName = new Date().toLocaleString(
      'default', {weekday: 'long'}
    );

    /* eslint-disable */
    if (value >= range[0] && value <= range[1] && dayOfWeekName === "Monday" && this.user.id===59){
      this.showButton = true;
    }
    else if(value >= range[0] && value <= range[1] && dayOfWeekName === "Wednesday" && this.user.id===85){
      this.showButton = true;
    }

    /* eslint-enable */
    this.countPendingRequests = this.requests.length;
  },
  head() {
    return {
      title: 'Home',
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
    ...mapGetters({
      user: 'getUser',
      started: 'getStartedSessions',
      requests: 'getPendingOnTutor',
      upcoming: 'getUpcoming',
    }),
    logout() {
      return {
        display: this.clicked ? 'flex' : 'none',
      }
    },
  },
  async created() {
    await this.fetchSessions('startedSessions')
    this.requests1 = await fetch(
      process.env.API_URL + '/sessions/pending_on_tutor/',
      {
        credentials: 'include',
      }
    ).then((res) => res.json())
    this.next = this.requests1.next
    
  },
  methods: {
    ...mapActions([
      'fetchUser',
      'fetchSessions',
      'addSession',
      'removeSession',
    ]),
    ...mapGetters([
      'getStartedSessions',
      'getUser',
      'getUpcoming',
      'getPendingOnTutor',
    ]),
    convertTime,
    async fetchNewRequests() {
      const data = await fetch(this.next, {
        credentials: 'include',
      }).then((res) => res.json())
      this.requests1.results.push(data.results)
      this.next = data.next
    },
    async accept(id, session) {
      const csrfToken = await getCSRF()
      await fetch(process.env.API_URL + '/sessions/' + id + '/', {
        method: 'PATCH',
        credentials: 'include',
        headers: {
          'X-CSRFToken': csrfToken.success,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          accepted: true,
        }),
      })
      this.removeSession([session, 'pendingOnTutor'])
    },
    async deny(id, session) {
      const csrfToken = await getCSRF()
      await fetch(process.env.API_URL + '/sessions/' + id + '/', {
        method: 'PATCH',
        credentials: 'include',
        headers: {
          'X-CSRFToken': csrfToken.success,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          rejected: true,
        }),
      })
      this.removeSession([session, 'pendingOnTutor'])
    },
    async startclass(id, session) {
      const today = new Date()
      const y = add(['00:10:00', session.timeStart])
      const x = sub([session.timeStart, '00:10:00'])

      const start = x[0] * 60 + x[1]
      const end = y[0] * 60 + y[1]
      const now = today.getHours() * 60 + today.getMinutes()

      const dd = String(today.getDate()).padStart(2, '0')
      const mm = String(today.getMonth() + 1).padStart(2, '0')
      const yyyy = today.getFullYear()
      const date = yyyy + '-' + mm + '-' + dd

      if (date === session.date && start < now && now < end) {
        const csrfToken = await getCSRF()
        await fetch(process.env.API_URL + '/sessions/' + id + '/', {
          method: 'PATCH',
          credentials: 'include',
          headers: {
            'X-CSRFToken': csrfToken.success,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            started: true,
          }),
        }).then((res) => {
          this.removeSession([session, 'upcoming'])
          this.addSession([session, 'startedSessions'])
        })
      } else {
        alert(
          'You are attempting to start this session too early or too late. You are only allowed to start a class at 10 minutes prior to the class start time or at most 10 minutes after.'
        )
      }
    },
    logoutclick() {
      this.clicked = !this.clicked
    },
    async canceledHandler(id, session) {
      const x = confirm('Please confirm that you wish to cancel this session.')
      if (x === true) {
        const csrfToken = await getCSRF()
        await fetch(process.env.API_URL + '/sessions/' + id + '/', {
          credentials: 'include',
          method: 'PATCH',
          headers: {
            'X-CSRFToken': csrfToken.success,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            canceled: true,
          }),
        })
        this.removeSession([session, 'upcoming'])
      }
    },
  },
}
</script>
<style scoped>

.tutorbadge {
  position: absolute;
  top: 11px;
  right: 3px;
  padding: 2px 8px;
  border-radius: 1000px;
  background-color: red;
  color: white;
  font-family: Poppins;
  font-size: 14px;
}
</style>