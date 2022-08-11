<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
    <head>
      <meta charset="utf-8" />
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" media="print" onload="this.media='all'">
    </head>
    <body>
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
                    class="tutornav-link-4 w-nav-link"
                    >Requests
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
                    class="tutornav-link-4 w-nav-link w--current"
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
           <div style="font-family: Poppins;" class="container">
              <h1 style="margin-top: 20px;">Certificate Generator</h1>
              <p>Claim your credit for volunteering hours here</p>
              <button class="btn btn-outline-primary" @click="download()" >Download</button>
              <div>
                <div ref="certificate">
                  <img ref="image" style="z-index: 0;" height="500" src="../static/tutor/images/certficate.jpg">
                  <h1 style="z-index: 5; margin-top: -280px; width: 760px; text-align: center; font-family: Playfair Display; font-size: 44px;"><strong>{{this.user.firstName}} {{this.user.lastName}}</strong></h1>
                  <p style="z-index: 5; font-size: 16px; margin-top: 130px; margin-left: 162px; font-family: Playfair Display;"><strong>{{month}}</strong></p>
                  <p style="z-index: 5; font-size: 16px; margin-left: 182px; margin-top: -40px; font-family: Playfair Display;"><strong>{{day}}</strong></p>
                  <p style="z-index: 5; font-size: 16px; margin-left: 202px; margin-top: -40px; font-family: Playfair Display;"><strong>{{year}}</strong></p>
                  <p style="z-index: 5; font-size: 26px; margin-left: 208px; margin-top: -110px; font-family: Playfair Display;"><strong>{{hours}}</strong></p>
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
import Jspdf from 'jspdf'
import html2canvas from 'html2canvas'

export default {
  data(){
    return{
      clicked: false,
      day: '',
      month: '',
      year: '',
      hours: '',
    }
  },
  head() {
    return {
      title: 'Tutor Volunteer Hours',
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

  async created() {
    await this.fetchTutor()
    await this.fetchUser()
    let date = new Date()
    date = new Date(date.getTime() - (date.getTimezoneOffset()*60*1000))
    this.hours = this.tutor.freeTutoringGiven.substr(0,2)
    this.day = date.getDate();
    if(this.day < 10){
      this.day = "0" + this.day
    }
    this.month = date.getMonth()+1;
    this.year = date.getFullYear();
    if(this.month < 10){
      this.month = "0" + this.month
    }
  },
  computed: {
    logout() {
      return {
        display: this.clicked ? 'flex' : 'none',
      }
    },
    ...mapGetters({ tutor: 'getTutor' }),
    ...mapGetters({ user: 'getUser' }),
  },
  methods: {
    logoutclick(){
      this.clicked = !this.clicked
    },
    download(){
      const pdf = new Jspdf('l', 'mm', [297, 210]);
      html2canvas(this.$refs.certificate, {
        height: 700
      }).then(function(canvas) {
        const img = canvas.toDataURL();
        pdf.addImage(img,'JPEG',0,0);
        pdf.save("certificate.pdf");
      });
    },
    ...mapActions(['fetchTutor', 'fetchUser']),
  }
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
 
