<template>
<div id="main">
  <div v-if='variable === 50'>
    <HomeMain></HomeMain>
  </div>
  <div v-else-if='variable === 20'>
    <HomeStudent></HomeStudent>
  </div>
  <div v-else-if='variable === 10'>
    <HomeTutor></HomeTutor>
  </div>
  <div v-else-if='variable === 0'>
    <NotFound></NotFound>
  </div>
</div>
</template>

<script>
import HomeMain from '../components/HomeMain';
import HomeStudent from '../components/HomeStudent';
import HomeTutor from '../components/HomeTutor';
import NotFound from '../components/NotFound';
var x = 50;
if (x === 50){
  require('../components/main/css/webflow.css');
  require('../components/main/css/homepage-12.webflow.css');
  require('../components/main/css/normalize.css');
}
else if(x === 20){
  require('../components/student/css/webflow.css');
  require('../components/student/css/student-main.webflow.css');
  require('../components/student/css/normalize.css');
}
else if(x === 10){
  require('../components/tutor/css/webflow.css');
  require('../components/tutor/css/tutor-main.webflow.css');
  require('../components/tutor/css/normalize.css');
}
else if( x === 0){
  require('../components/outcast/css/webflow.css');
  require('../components/outcast/css/last-project-afcf8d.webflow.css');
  require('../components/outcast/css/normalize.css');
}

export default {
  components: {
    HomeMain,
    HomeStudent,
    HomeTutor,
    NotFound 
  },
  head (){
    return{
      title: "Home - TutorPal",
    }
  },
  data() {
      return {
          variable: x,
      }
  }
}

</script>
