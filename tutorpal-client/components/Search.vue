<template>
  <client-only>
    <html
      data-wf-page="5f5844923df4f0c1c6587323"
      data-wf-site="5f5844923df4f032aa587322"
    >
    <div style="margin-left: 40px; margin-top: 20px;">
    <router-link to="/" class="link-block-3 w-inline-block"><img src="../static/student/images/logo.jpg" loading="lazy" width="200" srcset="../static/student/images/logo.jpg 500w, ../static/student/images/logo.jpg 800w, ../static/student/images/logo.jpg 1080w, ../static/student/images/logo.jpg 1432w" sizes="200px" alt=""></router-link>
    <div class="search">
      <form style="margin-left: 0px; margin-bottom: 40px;" action="search_main.html" class="stuff w-form"><img src="../static/main/images/search-1.png" loading="lazy" width="25" height="25" srcset="../static/main/images/search-1-p-500.png 500w, ../static/main/images/search-1.png 512w" sizes="(max-width: 767px) 25px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw" alt="" class="image-2"><input type="search" class="search-3 w-input" maxlength="256" name="q" placeholder="Search by subject" id="search" required=""><input type="submit" value="Search" class="button-8 _100 _5px-left w-button"></form>
      <div style="margin-bottom: 20px;" id="posts">
        <router-link to="/tutors/id" class="link-block-2 w-inline-block">
            <div class="div-block-54"><img src="../static/student/images/user-2.png" loading="lazy" width="38" height="38" srcset="../static/student/images/user-2.png 500w, ../static/student/images/user-2.png 512w" sizes="38px" alt="" class="image-5">
              <div class="text-block-21"><strong class="bold-text-3">${full_name}</strong></div>
                  <div class="text-block-21-copy">Subject: ${subject}</div>
                  <div class="text-block-21-copy-2">Price: ${price} hourly</div>
                  <div class="text-block-21-copy-2">Degree: ${education}</div>
                  <div class="text-block-21-copy-2">Education: ${major} at ${school}, GPA of ${gpa}</div>
                  <div class="text-block-21-copy-2">Reviews: ${reviews} Stars</div>
                  <div class="text-block-21-copy-2">Occupation: ${occupation}</div>
                  <div style="color: green; font-size: 24px;" class="text-block-21-copy-2"><strong>✓</strong></div>
            </div>
        </router-link>
      </div>
      </div>
    </div>
    </html>
  </client-only>
</template>
<script>

export default {
  head() {
    return {
      title: 'Find a tutor',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:'/student/css/student-main.webflow.css' },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
      ]
    }
  },
}

</script>