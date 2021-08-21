<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
    <head>
      <meta charset="utf-8" />
      <link rel="stylesheet" href="https://www.tutorpal.org/student/css/student-main.webflow.css" media="print" onload="this.media='all'">
    </head>
    <body id="body" style="min-height: 100vh" class="body-3">
        <div id="main">
          <div class="div-block-55">
            <div class="section"><router-link to="/" aria-current="page" class="link-block w-inline-block w--current"><img src="../static/student/images/logo.jpg" loading="lazy" width="200" srcset="../static/student/images/logo-p-500.jpeg 500w, ../static/student/images/logo-p-800.jpeg 800w, ../static/student/images/logo-p-1080.jpeg 1080w, ../static/student/images/logo.jpg 1432w" sizes="(max-width: 479px) 100vw, (max-width: 767px) 33vw, (max-width: 991px) 25vw, (max-width: 1439px) 20vw, (max-width: 1919px) 15vw, 12vw" alt=""></router-link>
              <div class="div-block-4">
                <form action="/search" class="stuff w-form"><img src="../static/student/images/search-1.png" loading="lazy" width="25" height="25" srcset="../static/student/images/search-1-p-500.png 500w, ../static/student/images/search-1.png 512w" sizes="(max-width: 767px) 20px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw" alt="" class="image-2"><input type="search" class="search-3 w-input" maxlength="256" name="q" placeholder="Search by subject" id="search" required=""><input type="submit" value="Search" class="button-8 _100 _5px-left w-button"></form>
                <div class="div-block-43">
                  <div class="name_profile_pic"><img :src="user.profilePic" id="image" width="60" height="60" sizes="(max-width: 479px) 15vw, (max-width: 767px) 8vw, 60px" alt="" class="image-7">
                    <div data-hover="" data-delay="0" class="dropdown-3 w-dropdown">
                      <div @click="logoutclick()" class="dropdown-toggle-2-copy w-dropdown-toggle">
                        <div id="name" class="text-block-18">{{user.firstName}} {{user.lastName}}</div>
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
              <div data-collapse="none" data-animation="default" data-duration="400" role="banner" class="navbar-2 w-nav">
                <div class="container-2 w-container">
                  <nav role="navigation" class="nav-menu-3 w-nav-menu"><router-link to="/" aria-current="page" class="nav-link-4 w-nav-link">Explore</router-link><router-link to="/inbox" class="nav-link-4 w-nav-link">Messages<span class="badge">{{user.unread}}</span></router-link><router-link to="/requests" class="nav-link-4 w-nav-link">Requests</router-link><router-link to="/payments" class="nav-link-4 w-nav-link w--current">Payments</router-link></nav>
                  <div class="menu-button-2 w-nav-button">
                    <div class="icon-2 w-icon-nav-menu"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="div-block-66">
            <div class="div-block-45"><img src="../static/student/images/question.png" loading="lazy" width="30" alt=""><a href="mailto:the2tor4u@gmail.com?subject=Website%20Email" class="link-2">Need help? Send us an email</a></div>
            <h1 class="heading"><strong>Payment Information</strong></h1>
            <div class="div-block-65">
              <div class="text-block-23">Payments</div>
              <p class="paragraph">These classes have been accepted by your tutor but you have not paid yet. Please make sure to pay for your session before it has started. Remember that you can cancel your class anytime, even after paying.</p>
            </div>
            <div class="loop">
              <div v-for="session in paymentpending" :key="session.id" id="paypending">
                <img @click="canceledHandler(session.id, session, 'pendingOnStudentPayment')" style="margin-top: 10px; cursor: pointer; margin-right: 10px" src="../static/student/images/close-1.png" align="right" width="15" alt=""/>
                <div class="i">
                  <div class="div-block-51-copy"><img :src="session.tutor !== undefined ? session.tutor.user.profilePic:''" loading="lazy" width="75" height="75" sizes="100px" alt="" class="image-15">
                    <p class="paragraph-2"><strong class="bold-text">Schedule<br></strong>First Session: {{session.date}}<br>Tutor: {{session.tutor !== undefined ? session.tutor.user.firstName : ''}} {{session.tutor !== undefined ? session.tutor.user.lastName : ''}}<br>Duration: {{convertTime(session.timeStart)}} - {{convertTime(session.timeEnd)}}
                    <br>Amount: <strong class="bold-text-7">${{session.price}}</strong><br>Trial: {{session.free}}</p>
                  </div>
                  <p class="paragraph-2-copy"><strong class="bold-text">Student Information</strong><br>Description: <strong class="bold-text"> </strong>{{session.description}}</p>
                  <div class="text-block-27">You have not paid for this session yet. Please do as soon as possible.</div><router-link :to="'/pay/'+session.id" class="button-10 w-button">Pay Now</router-link>
                </div>
              </div>
            </div>
            <div class="div-block-65-copy">
              <div class="text-block-23">Paid Classes</div>
              <p class="paragraph">Congratulations! All your work is over, now you can sit back and learn from your professional tutor.</p>
            </div>
            <div v-for="session in paymentfinished" :key="session.id" id="paid">
              <img @click="canceledHandler(session.id, session, 'upcoming')" style="margin-top: 10px; cursor: pointer; margin-right: 10px" src="../static/student/images/close-1.png" align="right" width="15" alt=""/>
              <div class="item-copy">
                <div class="div-block-51-copy"><img :src="session.tutor !== undefined ? session.tutor.user.profilePic:''" loading="lazy" width="75" height="75" sizes="100px" alt="" class="image-15">
                  <p class="paragraph-2"><strong class="bold-text">Schedule<br></strong>First Session: {{session.date}}<br>Tutor: {{session.tutor !== undefined ? session.tutor.user.firstName : ''}} {{session.tutor !== undefined ? session.tutor.user.lastName : ''}}<br>Duration: {{convertTime(session.timeStart)}} - {{convertTime(session.timeEnd)}}
                  <br>Amount: <strong class="bold-text-7">${{session.price}}</strong><br>Trial: {{session.free}}</p>
                </div>
                <p class="paragraph-2-copy"><strong class="bold-text">Student Information</strong><br>Description: <strong class="bold-text"> </strong>{{session.description}}</p>
                <div class="text-block-27-copy">Thank you for paying for your session!</div>
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
  data(){
    return {
      clicked:false,
    } 
  },
  async fetch() {
    await this.fetchSessions('upcoming')
  },
  head() {
    return {
      show: false,
      title: 'My Payments',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/main/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/main/css/normalize.css" },
      ]
    }
  },
  computed: {
    logout() {
        return {
          display: this.clicked ? "flex" : "none"
        }
    },
    ...mapGetters({ user: 'getUser', paymentpending: 'getPendingOnStudentPayment', paymentfinished: 'getUpcoming'}),
  },
  async created (){
    await this.fetchSessions('pendingOnStudentPayment')
    await this.fetchUser()
  },
  methods: {
    ...mapGetters(['getUser',  'getPendingOnStudentPayment', 'getUpcoming']),
    ...mapActions(['fetchUser', 'fetchSessions', 'removeSession']),
    convertTime,
    logoutclick(){
      this.clicked = !this.clicked
    },
    async canceledHandler(id, session, sessionType) {
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
        this.removeSession([session, sessionType])
      }
    },
  },
}
</script>
<style scoped>
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