<template>
  <client-only>
    <html
      data-wf-page="5f5844923df4f0c1c6587323"
      data-wf-site="5f5844923df4f032aa587322"
    >
      <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
      </head>
      <div style="font-family: Poppins; padding: 8px; font-size:24px; background-color: #41a8d3" id="scroll-container">
        <div style="height: 100%; white-space: nowrap; color: white; " id="scroll-text"><strong>{{message}}</strong></div>
      </div>
      <div style="margin-top: 0px;" class="homesection-2">
        <div class="homediv-block-5">
          <div class="homediv-block-3-copy">
            <div class="homediv-block-4">
              <router-link to="/login" class="homelink-2">login</router-link>
            </div>
            <router-link to="/register" class="homebutton w-button">register</router-link>
          </div>
          <h1 class="homeheading">
            Find tutors around the globe,<br />in an instant.
          </h1>
          <div class="homestuff w-form">
            <img
              src="../static/student/images/search-1.png"
              loading="lazy"
              width="25"
              height="25"
              srcset="
                ../static/student/images/search-1.png 500w,
                ../static/student/images/search-1.png       512w
              "
              sizes="(max-width: 767px) 25px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw"
              alt=""
              class="homeimage-2"
            /><input
                class="homesearch-3 w-input"
                placeholder="Search by subject"
                id="search"
                v-model="q"
                @keyup.enter="submitSearch()"
            />
          </div>
        </div>
      </div>
      <div
        data-w-id="fcb88f42-41a3-67cf-c3d6-d08c30f1625c"
        class="homecolumns w-row"
      >
        <div class="homecolumn-7 w-col w-col-2">
          <div class="homediv-block-11">
            <img
              src="../static/student/images/notes.png"
              loading="lazy"
              width="70"
              alt=""
              class="homeimage-10"
            />
            <div class="hometext-block-2">HOMEWORK <br />HELP</div>
          </div>
        </div>
        <div class="homecolumn-6 w-col w-col-2">
          <div class="homediv-block-11">
            <img
              src="../static/student/images/trophy.png"
              loading="lazy"
              width="70"
              srcset="
                ../static/student/images/trophy-p-500.png 500w,
                ../static/student/images/trophy.png         512w
              "
              sizes="70px"
              alt=""
              class="homeimage-9"
            />
            <div class="hometext-block-2">COMPETITION <br />PREP</div>
          </div>
        </div>
        <div class="homecolumn-5 w-col w-col-2">
          <div class="homediv-block-11">
            <img
              src="../static/student/images/files-and-folders.png"
              loading="lazy"
              width="70"
              alt=""
              class="homeimage-8"
            />
            <div class="hometext-block-2">PROFESSIONAL<br />TUTORS</div>
          </div>
        </div>
        <div class="homecolumn-2 w-col w-col-2">
          <div class="homediv-block-11">
            <img
              src="../static/student/images/student.png"
              loading="lazy"
              width="70"
              alt=""
              class="homeimage-6"
            />
            <div class="hometext-block-2">FLEXIBLE <br />SCHEDULES</div>
          </div>
        </div>
        <div class="homecolumn-3 w-col w-col-2">
          <div class="homediv-block-11">
            <img
              src="../static/student/images/school.png"
              loading="lazy"
              width="70"
              srcset="
                ../static/student/images/school-p-500.png 500w,
                ../static/student/images/school.png       512w
              "
              sizes="70px"
              alt=""
              class="homeimage-5"
            />
            <div class="hometext-block-2">INSTANT<br />CLASSES</div>
          </div>
        </div>
        <div class="homecolumn-4 w-col w-col-2">
          <div class="homediv-block-11">
            <img
              src="../static/student/images/research.png"
              loading="lazy"
              width="70"
              srcset="
                ../static/student/images/research-p-500.png 500w,
                ../static/student/images/research.png       512w
              "
              sizes="70px"
              alt=""
              class="homeimage-7"
            />
            <div class="hometext-block-2">LEARN NEW TOPICS ONLINE</div>
          </div>
        </div>
      </div>
      <div class="homediv-block-14">
        <h1 style= "padding-bottom: 40px" class="homeheading-4">What makes us so special?</h1>
        <div class="homew-layout-grid grid">
          <div class="homediv-block-15">
            <img
              src="../static/student/images/coin.png"
              loading="lazy"
              width="80"
              srcset="
                ../static/student/images/coin-p-500.png 500w,
                ../static/student/images/coin.png       512w
              "
              sizes="80px"
              alt=""
            />
            <div class="homediv-block-16">
              <h1 class="homeheading-5">Affordability</h1>
              <p style="font-size: 13px " class="homeparagraph-3">
                TutorPal is an affordable service that does not request payment in
                monthly installments. Students simply pay their tutors based on the tutor's hourly rate. You can expect a class for an hour to
                range from $15 to typically $60 or more, depending on the tutor's level of experience in the subject. We do take 5% commission from payments to tutors.<br />
              </p>
            </div>
          </div>
          <div class="homediv-block-15">
            <img
              src="../static/student/images/person.png"
              loading="lazy"
              width="80"
              srcset="
                ../static/student/images/person-p-500.png 500w,
                ../static/student/images/person.png       512w
              "
              sizes="80px"
              alt=""
            />
            <div class="homediv-block-16">
              <h1 class="homeheading-5">Qualified Tutors</h1>
              <p style="font-size: 13px " class="homeparagraph-2">
                The tutoring website offers tutors that can provide their services in a wide range of subjects. 
                 You can expect scholars ranging from high
                school students to college professors. Even currently unemployed people can tutor, 
                based on their background in certain subjects and level of skills. Tutors can earn money on 
                a fixed hourly rate of their choice or receive volunteering hours(This option is available to all).<br />
              </p>
            </div>
          </div>
          <div class="homediv-block-15">
            <img
              src="../static/student/images/ocean.png"
              loading="lazy"
              width="80"
              srcset="
                ../static/student/images/ocean-p-500.png 500w,
                ../static/student/images/ocean.png       512w
              "
              sizes="80px"
              alt=""
            />
            <div class="homediv-block-16">
              <h1 class="homeheading-5">Variety of subjects</h1>
              <p style="font-size: 13px " class="homeparagraph-5">
                The service consists of a varietal of classes, from kindergarten
                mathematics to college level science courses and more, taught by tutors from all
                backgrounds and diversity. It also includes non-academic
                subjects, such as culinary skills, arts and crafts, languages,
                and more.<br />
              </p>
            </div>
          </div>
          <div class="homediv-block-15">
            <img
              src="../static/student/images/gear.png"
              loading="lazy"
              width="80"
              alt=""
            />
            <div class="homediv-block-16">
              <h1 class="homeheading-5">Simple</h1>
              <p style="font-size: 13px " class="homeparagraph-4">
                TutorPal's aesthetic features and functions are designed to be straightforward, simple, and convenient.
                 Our main goal is to prioritize customers’ time into
                learning and educating more with a friendly user interface.<br />
              </p>
            </div>
          </div>
        </div>
      </div>
      
      <div class="homediv-block-19">
        <p class="homeparagraph-6">
          TutorPal is the most reliable tutoring platform, designed to help and
          teach fundamental and advanced subjects or topics for a suitable
          price. The platform has been enhanced to accommodate parental and
          students’ needs in these tough times. We provide a long-lasting
          experience to all our customers. An all-purpose tutoring platform
          designed to enhance personalized meetings between the teacher and
          student. TutorPal provides a straightforward and compatible system to
          promote learning for all age groups. It is not required for tutors to
          contain a degree of any kind but shall show proof of skills. While
          dealing with unemployment, individuals may join as tutors to earn
          income from customers, while performing an excellent job in teaching
          their students.<br /><br />@2020 TutorPal. All rights reserved.<br />Images
          licensed from Adobe Stock<br />Icons made by
          <a href="https://www.flaticon.com/authors/freepik" target="_blank"
            >Freepik</a
          ><br />
        </p>
      </div>
      <a style="position: fixed; bottom: 0px; right: 10px; font-family: Poppins; color: red; text-decoration: none; display: flex; align-items: center; justify-content: center;" href="https://www.youtube.com/channel/UCTbysqe_AM_eY9N3eVpiY6A" target="_blank"><i class="fa fa-youtube-play" style="font-size:36px;"></i><a style="margin-left: 10px; text-decoration: none;">Tutorials</a></a>
      <div class="homefooter-copy" style="position: static">
        <div class="homecolumns-2 w-row">
          <div class="homecolumn-8 w-col w-col-3">
            <router-link to="/bugs" class="homelink-3">Bugs</router-link>
          </div>
          <div class="homecolumn-9 w-col w-col-3">
            <router-link to="/team" class="homelink-3">Team</router-link>
          </div>
          <div class="homecolumn-10 w-col w-col-3">
            <router-link to="/toc" class="homelink-3">Terms of Service</router-link>
          </div>
          <div class="homecolumn-11 w-col w-col-3">
            <router-link to="/feedback" class="homelink-3">User Feedback</router-link>
          </div>
        </div>
      </div>
    </html>
  </client-only>
