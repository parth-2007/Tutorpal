
<template>
  <client-only>
    <html
      data-wf-page="5f600218af481481a99ffa6a"
      data-wf-site="5f600218af4814e3759ffa69"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <body style="background-color: rgba(65, 168, 211, 0.2); height: 100vh" id="body">
        <div id="main">
          <div class="div-block-55">
            <div class="section"><router-link to="/" aria-current="page" class="link-block w-inline-block w--current"><img src="../static/student/images/logo.jpg" loading="lazy" width="200" srcset="../static/student/images/logo-p-500.jpeg 500w, ../static/student/images/logo-p-800.jpeg 800w, ../static/student/images/logo-p-1080.jpeg 1080w, ../static/student/images/logo.jpg 1432w" sizes="(max-width: 479px) 100vw, (max-width: 767px) 33vw, (max-width: 991px) 25vw, (max-width: 1439px) 20vw, (max-width: 1919px) 15vw, 12vw" alt=""></router-link>
              <div class="div-block-4">
                <form action="search_student.html" class="stuff w-form"><img src="../static/student/images/search-1.png" loading="lazy" width="25" height="25" srcset="../static/student/images/search-1-p-500.png 500w, ../static/student/images/search-1.png 512w" sizes="(max-width: 767px) 20px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw" alt="" class="image-2"><input type="search" class="search-3 w-input" maxlength="256" name="q" placeholder="Search by subject" id="search" required=""><input type="submit" value="Search" class="button-8 _100 _5px-left w-button"></form>
                <div class="div-block-43">
                  <div class="name_profile_pic"><img :src="user.profilePic" id="image" width="60" height="60" sizes="(max-width: 479px) 15vw, (max-width: 767px) 8vw, 60px" alt="" class="image-7">
                    <div data-hover="" data-delay="0" class="dropdown-3 w-dropdown">
                      <div class="dropdown-toggle-2-copy w-dropdown-toggle">
                        <div id="name" class="text-block-18">{{user.firstName}} {{user.lastName}}</div>
                        <div class="text-block-20">Student</div>
                      </div>
                      <nav class="navigation-dropdown-2 w-dropdown-list">
                        <div class="dropdown-pointer-2">
                          <div style="width: 300px;" class="dropdown-wrapper-2">
                            <a id="logout" class="dropdown-link-2 w-inline-block">
                              <div class="nav-content-wrap-2">
                                <div class="dropdown-title-2">Logout</div>
                              </div>
                            </a>
                            <router-link to="/account" class="dropdown-link-2 w-inline-block">
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
                  <nav role="navigation" class="nav-menu-3 w-nav-menu"><router-link to="/" aria-current="page" class="nav-link-4 w-nav-link">Explore</router-link><router-link to="/inbox" class="nav-link-4 w-nav-link w--current">Messages</router-link><router-link to="/requests" class="nav-link-4 w-nav-link">Requests</router-link><router-link to="/payments" class="nav-link-4 w-nav-link">Payments</router-link></nav>
                  <div class="menu-button-2 w-nav-button">
                    <div class="icon-2 w-icon-nav-menu"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="div-block-66">
            <div class="div-block-45"><img src="../static/student/images/question.png" loading="lazy" width="30" alt=""><a href="mailto:the2tor4u@gmail.com?subject=Website%20Email" class="link-2">Need help? Send us an email</a></div>
            <div class="div-block-65">
              <div class="text-block-23">Messages</div>
              <p class="paragraph">View all of your contacts here on the messages page, click the buttons to reach the chatroom</p>
            </div>
            <!-- gets looped here -->
            <div v-for="contact in contacts" :key="contact.id" class="loop">
                <div style="padding-top: 5px; padding-bottom: 5px;" class="i-copy">
                  <div class="div-block-51">
                    <div class="div-block-51-copy"><img :src="contact.tutor !== undefined ? contact.tutor.user.profilePic: ''" loading="lazy"  height="60"  width="60" sizes="100px" alt="" class="image-15">
                      <h1 class="heading-12">{{contact.tutor !== undefined ? contact.tutor.user.firstName: '' }} {{contact.tutor !== undefined ? contact.tutor.user.lastName: ''}}</h1>
                    </div><router-link :to="'/chat/'+contact.id" class="link-block-3 w-inline-block"><img src="../static/student/images/chat.png" loading="lazy" width="40" alt=""></router-link></div>
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

export default {
  head() {
    return {
      title: 'Inbox',
      link: [
        { rel:"stylesheet", type:"text/css", href:"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:'/student/css/student-main.webflow.css' },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
      ]
    }
  },
  async fetch() {
    await this.fetchUser()
    await this.fetchContacts()
  },
  computed: mapGetters({ user: 'getUser', contacts: 'getContacts'}),
  methods: {
    ...mapActions(['fetchUser', 'fetchContacts']),
    ...mapGetters(['getUser', 'getContacts']),
  },
}
</script>


