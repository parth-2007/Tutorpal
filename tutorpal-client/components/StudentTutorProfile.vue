
<template>
  <client-only>
    <html
      data-wf-page="5f600218af481481a99ffa6a"
      data-wf-site="5f600218af4814e3759ffa69"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <body>
        <div id="main">
          <div :style="updatemodal" class="div-block-22-copy">
            <div style="border-radius: 8px; padding-bottom: 20px; height: 600px;" class="div-block-23">
              <div class="div-block-24"><img @click="updatemodalvalue()" src="../static/student/images/close-1.png" width="20" alt=""></div>
              <h1 class="heading-10">Schedule a Class</h1>
              <div class="div-block-25">
                <form id="form-wrapper" style="font-family: Poppins;">
                  <div class="form-group row">
                    <label for="date-time" class="col-2 col-form-label">Date and Start Time</label>
                    <div class="col-10">
                      <input class="form-control" type="datetime-local" id="date-time" required>
                    </div>
                    <label for="date-time" class="col-2 col-form-label">Duration in Minutes</label>
                    <div class="col-10">
                      <input type="number" id="duration" class="form-control" required>
                    </div>
                  </div> 
                  <textarea style="height:250px; margin-top: 25px; margin-bottom: 15px;" class="form-control" id="classdescription" placeholder="Describe what you want to learn, cover, or what you need help with." rows="3" required></textarea>
                  <div style="margin-top: 15px; margin-bottom: 15px;" class="form-check">
                    <input class="form-check-input" nam="checkbox" type="checkbox" id="trial">
                    <label class="form-check-label" for="trial">
                      I want this class to be a trial class
                    </label>
                  </div>
                  <button class="btn btn-primary" name="session">Send request</button>
                </form>
              </div>
            </div>
          </div>
          <div class="div-block-55">
            <div class="section"><router-link to="/" aria-current="page" class="link-block w-inline-block w--current"><img src="../static/student/images/logo.jpg" loading="lazy" width="200" srcset="../static/student/images/logo-p-500.jpeg 500w, ../static/student/images/logo-p-800.jpeg 800w, ../static/student/images/logo-p-1080.jpeg 1080w, ../static/student/images/logo.jpg 1432w" sizes="(max-width: 479px) 100vw, (max-width: 767px) 33vw, (max-width: 991px) 25vw, (max-width: 1439px) 20vw, (max-width: 1919px) 15vw, 12vw" alt=""></router-link>
              <div class="div-block-4">
                <form action="search_student.html" class="stuff w-form"><img src="../static/student/images/search-1.png" loading="lazy" width="25" height="25" srcset="../static/student/images/search-1-p-500.png 500w, ../static/student/images/search-1.png 512w" sizes="(max-width: 767px) 20px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw" alt="" class="image-2"><input type="search" class="search-3 w-input" maxlength="256" name="q" placeholder="Search by subject" id="search" required=""><input type="submit" value="Search" class="button-8 _100 _5px-left w-button"></form>
                <div class="div-block-43">
                  <div class="name_profile_pic"><img src="../static/student/images/user-2.png" width="60" height="60" srcset="../static/student/images/user-2.png 500w, ../static/student/images/user-2.png 512w" sizes="(max-width: 479px) 15vw, (max-width: 767px) 8vw, 60px" alt="" class="image-7">
                    <div data-hover="" data-delay="0" class="dropdown-3 w-dropdown">
                      <div class="dropdown-toggle-2-copy w-dropdown-toggle">
                        <div id="name" class="text-block-18">John wick</div>
                        <div class="text-block-20">Student</div>
                      </div>
                      <nav class="navigation-dropdown-2 w-dropdown-list">
                        <div class="dropdown-pointer-2">
                          <div class="dropdown-wrapper-2">
                            <a class="dropdown-link-2 w-inline-block">
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
                  <nav role="navigation" class="nav-menu-3 w-nav-menu"><router-link to="/" aria-current="page" class="nav-link-4 w-nav-link">Explore</router-link><router-link to="/inbox" class="nav-link-4 w-nav-link">Messages</router-link><router-link to="/requests" class="nav-link-4 w-nav-link">Requests</router-link><router-link to="/payments" class="nav-link-4 w-nav-link">Payments</router-link></nav>
                  <div class="menu-button-2 w-nav-button">
                    <div class="icon-2 w-icon-nav-menu"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="div-block-70">
            <div class="div-block-71"><img src="../static/student/images/user-2.png" loading="lazy" width="74" height="74" srcset="../static/student/images/user-2.png 500w, ../static/student/images/user-2.png 512w" sizes="74px" alt="">
              <div class="div-block-72">
                <h1 class="heading-3" id="subjects">Mothematics</h1>
                <div class="div-block-68">
                  <div class="text-block-32"><strong id="fullname" class="bold-text-8">Johnny Appleseed</strong></div>
                </div>
              </div>
            </div>
            <p style="padding-top: 20px;" class="paragraph-8"><strong>Degree: </strong><small style="font-size: 14px;" id="degree"></small><br><strong>Birthdate: </strong><small style="font-size: 14px;" id="birthdate"></small><br><strong>Qualification Description: </strong><small id="qualifications" style="font-size: 14px;"></small><br><strong>Education: </strong><small style="font-size: 14px;" id="education"></small><br><strong>Professional Experience:</strong> <small style="font-size: 14px;" id="professional_exp"></small> years<br><strong>Teaching Experience: </strong><small style="font-size: 14px;" id="teaching_exp"></small> years<br><strong>Average Review:</strong> <small style="font-size: 14px;" id="average_reviews"></small> Stars<br><strong>Time taught: </strong><small style="font-size: 14px;" id="hours_taught"></small><br><strong>Occupation: </strong><small style="font-size: 14px" id="occupation"></small><br><strong>Gender: </strong><small style="font-size: 14px;" id="gender"></small><br><strong>Price: </strong><small style="font-size: 14px;" id="price"></small> hourly <br><strong>Bio: </strong><small style="font-size: 14px;" id="bio"></small><br><strong>Course Description: </strong><small style="font-size: 14px;" id="course"></small><br><strong>Availability: </strong><small style="font-size: 14px;" id="availability"></small>
              <div id="linkedin"></div>
              <a @click="updatemodalvalue()" class="button-9 w-button">Schedule a class</a>
              <router-link style="margin-left: 20px;" to="/chat/tutorid" class="button-9 w-buttion">Send a message</router-link>
          </div>  
          <!-- if already taken class -->
          <div class="div-block-56">
            <div class="div-block-73">
              <h1 style="font-size: 18px;" class="heading-11">Post a review</h1>
              <div class="div-block-74">
                <form class="from-group">
                  <select style="margin-top: 0px;" class="form-select" id="stars" aria-label="Default select example" required>
                    <option value="1">1 Star</option>
                    <option value="2">2 Stars</option>
                    <option value="3">3 Stars</option>
                    <option value="4">4 Stars</option>
                    <option selected value="5">5 Stars</option>
                  </select>
                  <textarea style="height:250px; margin-top: 20px; margin-bottom: 20px;" class="form-control" id="description" placeholder="Enter Description" rows="3" required></textarea>
                  <button class="btn btn-primary" name="review">Post Review</button>
                </form>
              </div>
            </div>
            <h1 class="heading-11">Reviews</h1>
                <div id="posts"></div>
          </div>
        </div>
      </body>
    </html>
  </client-only>
</template>
<script>
export default {
  data(){
    return {clicked:false} 
  },
  head() {
    return {
      title: 'Home',
      link: [
        { rel:"stylesheet", type:"text/css", href:"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:'/student/css/student-main.webflow.css' },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
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
.div-block-22-copy {
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