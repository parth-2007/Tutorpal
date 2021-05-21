<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
    <body id="body" style="height: 100vh" class="body-4">
      <div style="height: 100%">
      <div id="main">
        <div class="section"><router-link to="/" class="link-block w-inline-block"><img src="../static/tutor/images/logo.jpg" loading="lazy" width="260" srcset="../static/tutor/images/logo-p-500.jpeg 500w, ../static/tutor/images/logo-p-800.jpeg 800w, ../static/tutor/images/logo-p-1080.jpeg 1080w, ../static/tutor/images/logo.jpg 1432w" sizes="(max-width: 479px) 100vw, (max-width: 767px) 34vw, (max-width: 991px) 25vw, (max-width: 1439px) 21vw, (max-width: 1919px) 15vw, 12vw" alt=""></router-link>
          <div class="div-block-4">
            <div class="div-block-43">
              <div class="name_profile_pic"><img :src="user.profilePic" id="image" width="60" height="60" sizes="60px" alt="" class="image-7">
                <div data-hover="" data-delay="0" class="dropdown-3 w-dropdown">
                  <div @click="logoutclick()" class="dropdown-toggle-2-copy w-dropdown-toggle">
                      <div id="name" class="text-block-18">{{user.firstName}} {{user.lastName}}</div>
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
        <div class="div-block-6">
          <div data-collapse="none" data-animation="default" data-duration="400" role="banner" class="navbar-2 w-nav">
            <div class="container-2 w-container">
              <nav role="navigation" class="nav-menu-3 w-nav-menu"><router-link to="/" aria-current="page" class="nav-link-4 w-nav-link">Requests</router-link><router-link to="/inbox" class="nav-link-4 w-nav-link">Messages</router-link><router-link to="/payments" class="nav-link-4 w-nav-link w--current">Payments</router-link></nav>
              <div class="menu-button-2 w-nav-button">
                <div class="icon-2 w-icon-nav-menu"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="div-block-48-copy">
        <div class="text-block-23">Payments</div>
        <p class="paragraph">12 hours after your class is completed, you will be paid through your registered email using PayPal. All of your payments will be recorded here. Remember that TutorPal takes a small 10% fee per payment.</p>
      </div>
        <div v-for="session in paymentfinished" :key="session.id" id="paid">
          <div class="div-block-64">
            <div class="text-block-43"><strong class="bold-text-7">Status:</strong> Paid</div>
            <div class="text-block-43"><strong class="bold-text-8">Amount: </strong>${{session.price}}</div>
            <div class="text-block-43"><strong class="bold-text-10">Student:</strong> {{session.student !== undefined ? session.student.user.firstName : ''}} {{session.student !== undefined ? session.student.user.lastName : ''}}</div>
            <div class="text-block-43"><strong class="bold-text-10">Class Date:</strong> {{session.date}}</div>
            <div class="text-block-43"><strong class="bold-text-10">Time: </strong>{{convertTime(session.timeStart)}} - {{convertTime(session.timeEnd)}}</div>
          </div>
        </div>
      <div class="div-block-48-copy">
        <div class="text-block-23">Unpaid Classes (student)</div>
        <p class="paragraph">You are not required to start the class until your student has paid for it.</p>
      </div>
      <div v-for="session in paymentpending" :key="session.id" id="unpaid">
        <div class="div-block-64">
          <div class="text-block-43"><strong class="bold-text-7">Status:</strong> Unpaid</div>
          <div class="text-block-43"><strong class="bold-text-8">Amount: </strong>${{session.price}}</div>
          <div class="text-block-43"><strong class="bold-text-10">Student:</strong> {{session.student !== undefined ? session.student.user.firstName : ''}} {{session.student !== undefined ? session.student.user.lastName : ''}}</div>
          <div class="text-block-43"><strong class="bold-text-10">Class Date:</strong> {{session.date}}</div>
          <div class="text-block-43"><strong class="bold-text-10">Time: </strong>{{convertTime(session.timeStart)}} - {{convertTime(session.timeEnd)}}</div>
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

export default {
  data(){
    return {clicked:false} 
  },
  async fetch() {
    await this.fetchSessions('upcoming')
    await this.fetchUser()
  },
  async created(){
    await this.fetchSessions('pendingOnStudentPayment')
  },
  head() {
    return {
      title: 'My Payments',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/tutor/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:'/tutor/css/tutor-main.webflow.css' },
        { rel:"stylesheet", type:"text/css", href:"/tutor/css/normalize.css" },
      ]
    }
  },
  computed: {
    ...mapGetters({ user: 'getUser', paymentpending: 'getPendingOnStudentPayment', paymentfinished: 'getUpcoming', }),
    logout() {
        return {
          display: this.clicked ? "flex" : "none"
        }
    },
  },
  methods: {
    ...mapGetters(['getUser', 'getPendingOnStudentPayment', 'getUpcoming']),
    ...mapActions(['fetchUser', 'fetchSessions']),
    convertTime,
    logoutclick(){
      this.clicked = !this.clicked
    }
  },
}
</script>
<style>
</style>
