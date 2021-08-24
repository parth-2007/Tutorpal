<template>
  <client-only>
    <html
      data-wf-page="5f600218af481481a99ffa6a"
      data-wf-site="5f600218af4814e3759ffa69"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <body id="body" style="min-height: 100vh" class="body">
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
                    id="image"
                    width="60"
                    height="60"
                    sizes="(max-width: 479px) 15vw, (max-width: 767px) 8vw, 60px"
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
                      <div class="text-block-18" id="name">
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
                    class="nav-link-4 w-nav-link w--current"
                    >Explore</router-link
                  ><router-link to="/inbox" class="nav-link-4 w-nav-link"
                    >Messages
                    <span class="badge">{{ user.unread }}</span> </router-link
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
        <div class="columns-4 w-row">
          <div class="column-18 w-col w-col-8">
            <div class="div-block-44">
              <div class="div-block-45">
                <img
                  src="../static/student/images/question.png"
                  loading="lazy"
                  width="30"
                  alt=""
                /><a
                  href="mailto:the2tor4u@gmail.com?subject=Website%20Email"
                  class="link-2"
                  >Need help? Send us an email</a
                >
              </div>
              <div class="div-block-48">
                <div class="text-block-23">Trending</div>
                <p class="paragraph">
                  Find the highest-ranked tutors and the ones everybody is
                  learning from.
                </p>
              </div>
              <div class="trending">
                <div v-for="tutor of trending" :key="tutor.id" id="trending">
                  <router-link
                    :to="'/tutors/' + tutor.id"
                    class="link-block-2 w-inline-block"
                  >
                    <div style="line-height: 14px" class="div-block-54">
                      <img
                        :src="
                          tutor.user !== undefined ? tutor.user.profilePic : ''
                        "
                        loading="lazy"
                        width="38"
                        height="38"
                        sizes="38px"
                        alt=""
                        class="image-5"
                      />
                      <div class="text-block-21">
                        <strong class="bold-text-3"
                          >{{
                            tutor.user !== undefined ? tutor.user.firstName : ''
                          }}
                          {{
                            tutor.user !== undefined ? tutor.user.lastName : ''
                          }}</strong
                        >
                      </div>
                      <div class="text-block-21-copy">
                        Subject: {{ tutor.subjects }}
                      </div>
                      <div class="text-block-21-copy-2">
                        Price: ${{ tutor.rates }} hourly
                      </div>
                      <div class="text-block-21-copy-2">
                        Degree: {{ tutor.education }}
                      </div>
                      <div class="text-block-21-copy-2">
                        Education: {{ tutor.major }} at {{ tutor.school }}, GPA
                        of {{ tutor.gpa }}
                      </div>
                      <div class="text-block-21-copy-2">
                        Reviews: {{ tutor.averageReviews }} Stars
                      </div>
                      <div class="text-block-21-copy-2">
                        Occupation: {{ tutor.occupation }}
                      </div>
                    </div>
                  </router-link>
                </div>
              </div>
            </div>
          </div>
          <div class="column-15 w-col w-col-4">
            <div style="margin-bottom: 20px" class="div-block-53">
              <h1 class="heading-2">Starting:</h1>
              <div class="upcoming_loop">
                <div
                  style="margin-bottom: 50px"
                  v-for="session in started"
                  :key="session.id"
                  id="started"
                >
                  <div class="upcoming_item">
                    <p class="paragraph-3">
                      Date: {{ session.date }}<br />Time:
                      {{ convertTime(session.timeStart) }} -
                      {{ convertTime(session.timeEnd) }}<br />Tutor:
                      {{
                        session.tutor !== undefined
                          ? session.tutor.user.firstName
                          : ''
                      }}
                      {{
                        session.tutor !== undefined
                          ? session.tutor.user.lastName
                          : ''
                      }}<br />Subject:
                      {{
                        session.tutor !== undefined
                          ? session.tutor.subjects
                          : ''
                      }}<br />Class Description:
                      {{ session.description }}‍<br />
                    </p>
                    <a
                      @click="joinSession(session.id)"
                      class="button-4 w-button"
                      >Join Meeting</a
                    >
                  </div>
                </div>
              </div>
            </div>
            <div
              style="height: 300px; margin-bottom: 20px"
              class="div-block-53"
            >
              <h1 class="heading-2">Upcoming Classes:</h1>
              <div class="upcoming_loop">
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
                    width="10"
                    alt=""
                  />
                  <div class="upcoming_item">
                    <p class="paragraph-3">
                      Date: {{ session.date }}<br />Time:
                      {{ convertTime(session.timeStart) }} -
                      {{ convertTime(session.timeEnd) }}<br />Tutor:
                      {{
                        session.tutor !== undefined
                          ? session.tutor.user.firstName
                          : ''
                      }}
                      {{
                        session.tutor !== undefined
                          ? session.tutor.user.lastName
                          : ''
                      }}<br />Subject:
                      {{
                        session.tutor !== undefined
                          ? session.tutor.subjects
                          : ''
                      }}<br />‍Class Description:
                      {{ session.description }}‍<br /><strong
                        style="margin-top: 10px"
                        class="bold-text-2"
                        >Don&#x27;t worry if you can&#x27;t keep track of your
                        classes, we send an email 10 minutes prior to the
                        beginning of the class.</strong
                      >
                    </p>
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
import convertTime from '../utils/convertTime'
import getCSRF from '../utils/getCSRF'

export default {
  data() {
    return {
      clicked: false,
    }
  },
  async fetch() {
    await this.fetchTrending()
    await this.fetchSessions('startedSessions')
  },
  head() {
    return {
      title: 'Home',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
        { rel:"stylesheet", type:"text/css", href: "/student/css/student-main.webflow.css" },
      ]
    }
  },
  computed: {
    logout() {
      return {
        display: this.clicked ? 'flex' : 'none',
      }
    },
    ...mapGetters({
      user: 'getUser',
      started: 'getStartedSessions',
      trending: 'getTrending',
      upcoming: 'getUpcoming',
    }),
  },
  async created() {
    await this.fetchSessions('upcoming')
    await this.fetchUser()
  },
  methods: {
    ...mapActions([
      'fetchUser',
      'fetchSessions',
      'fetchTrending',
      'removeSession',
    ]),
    ...mapGetters(['getStartedSessions', 'getUser', 'getUpcoming']),
    convertTime,
    logoutclick() {
      this.clicked = !this.clicked
    },
    async joinSession(id) {
      let url = 'https://api.tutorpal.org/sessions/' + id + '/'
      const csrfToken = await getCSRF()
      await fetch(url, {
        credentials: 'include',
        method: 'PATCH',
        headers: {
          'X-CSRFToken': csrfToken.success,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          student_joined: true,
        }),
      })
      url = '/sessions/' + id + '/'
      this.$router.push(url)
    },
    async canceledHandler(id, session) {
      const x = confirm('Please confirm that you wish to cancel this session.')
      if (x === true) {
        const url = 'https://api.tutorpal.org/sessions/' + id + '/'
        const csrfToken = await getCSRF()
        await fetch(url, {
          method: 'PATCH',
          credentials: 'include',
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
.badge {
  position: absolute;
  top: 11px;
  right: 3px;
  padding: 4px 7px;
  border-radius: 1000px;
  background-color: red;
  color: white;
  font-family: Poppins;
  font-size: 14px;
}
</style>