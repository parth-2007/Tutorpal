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
          <p class="homeparagraph-8">The members in the TutorPal team are Parth Saxena, Sarosh Thalappil, and Pratham Saxena.</p>
            <h1 class="Sarosh_name"> Sarosh Thalappil </h1>
            <img width="250" style="margin-left: 60px;" src="../static/student/images/sarosh.png"/>
            <p class="homeparagraph-Sa"> Sarosh Thalappil is a co-founder and one of the developers of the TutorPal platform, working on the backend of Tutorpal and frontend logic. He is currently a 10th grader attending Scripps Ranch High School with programming knowledge in Python, Django, HTML, Javascript, Vue.js, and other frameworks. He is interested in programming and wants to study computer science.</p>
            <h1 class="Parth_name"> Parth Saxena </h1>
            <img width="250" style="margin-left: 60px;" src="../static/student/images/parth.png"/>
             <p class="homeparagraph-Pa">Parth is a co-founder of TutorPal and is also one of the developers of the platform. He has had prior knowledge in Python, Javascript, HTML, CSS, and several other frameworks that have helped him in this pleasant journey. He is currently an 8th grader at Marshall Middle School and has always had a passion for STEM and programming. He particpates in other activities, like Scioly, Mathcounts, FTC, and more. In his free time, he enjoys watching TV, playing sports, and spending time with friends/family. He is an avid comic reader and Rock 'n' Roll fan. His message to future students and tutors using this platform is to never stop growing, improving, and grinding.</p>
            <h1 class="Pratham_name"> Pratham Saxena </h1>
            <img width="250" style="margin-left: 60px;" src="../static/student/images/pratham.png"/>
             <p style="padding-bottom: 60px" class="homeparagraph-Pra">Pratham Saxena is a co-founder, the website content manager, the testing and marketing lead for the TutorPal platform. He is currently a senior at SRHS and has a programming background in Java, C#, JavaScript, CSS, and HTML. Pratham is very interested in STEM, mainly in engineering and computer science. He has prior knowledge in mechanical engineering, CAD design, computer science, and is currently learning the basics of electrical engineering and marketing. Currently, Pratham volunteers as a high school coach for Thurgood Marshall Science Olympiad and is participating in the robotics competition RoboSub, RobotX, FIRST Robotics Challenge, and more with complete devotion. In his spare time, Pratham likes to swim and to spend time with his family and friends!</p>
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
