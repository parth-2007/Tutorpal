<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
    <head>
      <meta charset="utf-8" />
      <link rel="stylesheet" href="/tutor/css/tutor-main.webflow.css" media="none" onload="if(media!='all')media='all'">
    </head>
    <body id="body" style="min-height: 100vh" class="body-2">
      <div id="main">
        <div class="section">
          <router-link to="/" class="link-block w-inline-block"
            ><img
              src="../static/tutor/images/logo.jpg"
              loading="lazy"
              width="260"
              srcset="
                ../static/tutor/images/logo.jpg   500w,
                ../static/tutor/images/logo.jpg   800w,
                ../static/tutor/images/logo.jpg 1080w,
                ../static/tutor/images/logo.jpg         1432w
              "
              sizes="(max-width: 479px) 100vw, (max-width: 767px) 34vw, (max-width: 991px) 25vw, (max-width: 1439px) 21vw, (max-width: 1919px) 15vw, 12vw"
              alt=""
            /></router-link>
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
              <nav role="navigation" class="nav-menu-3 w-nav-menu"><router-link to="/" aria-current="page" class="nav-link-4 w-nav-link">Requests</router-link><router-link to="/inbox" class="nav-link-4 w-nav-link w--current">Messages</router-link><router-link to="/payments" class="nav-link-4 w-nav-link">Payments</router-link></nav>
              <div class="menu-button-2 w-nav-button">
                <div class="icon-2 w-icon-nav-menu"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="div-block-44">
        <div class="div-block-79"><img src="../static/tutor/images/question.png" loading="lazy" width="30" alt=""><a href="mailto:the2tor4u@gmail.com?subject=Website%20Email" class="link-2">Need help? Send us an email</a></div>
        <div class="div-block-48">
          <div class="text-block-23">Messages</div>
          <p class="paragraph">View all of your contacts here on the messages page, click the buttons to reach the chatroom</p>
        </div>
        <div v-for="contact in contacts" :key="contact.id" class="loop">
            <div style="padding-bottom: 5px; padding-top: 5px; " class="item-2">
              <span class="badge">{{contact.unread}}</span>
              <div class="div-block-78">
                <div class="div-block-77"><img style="border-radius: 100px" :src="contact.student !== undefined ? contact.student.user.profilePic: ''" loading="lazy" height="60"  width="60" alt="" class="image-15">
                  <h1 class="heading-12">{{contact.student !== undefined ? contact.student.user.firstName: '' }} {{contact.student !== undefined ? contact.student.user.lastName: ''}}</h1>
                </div><router-link style="margin-right: -10px" :to="'/chat/'+contact.id" class="link-block-3 w-inline-block"><img src="../static/tutor/images/chat.png" loading="lazy" width="40" alt=""></router-link></div>
            </div>
        </div>
      </div>
      </body>
    </html>
  </client-only>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  data(){
    return {clicked:false} 
  },
  async fetch() {
    await this.fetchContacts()
    await this.fetchUser()
  },
  head() {
    return {
      title: 'Inbox',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/main/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/main/css/normalize.css" },
      ]
    }
  },
  computed: { 
    ...mapGetters({ user: 'getUser', contacts: 'getContacts'}),
    logout() {
        return {
          display: this.clicked ? "flex" : "none"
        }
    },
  },
  methods: {
    ...mapActions(['fetchUser', 'fetchContacts']),
    ...mapGetters(['getUser', 'getContacts']),
    logoutclick(){
      this.clicked = !this.clicked
    }
  },
}
</script>
<style scoped>
.badge {
  margin-top: 5px;
  float: right;
  padding: 2px 8px;
  border-radius: 1000px;
  background-color: red;
  color: white;
  font-family: Poppins;
  font-size: 14px;
  margin-right: 15px;
}
</style>