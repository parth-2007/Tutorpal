<template>
  <client-only>
    <html
      data-wf-page="5f600218af481481a99ffa6a"
      data-wf-site="5f600218af4814e3759ffa69"
    >
      <head>
        <meta charset="utf-8" />
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
                <div style="margin-left: 0px; padding-left: 0px" class="stuff w-form">
                  <img
                    src="../static/student/images/search-1.png"
                    loading="lazy"
                    width="25"
                    height="25"
                    srcset="
                      ../static/student/images/search-1.png 500w,
                      ../static/student/images/search-1.png       512w
                    "
                    sizes="(max-width: 767px) 25px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw"
                    alt=""
                    class="image-2"
                  /><input
                      class="search-3 w-input"
                      placeholder="Search by subject"
                      id="search"
                      v-model="q"
                      @keyup.enter="submitSearch()"
                  /><input
                    type="submit"
                    value="Search"
                    class="button-8 _100 _5px-left w-button"
                  />
              </div>
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
                      ><router-link
                    to="/seminars"
                    class="tutornav-link-4 w-nav-link"
                    >Seminars
                  </router-link
                    ><router-link
                      to="/requests"
                      class="nav-link-4 w-nav-link w--current"
                      >Requests</router-link
                    ><router-link to="/payments" class="nav-link-4 w-nav-link"
                      >Payments</router-link
                    ><router-link to="/calendar" class="nav-link-4 w-nav-link"
                      >Calendar</router-link>
                    <router-link to="/donations" class="nav-link-4 w-nav-link"
                      >Donate</router-link>
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
      seminar: [],
      index: '',
      q: ''
    }
  },
  async fetch() {
    const id = parseInt(this.$route.params.id)
    this.seminar = await fetch(process.env.API_URL + '/seminars/' + id + '/', {
      credentials: 'include',
    }).then((res) => {
      if (res.status === 500) {
        this.$router.push('/payments')
      }
      return res.json()
    })
    await this.fetchUser()
  },
  head() {
    return {
      title: 'Pay',
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
    ...mapGetters({
      user: 'getUser',
    }),
  },
  mounted() {
    const script = document.createElement('script')
    script.src = 'https://www.paypal.com/sdk/js?client-id=Ae0zJYc6uq0r19vdNLW2TedQ86i7_FTrS7s_3pwgU5ePOXriAibXuXssw_Nbc5jOg7JOUvU4e7q_LkaT&enable-funding=venmo&currency=USD'
    script.addEventListener('load', this.setLoaded)
    document.body.appendChild(script)
  },
  methods: {
    ...mapGetters(['getUser']),
    ...mapActions([
      'fetchUser',
    ]),
    submitSearch() {
      this.$router.push("/search/"+this.q);
    },
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
                  amount: {
                    currency_code: 'USD',
                    value: parseFloat(this.seminar.price), // fix price
                  },
                },
              ],
            })
          },
          onApprove: async (data, actions) => {
            const csrfToken = await getCSRF()
            const respData = await fetch(
              process.env.API_URL + '/seminars/'+this.seminar.id+'/register/',
              {
                method: 'POST',
                credentials: 'include',
                headers: {
                  'X-CSRFToken': csrfToken.success,
                  'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                  order_id: data.orderID,
                }),
              }
            ).then((res) => res.json())
            this.data = respData
            return actions.order.capture().then(function (orderData) {
              console.log(
                'Capture result',
                orderData,
                JSON.stringify(orderData, null, 2)
              )
            })
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