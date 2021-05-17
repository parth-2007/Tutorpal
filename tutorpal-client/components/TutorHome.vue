<template>
  <client-only>
    <html
      data-wf-page="5f5d0db29d3d2a83a01fb34a"
      data-wf-site="5f5d0db29d3d2a6ab81fb349"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <body id="body" style="height: 100%" class="body">
        <div id="main">
          <div class="section">
            <router-link
              to="/"
              aria-current="page"
              class="link-block w-inline-block w--current"
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
                    <div class="dropdown-toggle-2-copy w-dropdown-toggle">
                      <div id="name" class="text-block-18">{{user.firstName}} {{user.lastName}}</div>
                      <div class="text-block-20">Tutor</div>
                    </div>
                    <nav class="navigation-dropdown-2 w-dropdown-list">
                      <div class="dropdown-pointer-2">
                        <div style="width: 300px" class="dropdown-wrapper-2">
                          <a
                            id="logout"
                            class="dropdown-link-2 w-inline-block"
                          >
                            <div class="nav-content-wrap-2">
                              <div class="dropdown-title-2">Logout</div>
                            </div>
                          </a>
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
                    >Requests</router-link
                  ><router-link to="/inbox" class="nav-link-4 w-nav-link"
                    >Messages</router-link
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
          <div class="w-col w-col-8">
            <div class="div-block-44">
              <div class="div-block-45">
                <img
                  src="../static/tutor/images/question.png"
                  loading="lazy"
                  width="30"
                  alt=""
                /><a
                  href="mailto:the2tor4u@gmail.com?subject=Website%20Email"
                  class="link-2"
                  >Need help? Send us an email</a
                >
              </div>
              <h1 class="heading">Student Requests</h1>
              <div class="div-block-48">
                <div class="text-block-23">Inbox</div>
                <p class="paragraph">
                  Please accept or deny these requests based off of your comfort
                  ability.
                </p>
              </div>
              <div v-for="session in requests" :key="session.id" id="inbox" class="loop">
                  <div class="item">
                    <div class="div-block-51"><img :src="session.student !== undefined ? session.student.user.profilePic:''" loading="lazy"  width="60" sizes="64px" alt="" class="image-9"></div>
                    <p style="font-size: 20px; margin-bottom: 15px;" class="paragraph-2">{{session.student !== undefined ? session.student.user.firstName : ''}} {{session.student !== undefined ? session.student.user.lastName : ''}}</p>
                    <p class="paragraph-2"><strong class="bold-text">Class Information<br></strong>First Session: {{session.date}}<br>Duration: {{convertTime(session.timeStart)}} - {{convertTime(session.timeEnd)}}<br>Trial: {{session.free}}<br>Amount: ${{session.price}}</p>
                    <p class="paragraph-2"><strong class="bold-text">Student Information</strong><br>Description: <strong class="bold-text"> </strong>{{session.description}}</p>
                    <div class="text-block-27">Remember, you only have 24 hours from since this request was sent to accept or deny.</div>
                  <div class="div-block-52"><a id="${x}" style="z-index: 5" aria-current="page" class="button-3 w-button w--current">Accept</a><a id="${y}" style="z-index: 5" aria-current="page" class="button-3-copy w-button w--current">Deny</a></div>
                </div>
              </div>
            </div>
          </div>
          <div class="column-15 w-col w-col-4">
            <div style="margin-bottom: 20px" class="div-block-53">
              <h1 class="heading-2">Starting:</h1>
              <div class="upcoming_loop">
                <div v-for="session in started" :key="session.id" id="started">
                  <div class="upcoming_item">
                    <p class="paragraph-3">Date: {{session.date}}<br>Time: {{convertTime(session.timeStart)}} - {{convertTime(session.timeEnd)}}<br>Student: {{session.student !== undefined ? session.student.user.firstName : ''}} {{session.student !== undefined ? session.student.user.lastName : ''}}<br>Subject: {{session.subjects}}<br>Class Description: {{session.description}}‍<br></p><router-link :to="'/sessions/'+session.id" class="button-4 w-button">Join Meeting</router-link>
                  </div>
                </div>
                <div style="text-align: center; padding: 20%" v-if="started=null">
                  <strong style="font-family: Poppins; font-size: 18px;" class="bold-text-2">Your classes have not started yet</strong>
                </div>
              </div>
            </div>
            <div
              style="height: 300px; margin-bottom: 20px"
              class="div-block-53"
            >
            <h1 class="heading-2">Upcoming Classes:</h1>
            <div class="upcoming_loop">
              <div v-for="session in upcoming" :key="session.id" id="upcoming">
                <div class="upcoming_item">
                  <p class="paragraph-3">Date: {{session.date}}<br>Time: {{convertTime(session.timeStart)}} - {{convertTime(session.timeEnd)}}<br>Tutor: {{session.student !== undefined ? session.student.user.firstName : ''}} {{session.student !== undefined ? session.student.user.lastName : ''}}<br>Subject: {{session.subjects}}<br>‍Class Description: {{session.description}}‍<br><strong style="margin-top: 10px;" class="bold-text-2">Don&#x27;t worry if you can&#x27;t keep track of your classes, we send an email 10 minutes prior to the beginning of the class.</strong></p>
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

export default {
  async fetch() {
    await this.fetchSessions('startedSessions')
    await this.fetchSessions('upcoming')
    await this.fetchSessions('pendingOnTutor')
    await this.fetchUser()
  },
  head() {
    return {
      title: 'Home',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/tutor/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:'/tutor/css/tutor-main.webflow.css' },
        { rel:"stylesheet", type:"text/css", href:"/tutor/css/normalize.css" },
      ]
    }
  },
  computed: mapGetters({ user: 'getUser', started: 'getStartedSessions', upcoming: 'getUpcoming', requests: 'getPendingOnTutor' }),
  methods: {
    ...mapActions(['fetchUser', 'fetchSessions', ]),
    ...mapGetters(['getStartedSessions', 'getUpcoming', 'getUser','getPendingOnTutor']),
    convertTime
  },
  // var from = new Date(2020, 11, 17, 0, 0, 0, 0);
  // var check = new Date();
  // if(check.getTime() <= to.getTime() && check.getTime() >= from.getTime()){
  //   console.log("inside")
  // }
  // else{
  //   console.log("outside")
  // }
}
</script>