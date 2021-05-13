<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
    <body id="body" style="margin-bottom: 0px; background-color: rgba(65, 168, 211, 0.2);" class="body-5">
      <div id="main">
            <div class="div-block-55">
              <div class="section"><router-link to="/" aria-current="page" class="link-block w-inline-block w--current"><img src="../static/student/images/logo.jpg" loading="lazy" width="200" srcset="../static/student/images/logo-p-500.jpeg 500w, ../static/student/images/logo-p-800.jpeg 800w, ../static/student/images/logo-p-1080.jpeg 1080w, ../static/student/images/logo.jpg 1432w" sizes="(max-width: 479px) 100vw, (max-width: 767px) 33vw, (max-width: 991px) 25vw, (max-width: 1439px) 20vw, (max-width: 1919px) 15vw, 12vw" alt=""></router-link>
                <div class="div-block-4">
                  <form action="search_student.html" class="stuff w-form"><img src="../static/student/images/search-1.png" loading="lazy" width="25" height="25" srcset="../static/student/images/search-1-p-500.png 500w, ../static/student/images/search-1.png 512w" sizes="(max-width: 767px) 20px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw" alt="" class="image-2"><input type="search" class="search-3 w-input" maxlength="256" name="q" placeholder="Search by subject" id="search" required=""><input type="submit" value="Search" class="button-8 _100 _5px-left w-button"></form>
                  <div class="div-block-43">
                    <div class="name_profile_pic"><img id="image" width="60" height="60" sizes="(max-width: 479px) 15vw, (max-width: 767px) 8vw, 60px" alt="" class="image-7">
                      <div data-hover="" data-delay="0" class="dropdown-3 w-dropdown">
                        <div class="dropdown-toggle-2-copy w-dropdown-toggle">
                          <div id="name" class="text-block-18">John Wick</div>
                          <div class="text-block-20">Student</div>
                        </div>
                        <nav class="navigation-dropdown-2 w-dropdown-list">
                          <div class="dropdown-pointer-2">
                            <div style="width: 300px;" class="dropdown-wrapper-2">
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
          </div>
        </div>
        <iframe style="width: 100vw; height: 87vh;" allow="camera;microphone" :src="'https://meet.jit.si/TutorpalSession'+$route.params.id"></iframe>
      </body>
    </html>
  </client-only>
</template>
<script>
export default {
  head() {
    return {
      title: 'Student Workspace',
      link: [
        { rel: 'stylesheet', type: 'text/css', href: '/student/css/webflow.css' },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/student-main.webflow.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/normalize.css',
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
}

</script>
<style>
  .div-block-80 {
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
</style>
 

