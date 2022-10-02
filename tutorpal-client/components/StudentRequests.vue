<template>
  <client-only>
    <html
      data-wf-page="5f600218af481481a99ffa6a"
      data-wf-site="5f600218af4814e3759ffa69"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <body id="body" style="min-height: 100vh" class="body-3">
        <div id="main">
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
                <div style="margin-left: 0px; padding-left: 0px" class="stuff w-form">
                  <img
                    src="../static/student/images/search-1.png"
                    loading="lazy"
                    width="25"
                    height="25"
                    srcset="
                      ../static/student/images/search-1.png 500w,
                      ../static/student/images/search-1.png       512w
                    "
                    sizes="(max-width: 767px) 25px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw"
                    alt=""
                    class="image-2"
                  /><input
                      class="search-3 w-input"
                      placeholder="Search by subject"
                      id="search"
                      v-model="q"
                      @keyup.enter="submitSearch()"
                  /><input
                    type="submit"
                    value="Search"
                    class="button-8 _100 _5px-left w-button"
                  />
              </div>
                <div class="div-block-43">
                  <div class="name_profile_pic">
                    <img
                      :src="user !== undefined ? user.profilePic : ''"
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
                      ><router-link
                    to="/seminars"
                    class="tutornav-link-4 w-nav-link"
                    >Seminars
                  </router-link
                    ><router-link
                      to="/requests"
                      class="nav-link-4 w-nav-link w--current"
                      >Requests</router-link
                    ><router-link to="/payments" class="nav-link-4 w-nav-link"
                      >Payments</router-link
                    ><router-link to="/calendar" class="nav-link-4 w-nav-link"
                      >Calendar</router-link>
                    <router-link to="/donations" class="nav-link-4 w-nav-link"
                      >Donate</router-link>
                  </nav>
                  <div class="menu-button-2 w-nav-button">
                    <div class="icon-2 w-icon-nav-menu"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="div-block-66">
            <div class="div-block-45">
              <img
                src="../static/student/images/question.png"
                loading="lazy"
                width="30"
                alt=""
              /><a
                href="mailto:info@tutorpal.org?subject=Website%20Email"
                class="link-2"
                >Need help? Send us an email</a
              >
            </div>
            <h1 class="heading">Student Requests</h1>
            <div class="div-block-65">
              <div class="text-block-23">Requests</div>
              <p class="paragraph">
                These are the requests you have sent to potential tutors who
                have not accepted yet. Once the tutor has accepted, please check
                the
                <router-link to="/payments" class="link-3"
                  >payments</router-link
                >
                page to pay for the class.
              </p>
            </div>
            <div v-if="requests.unfetched === undefined">
              <div
                v-for="session in requests"
                :key="session.id"
                id="requests"
                class="loop"
              >
                <div class="i">
                  <img
                    @click="canceledHandler(session.id, session)"
                    style="margin-top: 10px; cursor: pointer"
                    src="../static/student/images/close-1.png"
                    align="right"
                    width="15"
                    alt=""
                  />
                  <div class="div-block-51-copy">
                    <img
                      :src="
                        session.tutor !== undefined
                          ? session.tutor.user.profilePic
                          : ''
                      "
                      loading="lazy"
                      width="75"
                      height="75"
                      sizes="100px"
                      alt=""
                      class="image-15"
                    />
                    <p class="paragraph-2">
                      <strong class="bold-text">Schedule <br /></strong>First
                      Session: {{ session.date }}<br />Tutor:
                      {{
                        session.tutor !== undefined
                          ? session.tutor.user.firstName
                          : ''
                      }}
                      {{
                        session.tutor !== undefined
                          ? session.tutor.user.lastName
                          : ''
                      }}<br />Duration: {{ convertTime(session.timeStart) }} -
                      {{ convertTime(session.timeEnd) }} <br />Amount: ${{
                        session.price
                      }}<br />Trial: {{ session.free }}
                    </p>
                  </div>
                  <p class="paragraph-2-copy">
                    <strong class="bold-text">Student Information</strong>
                    <br />Topic: {{ session.subjects }}
                    <br />Description: {{ session.description }}
                  </p>
                  <div class="text-block-27">
                    This tutor has not accepted your request yet.
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
      q: ''
    }
  },
  async fetch() {
    await this.fetchSessions('pendingOnTutor')
    await this.fetchUser()
  },
  head() {
    return {
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
    ...mapGetters({ user: 'getUser', requests: 'getPendingOnTutor' }),
  },
  methods: {
    ...mapActions(['fetchUser', 'fetchSessions', 'removeSession']),
    ...mapGetters(['getUser', 'getPendingOnTutor']),
    convertTime,
    logoutclick() {
      this.clicked = !this.clicked
    },
    submitSearch() {
      this.$router.push("/search/"+this.q);
    },
    async canceledHandler(id, session) {
      const x = confirm('Please confirm that you wish to cancel this session.')
      if (x === true) {
        await fetch(process.env.API_URL + '/sessions/' + id + '/', {
          method: 'PATCH',
          credentials: 'include',
          headers: {
            'X-CSRFToken': (await getCSRF()).success,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            canceled: true,
          }),
        })
        this.removeSession([session, 'pendingOnTutor'])
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