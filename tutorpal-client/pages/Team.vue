<template>
  <client-only>
    <html
      data-wf-page="5f3c2694b3e9866a68ad2a10"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="/main/css/homepage-12.webflow.css" media="none" onload="if(media!='all')media='all'">
      </head>
      <body>
          <div class="homediv-block-3">
            <router-link
              style="margin-top: 0px; margin-bottom: -30px"
              to="/"
              class="homelink-block w-inline-block"
              ><img
                src="../static/student/images/logo.jpg"
                width="250"
                alt=""
                class="homeimage"
            /></router-link>
            <div class="homediv-block-4"><router-link to="/login" class="homelink-2-copy">login</router-link></div><router-link to="/register" class="homebutton w-button">register</router-link></div>
          <div data-w-id="f0d0fabc-c4a9-309e-3cfe-1d2993a9c551" class="homediv-block-24">
          <img 
            src="../static/student/images/team_pic.jpg" 
            loading="lazy" 
            width="639" 
            srcset="../static/student/images/team_pic.jpg 500w, ../static/student/images/team_pic.jpg 800w" 
            class="homeimage-13"
          >
          </div>
          <p class="homeparagraph-8">Our members in the team are Parth Saxena, Sarosh Thalappil, and Pratham Saxena.</p>
            <h1 class="Sarosh_name"> Sarosh Thalappil </h1>
            <p class="homeparagraph-Sa"> Sarosh Thalappil is a co-founder and one of the developers of the TutorPal platform, currently a 10th grader attending Scripps Ranch High School with programming knowledge in Python, HTML, and more.  </p>
            <h1 class="Parth_name"> Parth Saxena </h1>
             <p class="homeparagraph-Pa"> Co-founder Parth Saxena, a 8th grader at Thurgood Marshall Middle School with a background in Python, JavaScript, CSS, HTML, and more, is accompanying Sarosh in the development of the TutorPal platform. </p>
            <h1 class="Pratham_name"> Pratham Saxena </h1>
             <p style="padding-bottom: 60px" class="homeparagraph-Pra">Pratham Saxena is a co-founder, the website content manager, designer, the testing lead, and marketing lead for the TutorPal platform. He is currently a senior at SRHS and has a programming background in Java, C#, JavaScript, CSS, and HTML. Pratham is very interested in STEM, mainly in engineering and computer science. He has prior knowledge in mechanical engineering, CAD design, computer science, and is currently learning the basics of electrical engineering and marketing. Currently, Pratham volunteers as a high school coach for Thurgood Marshall Science Olympiad and is participating in the robotics competition RoboSub, RobotX, FIRST Robotics Challenge, and more with complete devotion. In his spare time, Pratham likes to swim and to spend time with his family and friends!</p>
      </body>
    </html>
  </client-only>
</template>
<script>
export default {
  head() {
    return {
      title: 'Our team',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
        { rel:"stylesheet", type:"text/css", href: "/student/css/student-main.webflow.css" },
      ]
    }
  },
}
</script>
