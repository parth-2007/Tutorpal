<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
    <body id="body" style="height: 100vh" class="body-4">
      <div id="main">
        <div class="section"><router-link to="/" class="link-block w-inline-block"><img src="../static/tutor/images/logo.jpg" loading="lazy" width="260" srcset="../static/tutor/images/logo-p-500.jpeg 500w, ../static/tutor/images/logo-p-800.jpeg 800w, ../static/tutor/images/logo-p-1080.jpeg 1080w, ../static/tutor/images/logo.jpg 1432w" sizes="(max-width: 479px) 100vw, (max-width: 767px) 34vw, (max-width: 991px) 25vw, (max-width: 1439px) 21vw, (max-width: 1919px) 15vw, 12vw" alt=""></router-link>
          <div class="div-block-4">
            <div class="div-block-43">
              <div class="name_profile_pic"><img id="image" width="60" height="60" sizes="60px" alt="" class="image-7">
                <div data-hover="" data-delay="0" class="dropdown-3 w-dropdown">
                  <div class="dropdown-toggle-2-copy w-dropdown-toggle">
                    <div id="name" class="text-block-18">John Wick</div>
                    <div class="text-block-20">Tutor</div>
                  </div>
                  <nav class="navigation-dropdown-2 w-dropdown-list">
                    <div class="dropdown-pointer-2">
                      <div style="width: 300px;"  class="dropdown-wrapper-2">
                        <a href="#" id="logout" class="dropdown-link-2 w-inline-block">
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
              <nav role="navigation" class="nav-menu-3 w-nav-menu"><router-link to="/" aria-current="page" class="nav-link-4 w-nav-link">Requests</router-link><router-link to="inbox_tutor.html" class="nav-link-4 w-nav-link">Messages</router-link><router-link to="/payments" class="nav-link-4 w-nav-link w--current">Payments</router-link></nav>
              <div class="menu-button-2 w-nav-button">
                <div class="icon-2 w-icon-nav-menu"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="div-block-48-copy">
        <div class="text-block-23">Payments</div>
        <p class="paragraph">12 hours after your class is completed, you will be paid through your registered email using PayPal. All of your payments will be recorded here.</p>
      </div>
        <div id="paid"></div>
      <div class="div-block-48-copy">
        <div class="text-block-23">Unpaid Classes (student)</div>
        <p class="paragraph">You are not required to start the class until your student has paid for it.</p>
      </div>
    <div id="unpaid"></div>
      </body>
    </html>
  </client-only>
</template>
<script>
export default {
  head() {
    return {
      title: 'My Payments',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/tutor/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:'/tutor/css/tutor-main.webflow.css' },
        { rel:"stylesheet", type:"text/css", href:"/tutor/css/normalize.css" },
      ]
    }
  },
}
</script>
<style>
</style>
