<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
    <body id="body" style="min-height: 100vh" class="body-4">
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
              <nav role="navigation" class="nav-menu-3 w-nav-menu"><router-link to="/" aria-current="page" class="nav-link-4 w-nav-link">Requests</router-link><router-link to="/inbox" class="nav-link-4 w-nav-link">Messages<span class="badge">{{user.unread}}</span></router-link><router-link to="/payments" class="nav-link-4 w-nav-link w--current">Payments</router-link></nav>
              <div class="menu-button-2 w-nav-button">
                <div class="icon-2 w-icon-nav-menu"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="div-block-48-copy">
        <div class="text-block-23">Payments</div>
        <p class="paragraph">All of your payments for your finished classes will be recorded here.</p>
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
        <p class="paragraph">You are not required to start this class until your student has paid for it.</p>
      </div>
      <div v-for="session in paymentpending" :key="session.id" id="unpaid">
        <div class="div-block-64">
          <div class="text-block-43"><strong class="bold-text-7">Status:</strong> Unpaid</div>
          <div class="text-block-43"><strong class="bold-text-8">Amount: </strong>${{session.price}}</div>
          <div class="text-block-43"><strong class="bold-text-10">Student:</strong> {{session.student !== undefined ? session.student.user.firstName : ''}} {{session.student !== undefined ? session.student.user.lastName : ''}}</div>
          <div class="text-block-43"><strong class="bold-text-10">Class Date:</strong> {{session.date}}</div>
          <div class="text-block-43"><strong class="bold-text-10">Time: </strong>{{convertTime(session.timeStart)}} - {{convertTime(session.timeEnd)}}</div>
          <img @click="canceledHandler(session.id, session)" style="cursor: pointer; margin-left: 25px" src="../static/student/images/close-1.png" align="right" width="15" alt=""/>
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
  data(){
    return {
      clicked:false,
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
        { rel:"stylesheet", type:"text/css", href:"/main/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:'/tutor/css/tutor-main.webflow.css' },
        { rel:"stylesheet", type:"text/css", href:"/main/css/normalize.css" },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href:
            'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css',
        },
      ]
    }
  },
  computed: {
    ...mapGetters({ user: 'getUser', paymentpending: 'getPendingOnStudentPayment', paymentfinished: 'getPastSessions'}),
    logout() {
      return {
        display: this.clicked ? "flex" : "none"
      }
    },
  },
  async created(){
    await this.fetchSessions('pendingOnStudentPayment')
  },
  methods: {
    ...mapGetters(['getUser',  'getPendingOnStudentPayment', 'getPastSessions']),
    ...mapActions(['fetchUser', 'fetchSessions', 'removeSession']),
    convertTime,
    logoutclick(){
      this.clicked = !this.clicked
    },
    async canceledHandler(id, session){
      const x = confirm("Please confirm that you wish to cancel this session.")
      if(x === true){
        const url = 'https://api.tutorpal.org/sessions/'+id+'/'
        const csrfToken = await getCSRF()
        await fetch(url, {
            method: 'PATCH',
            credentials: 'include',
            headers: {
              'X-CSRFToken': csrfToken.success,
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              "canceled": true,
            }),
        })
        this.removeSession([session, 'pendingOnStudentPayment'])
      }
    }
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