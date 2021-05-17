T<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <body>
        <div :style="updateModal" class="div-block-22">
          <div
            style="
              border-radius: 8px;
              padding-bottom: 20px;
              height: 550px;
              font-family: Poppins;
            "
            class="div-block-23"
          >
            <div class="div-block-24">
              <img
                @click="updateModalValue()"
                src="../static/tutor/images/close-1.png"
                width="20"
                alt=""
              />
            </div>
            <h1 style="margin-top: 30px" class="heading-10">Update Profile</h1>
            <div class="div-block-25">
              <TutorChangeInfoModal @modalSubmit="handleModalSubmit()" />
            </div>
          </div>
        </div>
        <div>
          <div class="section">
            <router-link to="/" class="link-block w-inline-block"
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
                      <div id="name" class="text-block-18">John Wick</div>
                      <div class="text-block-20">Tutor</div>
                    </div>
                    <nav class="navigation-dropdown-2 w-dropdown-list">
                      <div class="dropdown-pointer-2">
                        <div style="width: 300px" class="dropdown-wrapper-2">
                          <a id="logout" class="dropdown-link-2 w-inline-block">
                            <div class="nav-content-wrap-2">
                              <div class="dropdown-title-2">Logout</div>
                            </div>
                          </a>
                          <router-link
                            to="account.html"
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
                    >Requests</router-link
                  ><router-link
                    to="/inbox"
                    class="nav-link-4 w-nav-link"
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
        <div class="div-block-48-copy">
          <div class="text-block-23">Profile</div>
          <p class="paragraph">
            This is your public profile, all of this information can be viewed
            by potential students.
          </p>
        </div>
        <div style="margin-bottom: 20px" class="columns-5 w-row">
          <div class="column-16 w-col w-col-4">
            <img
              id="image2"
              loading="lazy"
              width="257"
              height="257"
              sizes="(max-width: 479px) 73vw, (max-width: 767px) 257px, (max-width: 991px) 28vw, 257px"
              alt=""
              :src="user.profilePic"
              class="image-11"
            />
          </div>
          <div class="w-col w-col-8">
            <div>
              <h1 class="heading-3">Subject: {{ tutor.subjects }}</h1>
              <div class="div-block-54">
                <div class="text-block-32">
                  <strong class="bold-text-3">
                    {{ user.firstName }} {{ user.lastName }}
                  </strong>
                </div>
              </div>
              <p style="padding-top: 20px" class="paragraph-7">
                <!-- <strong>Member since:</strong> 7/12/2020<br /> -->
                <strong>Birth Date: </strong>{{ tutor.birthDate }}<br /><strong
                  >Qualification Description: </strong
                >{{ tutor.qualifications }}<br /><strong>Education:</strong>
                {{ tutor.education }}<br /><strong
                  >Working/Subject Experience:</strong
                >
                {{ tutor.profExp }}<br /><strong>Teaching Experience: </strong>9
                years<br /><strong>Average Review:</strong>
                {{ tutor.averageReviews }}<br /><strong
                  >Number of classes taught:</strong
                >
                {{ tutor.numClasses }}<br /><strong>Occupation:</strong>
                {{ tutor.occupation }}<br /><strong>Price: </strong>${{
                  tutor.rates
                }}
                per hour <br /><strong>Bio: </strong>{{ tutor.bio
                }}<br /><strong>Course Description: </strong
                >{{ tutor.whatYouTeach }}<br />
                <!-- <a
                v-if="tutor.linkedIn.length > 0"
                :href="tutor.linkedIn"
                target="_blank"
                ><strong>Linkedin Account:</strong>
              </a> -->
                <a
                  @click="updateModalValue"
                  class="button-10-copy-copy w-button"
                  >Update Information</a
                >
              </p>
            </div>
          </div>
        </div>
      </body>
    </html>
  </client-only>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'
import TutorChangeInfoModal from './TutorChangeInfoModal.vue'
export default {
  components: { TutorChangeInfoModal },
  data() {
    return {
      clicked: false,
    }
  },
  head() {
    return {
      title: 'Account Information',
      link: [
        { rel: 'stylesheet', type: 'text/css', href: '/tutor/css/webflow.css' },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/tutor/css/tutor-main.webflow.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/tutor/css/normalize.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href:
            'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css',
        },
      ],
    }
  },
  computed: {
    updateModal() {
      return {
        display: this.clicked ? 'flex' : 'none',
      }
    },
    ...mapGetters({ tutor: 'getTutor' }),
    ...mapGetters({ user: 'getUser' }),
  },
  async created() {
    await this.fetchTutor()
    await this.fetchUser()
  },
  methods: {
    updateModalValue() {
      this.clicked = !this.clicked
    },
    async handleModalSubmit() {
      this.updateModalValue()
      await this.fetchTutor()
      await this.fetchUser()
    },
    ...mapActions(['fetchTutor', 'fetchUser']),
  },
}
</script>
<style>
.div-block-22 {
  position: fixed;
  z-index: 21;
  width: 100vw;
  display: none;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.3);
  -o-object-fit: contain;
  object-fit: contain;
}
</style>
