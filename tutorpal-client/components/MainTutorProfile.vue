
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
        <div class="div-block-55">
          <div class="section">
            <router-link
              style="margin-top: 0px; margin-bottom: -30px"
              to="/"
              class="link-block w-inline-block"
              ><img
                src="../static/main/images/logo.jpg"
                width="250"
                alt=""
                class="image"
            /></router-link>
            <div class="div-block-4">
              <form action="/search" class="stuff w-form">
                <img
                  src="../static/student/images/search-1.png"
                  loading="lazy"
                  width="25"
                  height="25"
                  srcset="
                    ../static/student/images/search-1-p-500.png 500w,
                    ../static/student/images/search-1.png       512w
                  "
                  sizes="(max-width: 767px) 20px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw"
                  alt=""
                  class="image-2"
                /><input
                  type="search"
                  class="search-3 w-input"
                  name="q"
                  placeholder="Search by subject"
                  id="search"
                  required=""
                /><input
                  type="submit"
                  value="Search"
                  class="button-8 _100 _5px-left w-button"
                />
              </form>
            </div>
          </div>
        </div>
        <div class="div-block-70">
          <p style="padding-top: 20px" class="paragraph-8">
            <strong>Degree: </strong>{{ data.education }}<br /><strong
              >Birthdate: </strong
            >{{ data.birth_date }}<br /><strong
              >Qualification Description: </strong
            >{{ data.qualifications }}<br />
            <strong>Education: </strong>{{ data.major }} at {{ data.school }},
            GPA of {{ data.gpa }}<br /><strong
              >Professional Experience: </strong
            >{{ data.prof_exp }} years<br /><strong
              >Teaching Experience: </strong
            >{{ data.teach_exp }} years<br />
            <strong>Average Review:</strong>
            {{ data.average_reviews }} Stars<br /><strong>Occupation: </strong
            >{{ data.occupation }}<br /><strong>Gender: </strong
            >{{ data.gender }}<br />
            <strong>Price: </strong>${{ data.rates }} hourly <br /><strong
              >Bio: </strong
            >{{ data.bio }}<br /><strong>Course Description: </strong
            >{{ data.what_you_teach }}<br /><strong>Availability: </strong
            >{{ data.availability }} <br /><a
              style="font-family: Poppins"
              :href="data.linkedIn"
              target="_blank"
              ><strong>Linkedin Account:</strong></a
            >
          </p>
        </div>
        <div class="div-block-56">
            <h1 class="heading-11">Reviews</h1>
            <div v-for="review in reviews.results" :key="review.id" id="posts">
              <div class="review_bundle">
                <div class="review_item">
                  <img
                    :src="review.student.user.profile_pic"
                    loading="lazy"
                    width="40"
                    sizes="40px"
                    alt=""
                    class="image-12"
                  />
                  <div class="text-block-33">
                    {{ review.student.user.first_name }}
                    {{ review.student.user.last_name }}
                  </div>
                  <div class="text-block-34">
                    Review: <strong>{{ review.stars }} Stars</strong>
                  </div>
                </div>
                <p class="paragraph-9">{{ review.description }}</p>
              </div>
            </div>
          </div>
        </div>
    </body>
  </html>
  </client-only>
</template>
<script>
export default {
  data() {
    return {
      tutordata: [],
      reviews: [],
    }
  },
  async fetch() {
    const url = 'https://api.tutorpal.org/tutors/' + this.$route.params.id + '/'
    this.tutordata = await fetch(url, {
      credentials: 'include',
    }).then((res) => res.json())
    this.reviews = await fetch(url + 'reviews/', {
      credentials: 'include',
    }).then((res) => res.json())
  },
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