</template>
<script>
export default {
  data(){
    return {
      q: '',
      message: 'Tune in on Mondays and Wednesdays to join our free Physics and Math Seminars!'
    }
  },
  head() {
    return {
      title: 'Home - TutorPal',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/student-main.webflow.css" }
      ]
    }
  },
  methods: {
    submitSearch() {
      this.$router.push("/search/"+this.q);
    },
  },
  created(){
    const range = ["2:00", "3:00"];
    const value = (new Date().toLocaleTimeString()).substring(0, 4)
    const dayOfWeekName = new Date().toLocaleString(
      'default', {weekday: 'long'}
    );

    /* eslint-disable */
    if(dayOfWeekName === "Sunday"){
      this.message = "Stay tuned in tommorow, because Physics Coach and Tutor, Veer Chopra will be hosting a free Physics seminar, only on Mondays from 2 - 3 pm! Register as a student to join!"
    } 

    if(dayOfWeekName === "Tuesday"){
      this.message = "Stay tuned in tommorow, because MathCounts Coach and Tutor, Anirudh Nayak, will be hosting a free Competitive Math seminar, only on Wednesdays from 2 - 3 pm! Register as a student to join!"
    } 

    if(dayOfWeekName === "Monday"){
      this.message = "Today on TutorPal, Physics Coach and Tutor, Veer Chopra, will be hosting a free Physics (beginner to intermediate) seminar to prepare you for future courses from 2 - 3 pm. Register as a student to join!"
    } 

    if(dayOfWeekName === "Wednesday"){
      this.message = "Today on TutorPal, MathCounts Coach and Tutor, Anirudh Nayak, will be hosting a free Competition Math (intermediate to advanced) seminar to prepare you for future contests from 2 - 3 pm. Register as a student to join!"
    } 

    if (value >= range[0] && value <= range[1] && dayOfWeekName === "Monday"){
      this.message = "A free Physics seminar is IN PROGRESS from 2 - 3 pm by Physics Coach and esteemed tutor, Veer Chopra. Register as a student to join!";
    }
    else if(value >= range[0] && value <= range[1] && dayOfWeekName === "Wednesday"){
      this.message = "A free Competition Math seminar is IN PROGRESS from 2 - 3 pm by Marshall MathCounts Coach and Tutor, Anirudh Nayak, register as a student to join!";
    }

    /* eslint-enable */
  }
}
</script>
<style scoped>
#scroll-container {
  overflow: hidden;
}

#scroll-text {
  /* animation properties */
  -moz-transform: translateX(100%);
  -webkit-transform: translateX(100%);
  transform: translateX(100%);
  
  -moz-animation: my-animation 15s linear infinite;
  -webkit-animation: my-animation 15s linear infinite;
  animation: my-animation 15s linear infinite;
}

/* for Firefox */
@-moz-keyframes my-animation {
  from { -moz-transform: translateX(100%); }
  to { -moz-transform: translateX(-140%); }
}

/* for Chrome */
@-webkit-keyframes my-animation {
  from { -webkit-transform: translateX(100%); }
  to { -webkit-transform: translateX(-140%); }
}

@keyframes my-animation {
  from {
    -moz-transform: translateX(100%);
    -webkit-transform: translateX(100%);
    transform: translateX(100%);
  }
  to {
    -moz-transform: translateX(-140%);
    -webkit-transform: translateX(-140%);
    transform: translateX(-140%);
  }
}
</style>