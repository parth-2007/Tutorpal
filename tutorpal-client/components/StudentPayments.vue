<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
    <body id="body" style="height: 100vh" class="body-3">
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
                  <nav role="navigation" class="nav-menu-3 w-nav-menu"><router-link to="/" aria-current="page" class="nav-link-4 w-nav-link">Explore</router-link><router-link to="/inbox" class="nav-link-4 w-nav-link">Messages</router-link><router-link to="/requests" class="nav-link-4 w-nav-link">Requests</router-link><router-link to="/payments" class="nav-link-4 w-nav-link w--current">Payments</router-link></nav>
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
              <p class="paragraph">These classes have been accepted by your tutor but you have not paid yet. Please make sure to pay for your session before it has started.</p>
            </div>
            <div class="loop">
                <div id="paypending">
                  <div class="i">
                    <div class="div-block-51-copy"><img src="../static/student/images/user-2.png" loading="lazy" width="75" height="75" srcset="../static/student/images/user-2.png 500w, ../static/student/images/user-2.png 512w" sizes="100px" alt="" class="image-15">
                      <p class="paragraph-2"><strong class="bold-text">Schedule<br></strong>First Session: ${date}<br>Tutor: ${tutorname}<br>Duration: ${duration}<br>Amount: <strong class="bold-text-7">${amount}</strong><br>Trial: ${trial}</p>
                    </div>
                    <p class="paragraph-2-copy"><strong class="bold-text">Student Information</strong><br>Description:<strong class="bold-text"> </strong>${description}</p>
                    <div class="text-block-27">You have not paid for this session yet. Please do as soon as possible.</div><router-link to="/pay/id" class="button-10 w-button">Pay Now</router-link>
                  </div>
                </div>
            </div>
            <div class="div-block-65-copy">
              <div class="text-block-23">Paid Classes</div>
              <p class="paragraph">Congratulations! All your work is over, now you can sit back and learn from your professional tutor.</p>
            </div>
            <div id="paid">
              <div class="item-copy">
                <div class="div-block-51-copy"><img src="../static/student/images/user-2.png" loading="lazy" width="75" height="75" srcset="../static/student/images/user-2.png 500w, ../static/student/images/user-2.png 512w" sizes="100px" alt="" class="image-15">
                  <p class="paragraph-2"><strong class="bold-text">Schedule<br></strong>First Session: ${date}<br>Tutor: ${tutorname}<br>Duration: ${duration}<br>Amount: <strong class="bold-text-7">${amount}</strong><br>Trial: ${trial}</p>
                </div>
                <p class="paragraph-2-copy"><strong class="bold-text">Student Information</strong><br>Description:<strong class="bold-text"> </strong>${description}</p>
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

export default {
  head() {
    return {
      show: false,
      title: 'My Payments',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:'/student/css/student-main.webflow.css' },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
        { rel:"stylesheet", type:"text/css", href:"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" },
      ]
    }
  },
  computed: mapGetters({ user: 'getUser' }),
  async created() {
    await this.fetchUser()
  },
  methods: {
    ...mapGetters(['getUser']),
    ...mapActions(['fetchUser']),
  },
}
</script>
<style>

</style>
