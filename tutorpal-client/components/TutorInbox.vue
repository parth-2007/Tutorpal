<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
    <body id="body" class="body-2">
      <div id="main">
        <div class="section"><router-link to="/" aria-current="page" class="link-block w-inline-block w--current"><img src="../static/tutor/images/logo.jpg" loading="lazy" width="260" srcset="../static/tutor/images/logo-p-500.jpeg 500w, ../static/tutor/images/logo-p-800.jpeg 800w, ../static/tutor/images/logo-p-1080.jpeg 1080w, ../static/tutor/images/logo.jpg 1432w" sizes="(max-width: 479px) 100vw, (max-width: 767px) 34vw, (max-width: 991px) 25vw, (max-width: 1439px) 21vw, (max-width: 1919px) 15vw, 12vw" alt=""></router-link>
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
        <div class="loop">
          <!-- gets looped here -->
            <div style="padding-bottom: 5px; padding-top: 5px; " class="item-2">
              <div class="div-block-78">
                <div class="div-block-77"><img src="../static/tutor/images/user-2.png" loading="lazy" height="60"  width="60" alt="" class="image-15">
                  <h1 class="heading-12">Jane Doe</h1>
                </div><router-link to="/chat/id" class="link-block-3 w-inline-block"><img src="../static/tutor/images/chat.png" loading="lazy" width="40" alt=""></router-link></div>
            </div>
        </div>
      </div>
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
