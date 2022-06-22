
<template>
  <client-only>
    <html
      data-wf-page="5f600218af481481a99ffa6a"
      data-wf-site="5f600218af4814e3759ffa69"
    >
      <head>
        <meta charset="utf-8" />
        <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" />
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
                  src="../static/student/images/logo.jpg"
                  width="250"
                  alt=""
                  class="image"
              /></router-link>
              <div style="margin-top: 15px" class="div-block-4">
                <div class="stuff w-form">
                  <img
                    src="../static/student/images/search-1.png"
                    loading="lazy"
                    width="25"
                    height="25"
                    srcset="
                      ../static/student/images/search-1.png 500w,
                      ../static/student/images/search-1.png 512w
                    "
                    sizes="(max-width: 767px) 25px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw"
                    alt=""
                    class="image-2"
                  /><input
                    class="search-3 w-input"
                    placeholder="Search by subject"
                    id="search"
                    v-model="q"
                    @keyup.enter="submitSearch()"
                  />
                </div>
              </div>
            </div>
          </div>
          <div v-if="data !== []" class="div-block-70">
            <div class="div-block-71">
              <img
                :src="data.user !== undefined ? data.user.profile_pic : ''"
                loading="lazy"
                width="74"
                height="74"
                style="border-radius: 100px;"
                sizes="74px"
                alt=""
              />
              <div class="div-block-72">
                <h1 class="heading-3" id="subjects">{{ data.subjects }}</h1>
                <div class="div-block-68">
                  <div class="text-block-32">
                    <strong id="fullname" class="bold-text-8"
                      >{{
                        data.user !== undefined ? data.user.first_name : ''
                      }}
                      {{
                        data.user !== undefined ? data.user.last_name : ''
                      }}</strong
                    >
                  </div>
                </div>
              </div>
            </div>
            <p style="padding-top: 20px" class="paragraph-8">
              <strong>Degree: </strong>{{ data.education }}<br /><strong
                >Qualification Description: </strong
              >{{ data.qualifications }}<br />
              <strong>Education: </strong
              ><text
                v-if="data.education !== 'High School' || data.major !== ''"
                >{{ data.major }} at</text
              >
              {{ data.school }} <br /><strong
                >Professional Experience: </strong
              >{{ data.prof_exp }} years<br /><strong
                >Teaching Experience: </strong
              >{{ data.teach_exp }} years<br />
              <strong>Average Review:</strong>
              <strong v-html="html"></strong>
              <strong style="font-size: 11px; margin: 0px; padding: 0px; font-weight: normal;">(Based on {{reviewNum}} Review(s))</strong>
              <br /><strong>Occupation: </strong
              >{{ data.occupation }}<br /><strong>Gender: </strong
              >{{ data.gender }}<br />
              <strong>Price: </strong>${{ data.rates }} hourly <br /><strong
                >Bio: </strong
              >{{ data.bio }}<br /><strong>Course Description: </strong
              >{{ data.what_you_teach }}<br /><strong>Availability: </strong
              >{{ data.availability }} <br /><a
                v-if="data.linkedIn !== ''"
                style="font-family: Poppins"
                :href="data.linkedIn"
                target="_blank"
                ><strong>Linkedin Account:</strong></a
              >
            </p>
          </div>
          <div class="div-block-56">
            <h1 class="heading-11">Reviews ({{this.reviewNum}})</h1>
            <div v-if="reviews !== []">
              <div
                v-for="review in reviews.results"
                :key="review.id"
                id="posts"
              >
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
                    <div  class="text-block-34">
                      Review: <strong :id="review.id"></strong>
                    </div>
                  </div>
                  <p class="paragraph-9">{{ review.description }}</p>
                </div>
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
      data: [],
      reviews: [],
      q: '',
      reviewNum: "",
      html: '',
    }
  },
  async fetch() {
    this.data = await fetch(
      process.env.API_URL + '/tutors/' + this.$route.params.id + '/',
      {
        credentials: 'include',
      }
    ).then((res) => res.json())
    this.reviews = await fetch(
      process.env.API_URL + '/tutors/' + this.$route.params.id + '/reviews/',
      {
        credentials: 'include',
      }
    ).then((res) => res.json())
    this.reviewNum=this.reviews.results.length;
    const rating = this.data.average_reviews;
    let output = '';
    let i = ""
    for (i = rating; i >= 1; i--){
      output+=('<i class="fa fa-star" aria-hidden="true" style="color: gold; font-size: 16px;"></i>&nbsp;');
    }
    /* eslint-disable */
    if (i == 0.5){
      output+=('<i class="fa fa-star-half-o" aria-hidden="true" style="color: gold; font-size: 16px;"></i>&nbsp;');
    } 
    /* eslint-enable */
    for (i = (5 - rating); i >= 1; i--){
      output+=('<i class="fa fa-star-o" aria-hidden="true" style="color: gold; font-size: 16px;"></i>&nbsp;');
    }
    this.html = output;
    this.getStars()
  },
  head() {
    return {
      title: 'Tutor Profile',
      link: [
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/webflow.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/normalize.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/student-main.webflow.css',
        },
      ],
    }
  },
  methods: {
    submitSearch() {
      this.$router.push('/search/' + this.q)
    },
    async getStars() {
      await new Promise(resolve => setTimeout(resolve, 1000));
      this.reviews.results.forEach((value,index ) => {
        const rating = value.stars;
        let output = '';
        let i = ""
        for (i = rating; i >= 1; i--){
          output+=('<i class="fa fa-star" aria-hidden="true" style="color: gold; font-size: 16px;"></i>&nbsp;');
        }
        /* eslint-disable */
        if (i == 0.5){
          output+=('<i class="fa fa-star-half-o" aria-hidden="true" style="color: gold; font-size: 16px;"></i>&nbsp;');
        } 
        /* eslint-enable */
        for (i = (5 - rating); i >= 1; i--){
          output+=('<i class="fa fa-star-o" aria-hidden="true" style="color: gold; font-size: 16px;"></i>&nbsp;');
        }
        document.getElementById(value.id).innerHTML = output;
      });
    },
  },
}
</script>


