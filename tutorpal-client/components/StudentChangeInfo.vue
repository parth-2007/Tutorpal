<template>
  <no-ssr>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <body>
        <div :style="updatemodal" class="div-block-22">
          <div style="border-radius: 8px; padding-bottom: 20px; height: 550px;" class="div-block-23">
            <div class="div-block-24"><img @click="updatemodalvalue()" src="../static/student/images/close-1.png" width="20" alt=""></div>
            <h1 style="margin-top: 30px;" class="heading-10">Update Profile</h1>
            <div class="div-block-25">
              <form style="font-family: Poppins; padding-bottom: 20px;">
                  <div class="row">
                    <div class="col">
                      <label for="firstname" class="form-label">First Name</label>
                      <input type="text" class="form-control" id="firstname" aria-label="First name" required>
                    </div>
                    <div style="padding-left: 0px;" class="col">
                      <label for="lastname" class="form-label">Last Name</label>
                      <input type="text" class="form-control" id="lastname" aria-label="Last name" required>
                    </div>
                  </div>
                  <div style="margin-top: 15px;" class="mb-3">
                    <label for="emailaddress" class="form-label">Email Address</label>
                    <input type="email" class="form-control" id="emailaddress" required>
                  </div>
                  <div style="margin-top:15px; float: left;" class="row">
                    <div style="position: relative; text-align: center;" class="col">
                      <p><input type="file" accept="image/*" name="image" id="file" onchange="loadFile(event)" style="display: none;"></p>
                      <label for="file" style="cursor: pointer;"><p><img style="border-radius:400px" id="output" width="100" height="100"/></p></label>
                      <label style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);" class="form-label">Upload</label>
                    </div>
                  </div>
                  <div style="margin-top: 25px;" class="mb-3">
                    <input type="email" class="form-control" id="parentemail" placeholder="Enter Parent Email" required>
                  </div>
                  <div class="form-group row">
                    <label for="birthdate" class="col-2 col-form-label">Birthdate</label>
                    <div class="col-10">
                      <input class="form-control" type="date" id="birthdate" required>
                    </div>
                  </div>
                  <label for="password" class="form-label">Verify Password</label>
                  <input style="margin-bottom: 15px;" type="password" class="form-control" id="password" required>
                  <button class="btn btn-primary">Update Information</button>
                </form>
            </div>
          </div>
        </div>
        <div class="div-block-55">
          <div class="section"><router-link to="/" aria-current="page" class="link-block w-inline-block w--current"><img src="../static/student/images/logo.jpg" loading="lazy" width="200" srcset="../static/student/images/logo-p-500.jpeg 500w, ../static/student/images/logo-p-800.jpeg 800w, ../static/student/images/logo-p-1080.jpeg 1080w, ../static/student/images/logo.jpg 1432w" sizes="(max-width: 479px) 100vw, (max-width: 767px) 33vw, (max-width: 991px) 25vw, (max-width: 1439px) 20vw, (max-width: 1919px) 15vw, 12vw" alt=""></router-link>
            <div class="div-block-4">
              <form action="search_student.html" class="stuff w-form"><img src="../static/student/images/search-1.png" loading="lazy" width="25" height="25" srcset="../static/student/images/search-1-p-500.png 500w, ../static/student/images/search-1.png 512w" sizes="(max-width: 767px) 20px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw" alt="" class="image-2"><input type="search" class="search-3 w-input" maxlength="256" name="q" placeholder="Search by subject" id="search" required=""><input type="submit" value="Search" class="button-8 _100 _5px-left w-button"></form>
              <div class="div-block-43">
                <div class="name_profile_pic"><img id="image" width="60" height="60" sizes="(max-width: 479px) 15vw, (max-width: 767px) 8vw, 60px" alt="" class="image-7">
                  <div data-hover="" data-delay="0" class="dropdown-3 w-dropdown">
                    <div class="dropdown-toggle-2-copy w-dropdown-toggle">
                      <div class="text-block-18">John Wick</div>
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
                          <router-link to="profile.html" class="dropdown-link-2 w-inline-block">
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
                <nav role="navigation" class="nav-menu-3 w-nav-menu"><router-link to="/" aria-current="page" class="nav-link-4 w-nav-link w--current">Explore</router-link><router-link to="inbox_student.html" class="nav-link-4 w-nav-link">Messages</router-link><router-link to="requests.html" class="nav-link-4 w-nav-link">Requests</router-link><router-link to="payments.html" class="nav-link-4 w-nav-link">Payments</router-link></nav>
                <div class="menu-button-2 w-nav-button">
                  <div class="icon-2 w-icon-nav-menu"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="div-block-67">
          <div class="columns-5 w-row">
            <div class="column-16 w-col w-col-4 w-col-small-small-stack w-col-tiny-tiny-stack"><img id="profile" loading="lazy" width="257" height="257" sizes="(max-width: 479px) 100vw, (max-width: 767px) 33vw, (max-width: 991px) 21vw, (max-width: 1439px) 19vw, 250px" alt="" class="image-11"></div>
            <div class="column-17 w-col w-col-8 w-col-small-small-stack w-col-tiny-tiny-stack">
              <div class="div-block-69">
                <h1 class="heading-3">Johnny Appleseed</h1>
                <p class="paragraph-7"><strong>Birth Date: </strong><small id="bday" style="font-size: 14px;"></small><br><strong>Student Email: </strong><small style="font-size: 14px;" id="email"></small><br><strong>Parent Email: </strong><small style="font-size: 14px;" id="parent"></small></p>
                <a @click="updatemodalvalue()" href="#" class="b10 w-button">Update Information</a></div>
            </div>
          </div>
        </div>
      </body>
    </html>
  </no-ssr>
</template>
<script>
export default {
  data(){
    return {clicked:false} 
  },
  head() {
    return {
      show: false,
      title: 'Account Information',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:'/student/css/student-main.webflow.css' },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
        { rel:"stylesheet", type:"text/css", href:"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" },
      ]
    }
  },
  computed: {
    updatemodal() {
      return {
        display: this.clicked ? "flex" : "none"
      }
    }
  },
  methods: {
    updatemodalvalue(){
      this.clicked = !this.clicked
    }
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
