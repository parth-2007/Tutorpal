
<template>
  <client-only>
    <html
      data-wf-page="5f600218af481481a99ffa6a"
      data-wf-site="5f600218af4814e3759ffa69"
    >
      <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="https://www.tutorpal.org/student/css/student-main.webflow.css" media="print" onload="this.media='all'">
      </head>
      <body id="body" style="min-height: 100vh" class="body-3">
        <div id="main">
          <div class="div-block-55">
            <div class="section">
              <router-link to="/" class="link-block-3 w-inline-block"
                ><img
                  src="../static/student/images/logo.jpg"
                  loading="lazy"
                  width="200"
                  srcset="
                    ../static/student/images/logo.jpg  500w,
                    ../static/student/images/logo.jpg  800w,
                    ../static/student/images/logo.jpg 1080w,
                    ../static/student/images/logo.jpg 1432w
                  "
                  sizes="200px"
                  alt=""
              /></router-link>
              <div class="div-block-4">
                <form action="/search" class="stuff w-form">
                  <img
                    src="../static/student/images/search-1.png"
                    loading="lazy"
                    width="25"
                    height="25"
                    srcset="
                      ../static/student/images/search-1-p-500.png 500w,
                      ../static/student/images/search-1.png       512w
                    "
                    sizes="(max-width: 767px) 20px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw"
                    alt=""
                    class="image-2"
                  /><input
                    type="search"
                    class="search-3 w-input"
                    maxlength="256"
                    name="q"
                    placeholder="Search by subject"
                    id="search"
                    required=""
                  /><input
                    type="submit"
                    value="Search"
                    class="button-8 _100 _5px-left w-button"
                  />
                </form>
                <div class="div-block-43">
                  <div class="name_profile_pic">
                    <img
                      :src="user.profilePic"
                      id="image"
                      width="60"
                      height="60"
                      sizes="(max-width: 479px) 15vw, (max-width: 767px) 8vw, 60px"
                      alt=""
                      class="image-7"
                    />
                    <div
                      data-hover=""
                      data-delay="0"
                      class="dropdown-3 w-dropdown"
                    >
                      <div class="dropdown-toggle-2-copy w-dropdown-toggle">
                        <div id="name" class="text-block-18">
                          {{ user.firstName }} {{ user.lastName }}
                        </div>
                        <div class="text-block-20">Student</div>
                      </div>
                      <nav class="navigation-dropdown-2 w-dropdown-list">
                        <div class="dropdown-pointer-2">
                          <div style="width: 300px" class="dropdown-wrapper-2">
                            <a
                              href="#"
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
                      class="nav-link-4 w-nav-link"
                      >Explore</router-link
                    ><router-link to="/inbox" class="nav-link-4 w-nav-link"
                      >Messages
                      <span class="badge">{{ user.unread }}</span> </router-link
                    ><router-link
                      to="/requests"
                      class="nav-link-4 w-nav-link w--current"
                      >Requests</router-link
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
          <div class="div-block-80">
            <h1 style="text-align: center" class="heading-14">
              Pay for your classes
            </h1>
            <p class="paragraph-11">
              Pay here using either PayPal, PayPal Credit, or a Debit/Credit
              card. Your payment will be sent to the tutor, 12 hours after the
              class ends. Information pertaining to the purchase will be sent
              through email. If you are not satisfied with your class, you may
              apply for a refund request.<br />
            </p>
            <div style="margin-left: 20%; margin-right: 20%" ref="paypal"></div>
          </div>
        </div>
      </body>
    </html>
  </client-only>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'
import getCSRF from '../utils/getCSRF'

export default {
  data() {
    return {
      session: [],
      index: '',
    }
  },
  async fetch() {
    const id = parseInt(this.$route.params.id)
    const url = 'https://api.tutorpal.org/sessions/' + id + '/'
    this.session = await fetch(url, {
      credentials: 'include',
    }).then((res) => {
      if (res.status === 500) {
        this.$router.push('/payments')
      }
      return res.json()
    })
    await this.fetchUser()
    if (
      this.session.student_pk !== this.user.studentPk ||
      this.session.student_paid === true ||
      this.session.accepted === false
    ) {
      this.$router.push('/payments')
    }
    this.paymentpending.forEach((x) => {
      if (x.id === id) {
        this.session = x
      }
    })
  },
  head() {
    return {
      title: 'Pay',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/main/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/main/css/normalize.css" },
      ]
    }
  },
  computed: {
    ...mapGetters({
      user: 'getUser',
      paymentpending: 'getPendingOnStudentPayment',
    }),
  },
  async created() {
    await this.fetchSessions('pendingOnStudentPayment')
    await this.fetchSessions('upcoming')
  },
  mounted() {
    const script = document.createElement('script')
    const clientId =
      'AWW16XfjrRH_ES95pba-gKzG2Zf51wsnFT00MqTASBMYetPIoGvo9zjAH2_K5yZ9rW3ssiwGXqsHl1iJ'
    script.src = `https://www.paypal.com/sdk/js?client-id=${clientId}`
    script.addEventListener('load', this.setLoaded)
    document.body.appendChild(script)
  },
  methods: {
    ...mapGetters(['getUser', 'getPendingOnStudentPayment', 'getUpcoming']),
    ...mapActions([
      'fetchUser',
      'fetchSessions',
      'addSession',
      'removeSession',
    ]),
    setLoaded() {
      window.paypal
        .Buttons({
          style: {
            color: 'blue',
            shape: 'pill',
            label: 'pay',
            height: 40,
          },
          createOrder: (data, actions) => {
            return actions.order.create({
              purchase_units: [
                {
                  description: 'Pay for your TutorPal Session',
                  amount: {
                    currency_code: 'USD',
                    value: this.session.price,
                  },
                },
              ],
            })
          },
          onApprove: async (data) => {
            let url = 'https://api.tutorpal.org/capture_order/' + this.$route.params.id + '/'
            const csrfToken = await getCSRF()
            await fetch(url, {
              credentials: 'include',
              method: 'POST',
              headers: {
                'X-CSRFToken': csrfToken.success,
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                order_id: data.orderID,
              }),
            })
            url = 'https://api.tutorpal.org/sessions/' + this.$route.params.id + '/'
            await fetch(url, {
              credentials: 'include',
              method: 'PATCH',
              headers: {
                'X-CSRFToken': csrfToken.success,
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                student_paid: true,
              }),
            })
            this.removeSession([this.session, 'pendingOnStudentPayment'])
            this.addSession([this.session, 'upcoming'])
            this.$router.push('/payments')
          },
          onError: () => {
            alert(
              'Sorry, we had an error with processing the payment. Please try again'
            )
          },
        })
        .render(this.$refs.paypal)
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