
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
        <div class="div-block-55">
            <div class="section"><router-link to="/" aria-current="page" class="link-block w-inline-block w--current"><img src="../static/student/images/logo.jpg" loading="lazy" width="200" srcset="../static/student/images/logo-p-500.jpeg 500w, ../static/student/images/logo-p-800.jpeg 800w, ../static/student/images/logo-p-1080.jpeg 1080w, ../static/student/images/logo.jpg 1432w" sizes="(max-width: 479px) 100vw, (max-width: 767px) 33vw, (max-width: 991px) 25vw, (max-width: 1439px) 20vw, (max-width: 1919px) 15vw, 12vw" alt=""></router-link>
              <div class="div-block-4">
                <form action="search_main.html" class="stuff w-form"><img src="../static/student/images/search-1.png" loading="lazy" width="25" height="25" srcset="../static/student/images/search-1-p-500.png 500w, ../static/student/images/search-1.png 512w" sizes="(max-width: 767px) 20px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw" alt="" class="image-2"><input type="search" class="search-3 w-input" maxlength="256" name="q" placeholder="Search by subject" id="search" required=""><input type="submit" value="Search" class="button-8 _100 _5px-left w-button"></form>
              </div>
            </div>
          </div>
          <div class="div-block-70">
            <div class="div-block-71"><img src="../static/student/images/user-2.png" loading="lazy" width="74" height="74" srcset="../static/student/images/user-2.png 500w, ../static/student/images/user-2.png 512w" sizes="74px" alt="">
              <div class="div-block-72">
                <h1 class="heading-3" id="subjects">Phsx</h1>
                <div class="div-block-68">
                  <div class="text-block-32"><strong id="fullname" class="bold-text-8">Johnny Appleseed</strong></div>
                </div>
              </div>
            </div>
            <p style="padding-top: 20px;" class="paragraph-8"><strong>Degree: </strong><small style="font-size: 14px;" id="degree"></small><br><strong>Birthdate: </strong><small style="font-size: 14px;" id="birthdate"></small><br><strong>Qualification Description: </strong><small id="qualifications" style="font-size: 14px;"></small><br><strong>Education: </strong><small style="font-size: 14px;" id="education"></small><br><strong>Professional Experience:</strong> <small style="font-size: 14px;" id="professional_exp"></small> years<br><strong>Teaching Experience: </strong><small style="font-size: 14px;" id="teaching_exp"></small> years<br><strong>Average Review:</strong> <small style="font-size: 14px;" id="average_reviews"></small> Stars<br><strong>Time taught: </strong><small style="font-size: 14px;" id="hours_taught"></small><br><strong>Occupation: </strong><small style="font-size: 14px" id="occupation"></small><br><strong>Gender: </strong><small style="font-size: 14px;" id="gender"></small><br><strong>Price: </strong><small style="font-size: 14px;" id="price"></small> hourly <br><strong>Bio: </strong><small style="font-size: 14px;" id="bio"></small><br><strong>Course Description: </strong><small style="font-size: 14px;" id="course"></small><br><strong>Availability: </strong><small style="font-size: 14px;" id="availability"></small>
              <div id="linkedin"></div>
            </div>
          <div class="div-block-56">
            <h1 class="heading-11">Reviews</h1>
            <div id="posts">
              <div class="review_bundle">
                <div class="review_item"><img src="tutor/images/user-2.png" loading="lazy" width="40" srcset="tutor/images/user-2.png 500w, tutor/images/user-2.png 512w" sizes="40px" alt="" class="image-12">
                  <div class="text-block-33">${fullname}</div>
                  <div class="text-block-34">Review: <strong>${stars} Stars</strong></div>
                </div>
                <p class="paragraph-9">${description}</p>
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
      title: 'Tutor Profile',
      link: [
        { rel:"stylesheet", type:"text/css", href:"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:'/student/css/student-main.webflow.css' },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
      ]
    }
  },
}
</script>


