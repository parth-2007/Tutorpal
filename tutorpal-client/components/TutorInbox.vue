<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <body id="body" style="min-height: 100vh" class="tutorbody-2">
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
                    aria-current="page"
                    class="tutornav-link-4 w-nav-link"
                    >Requests</router-link
                  ><router-link
                    to="/inbox"
                    class="tutornav-link-4 w-nav-link w--current"
                    >Messages</router-link
                  ><router-link
                    to="/payments"
                    class="tutornav-link-4 w-nav-link"
                    >Payments</router-link
                  >
                </nav>
                <div class="tutormenu-button-2 w-nav-button">
                  <div class="tutoricon-2 w-icon-nav-menu"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="tutordiv-block-44">
          <div class="tutordiv-block-79">
            <img
              src="../static/tutor/images/question.png"
              loading="lazy"
              width="30"
              alt=""
            /><a
              href="mailto:the2tor4u@gmail.com?subject=Website%20Email"
              class="tutorlink-2"
              >Need help? Send us an email</a
            >
          </div>
          <div class="tutordiv-block-48">
            <div class="tutortext-block-23">Messages</div>
            <p class="tutorparagraph">
              View all of your contacts here on the messages page, click the
              buttons to reach the chatroom
            </p>
          </div>
          <div v-if="contacts.unfetched === undefined">
            <div
              v-for="contact in contacts"
              :key="contact.id"
              class="tutorloop"
            >
              <div
                style="padding-bottom: 5px; padding-top: 5px"
                class="tutoritem-2"
              >
                <span class="tutorbadge">{{ contact.unread }}</span>
                <div class="tutordiv-block-78">
                  <div class="tutordiv-block-77">
                    <img
                      style="border-radius: 100px"
                      :src="
                        contact.student !== undefined
                          ? contact.student.user.profilePic
                          : ''
                      "
                      loading="lazy"
                      height="60"
                      width="60"
                      alt=""
                      class="tutorimage-15"
                    />
                    <h1 class="tutorheading-12">
                      {{
                        contact.student !== undefined
                          ? contact.student.user.firstName
                          : ''
                      }}
                      {{
                        contact.student !== undefined
                          ? contact.student.user.lastName
                          : ''
                      }}
                    </h1>
                  </div>
                  <router-link
                    style="margin-right: -10px"
                    :to="'/chat/' + contact.id"
                    class="tutorlink-block-3 w-inline-block"
                    ><img
                      src="../static/tutor/images/chat.png"
                      loading="lazy"
                      width="40"
                      alt=""
                  /></router-link>
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

export default {
  data() {
    return { clicked: false }
  },
  async fetch() {
    await this.fetchContacts()
    await this.fetchUser()
  },
  head() {
    return {
      title: 'Inbox',
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
    ...mapGetters({ user: 'getUser', contacts: 'getContacts' }),
    logout() {
      return {
        display: this.clicked ? 'flex' : 'none',
      }
    },
  },
  methods: {
    ...mapActions(['fetchUser', 'fetchContacts']),
    ...mapGetters(['getUser', 'getContacts']),
    logoutclick() {
      this.clicked = !this.clicked
    },
  },
}
</script>
<style scoped>
.tutorbadge {
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