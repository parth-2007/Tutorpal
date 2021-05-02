<template>
  <no-ssr>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <body>
        <div style="display:none;opacity:0" class="div-block-22">
          <div style="border-radius: 8px; padding-bottom: 20px; height: 550px;" class="div-block-23">
            <div data-w-id="473c235f-1497-5a38-a04b-c345cec6357a" class="div-block-24"><img src="../static/tutor/images/close-1.png" width="20" alt=""></div>
            <h1 class="heading-10">Update Profile</h1>
            <div class="div-block-25">
              <form>
                <div style="margin-top: 15px;" class="mb-3">
                    <label for="emailaddress" class="form-label">Email Address</label>
                    <input type="email" class="form-control" id="emailaddress" required>
                  </div>
                  <div class="mb-3">
                    <label for="occupation" class="form-label">Occupation</label>
                    <input class="form-control" id="occupation" required>
                  </div>
                  <div class="mb-3">
                    <label for="subject" class="form-label">Subjects</label>
                    <input class="form-control" id="subject" required>
                  </div>
                  <div class="text-block-5"><b>Class Description</b></div>
                  <textarea style="height:250px;" class="form-control" id="description" rows="3"></textarea>
                    <div style="margin-top: 15px;" class="row">
                      <div class="col">
                        <label for="major" class="form-label">Major</label>
                        <input type="text" class="form-control" id="major" required>
                      </div>
                      <div style="padding-left: 0px;" class="col">
                        <label for="gpa" class="form-label">GPA</label>
                        <input type="number" id="gpa" min=0 max=5 class="form-control">
                      </div>
                      <div style="padding-left: 0px;" class="col">
                        <label for="education" class="form-label">Education</label>
                        <select style="margin-top: 0px;" class="form-select" id="education" aria-label="Default select example">
                          <option selected>Select</option>
                          <option value="1">Highschooler</option>
                          <option value="2">College Student</option>
                          <option value="3">Bachelors</option>
                          <option value="4">Masters</option>
                          <option value="4">PhD</option>
                        </select>
                      </div>
                      <div style="padding-left: 0px;" class="col">
                        <label for="school" class="form-label">School/College</label>
                        <input type="text" class="form-control" id="school" required>
                      </div>
                    </div>
                    <textarea style="height:250px; margin-top: 25px;" class="form-control" placeholder="Extra Information About Your Education" id="educationdescription" rows="3"></textarea>
                    <div style="margin-top: 15px; margin-bottom: 5px;" class="text-block-5"><b>Linkedin Profile Link(Optional)</b></div>
                    <input class="form-control" id="linkedin" placeholder="https://www.linkedin.com/in/johndoe">
                      <div class="row">
                        <div class="col">
                          <textarea style="height:250px; margin-top: 25px;" class="form-control" id="bio" placeholder="Eg. My hobbies are..." rows="3"></textarea>
                        </div>
                        <div style="padding-left: 0px;" class="col">
                          <div style="position: relative; text-align: center;" class="col">
                            <p><input type="file" accept="image/" name="image" id="file" onchange="loadFile(event)" style="display: none;"></p>
                            <label for="file" style="cursor: pointer;"><p><img style="border-radius:400px" src="../static/tutor/images/user-2.png" id="output" width="250" height="250"/></p></label>
                            <label style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);" class="form-label">Upload</label>
                          </div>
                        </div>
                      </div>
                      <label style="margin-top: 15px;" for="rates" id="pricedisplay" class="form-label">Pricing: $500</label>
                      <input type="range" min=0 max=1000 class="form-range" id="rates">
                      <div style="margin-top: 15px;" class="row">
                        <div class="col">
                          <label for="teachexp" class="form-label">Years of Teaching Experience</label>
                          <input type="number" id="teachexp" min=0 max=30 class="form-control">
                        </div>
                        <div style="padding-left: 0px;" class="col">
                          <label for="profexp" class="form-label">Years of Professional Experience</label>
                          <input id="profexp" type="number" min=0 max=30 class="form-control">
                        </div>
                      </div>
                      <label style="margin-top: 15px;" for="availability" class="form-label">Availability</label>
                      <input class="form-control" id="availability" placeholder="Mondays, 4:00 PM - 6:00 PM">
                      <label style="margin-top: 15px;" for="password" class="form-label">Verify Password</label>
                      <input type="password" class="form-control" id="password" required>
                    <button style="margin-top: 15px; font-family: Poppins;margin-left: 20px;" class="btn btn-primary">Update Profile</button>
              </form>
            </div>
          </div>
        </div>
        <div>
          <div class="section"><router-link to="/" class="link-block w-inline-block"><img src="../static/tutor/images/logo.jpg" loading="lazy" width="260" srcset="../static/tutor/images/logo-p-500.jpeg 500w, ../static/tutor/images/logo-p-800.jpeg 800w, ../static/tutor/images/logo-p-1080.jpeg 1080w, ../static/tutor/images/logo.jpg 1432w" sizes="(max-width: 479px) 100vw, (max-width: 767px) 34vw, (max-width: 991px) 25vw, (max-width: 1439px) 21vw, (max-width: 1919px) 15vw, 12vw" alt=""></router-link>
            <div class="div-block-4">
              <div class="div-block-43">
                <div class="name_profile_pic"><img id="image" width="60" height="60" sizes="60px" alt="" class="image-7">
                  <div data-hover="" data-delay="0" class="dropdown-3 w-dropdown">
                    <div class="dropdown-toggle-2-copy w-dropdown-toggle">
                      <div id="name" class="text-block-18"></div>
                      <div class="text-block-20">Tutor</div>
                    </div>
                    <nav class="navigation-dropdown-2 w-dropdown-list">
                      <div class="dropdown-pointer-2">
                        <div style="width: 300px;" class="dropdown-wrapper-2">
                          <a href="#" id="logout" class="dropdown-link-2 w-inline-block">
                            <div class="nav-content-wrap-2">
                              <div class="dropdown-title-2">Logout</div>
                            </div>
                          </a>
                          <router-link to="account.html" class="dropdown-link-2 w-inline-block">
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
                <nav role="navigation" class="nav-menu-3 w-nav-menu"><router-link href="/" aria-current="page" class="nav-link-4 w-nav-link w--current">Requests</router-link><router-link to="inbox_tutor.html" class="nav-link-4 w-nav-link">Messages</router-link><router-link href="payments.html" class="nav-link-4 w-nav-link">Payments</router-link></nav>
                <div class="menu-button-2 w-nav-button">
                  <div class="icon-2 w-icon-nav-menu"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="div-block-48-copy">
          <div class="text-block-23">Profile</div>
          <p class="paragraph">This is your public profile, all of this information can be viewed by potential students.</p>
        </div>
        <div style="margin-bottom: 20px;" class="columns-5 w-row">
          <div class="column-16 w-col w-col-4"><img id="image2" loading="lazy" width="257" height="257" sizes="(max-width: 479px) 73vw, (max-width: 767px) 257px, (max-width: 991px) 28vw, 257px" alt="" class="image-11"></div>
          <div class="w-col w-col-8">
            <div>
              <h1 class="heading-3">Subject: Stuff</h1>
              <div class="div-block-54">
                <div class="text-block-32"><strong class="bold-text-3">Stuff Stuff </strong></div>
              </div>
              <p style="padding-top: 20px;" class="paragraph-7"><strong>Member since:</strong> 7/12/2020<br><strong>Birth Date: </strong>Its my bday<br><strong>Qualification Description: </strong>Qualifications<br><strong>Education:</strong> Education<br><strong>Working/Subject Experience:</strong> 6 years<br><strong>Teaching Experience: </strong>9 years<br><strong>Average Review:</strong> 10 stars<br><strong>Number of classes taught:</strong> 300<br><strong>Occupation:</strong> SWE<br><strong>Price: </strong>$54 per hour <br><strong>Bio: </strong>I eat cake<br><strong>Course Description: </strong>I teach stuff<br><a href="" target="_blank"><strong>Linkedin Account:</strong> </a></p><a data-w-id="a5b46ff5-ef05-139d-c6c0-4085e3d55ef2"  href="#" class="button-10-copy-copy w-button">Update Information</a></div>
          </div>
        </div>
      </body>
    </html>
  </no-ssr>
</template>
<script>
export default {
  head() {
    return {
      title: 'Account Information',
      link: [
        { rel:"stylesheet", type:"text/css", href:"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" },
        { type:"text/js", href:'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js' },
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
