<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <body id="body" style="min-height: 100vh" class="tutorbody-4">
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
                  class="tutornav-link-4 w-nav-link"
                  >Requests</router-link
                ><router-link to="/inbox" class="tutornav-link-4 w-nav-link"
                  >Messages<span v-if="user.unread > 0" class="tutorbadge">{{
                    user.unread
                  }}</span></router-link
                ><router-link
                  to="/payments"
                  class="tutornav-link-4 w-nav-link w--current"
                  >Payments</router-link
                >
                <router-link
                  to="/volunteering"
                  class="tutornav-link-4 w-nav-link"
                  >Volunteering
                </router-link>
              </nav>
              <div class="tutormenu-button-2 w-nav-button">
                <div class="tutoricon-2 w-icon-nav-menu"></div>
              </div>
            </div>
          </div>
        </div>
        <div class="tutordiv-block-48-copy">
          <div class="tutortext-block-23">Payments</div>
          <p class="tutorparagraph">
            All of your payments for your finished classes will be recorded
            here.
          </p>
        </div>
        <div v-if="paymentfinished.unfetched === undefined">
          <div v-for="session in paymentfinished" :key="session.id" id="paid">
            <div class="tutordiv-block-64">
              <div class="tutortext-block-43">
                <strong class="tutorbold-text-7">Status:</strong> Paid
              </div>
              <div class="tutortext-block-43">
                <strong class="tutorbold-text-8">Amount: </strong>${{
                  session.price
                }}
              </div>
              <div class="tutortext-block-43">
                <strong class="tutorbold-text-10">Student:</strong>
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
              </div>
              <div class="tutortext-block-43">
                <strong class="tutorbold-text-10">Class Date:</strong>
                {{ session.date }}
              </div>
              <div class="tutortext-block-43">
                <strong class="tutorbold-text-10">Time: </strong
                >{{ convertTime(session.timeStart) }} -
                {{ convertTime(session.timeEnd) }}
              </div>
            </div>
          </div>
        </div>
        <div class="tutordiv-block-48-copy">
          <div class="tutortext-block-23">Unpaid Classes (student)</div>
          <p class="tutorparagraph">
            You are not required to start this class until your student has paid
            for it.
          </p>
        </div>
        <div v-if="paymentpending.unfetched === undefined">
          <div v-for="session in paymentpending" :key="session.id" id="unpaid">
            <div class="tutordiv-block-64">
              <div class="tutortext-block-43">
                <strong class="tutorbold-text-7">Status:</strong> Unpaid
              </div>
              <div class="tutortext-block-43">
                <strong class="tutorbold-text-8">Amount: </strong>${{
                  session.price
                }}
              </div>
              <div class="tutortext-block-43">
                <strong class="tutorbold-text-10">Student:</strong>
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
              </div>
              <div class="tutortext-block-43">
                <strong class="tutorbold-text-10">Class Date:</strong>
                {{ session.date }}
              </div>
              <div class="tutortext-block-43">
                <strong class="tutorbold-text-10">Time: </strong
                >{{ convertTime(session.timeStart) }} -
                {{ convertTime(session.timeEnd) }}
              </div>
              <img
                @click="canceledHandler(session.id, session)"
                style="cursor: pointer; margin-left: 25px"
                src="../static/student/images/close-1.png"
                align="right"
                width="15"
                alt=""
              />
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
    await this.fetchSessions('pastSessions')
    await this.fetchUser()
  },
  head() {
    return {
      title: 'My Payments',
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
      paymentpending: 'getPendingOnStudentPayment',
      paymentfinished: 'getPastSessions',
    }),
    logout() {
      return {
        display: this.clicked ? 'flex' : 'none',
      }
    },
  },
  async created() {
    await this.fetchSessions('pendingOnStudentPayment')
  },
  methods: {
    ...mapGetters(['getUser', 'getPendingOnStudentPayment', 'getPastSessions']),
    ...mapActions(['fetchUser', 'fetchSessions', 'removeSession']),
    convertTime,
    logoutclick() {
      this.clicked = !this.clicked
    },
    async canceledHandler(id, session) {
      const x = confirm('Please confirm that you wish to cancel this session.')
      if (x === true) {
        const csrfToken = await getCSRF()
        await fetch(process.env.API_URL + '/sessions/' + id + '/', {
          method: 'PATCH',
          credentials: 'include',
          headers: {
            'X-CSRFToken': csrfToken.success,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            canceled: true,
          }),
        }).then((res) => {
            console.log(res)
          })
        this.removeSession([session, 'pendingOnStudentPayment'])
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
  padding: 4px 7px;
  border-radius: 1000px;
  background-color: red;
  color: white;
  font-family: Poppins;
  font-size: 14px;
}
</style>