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
</div>
</template>

<script>
import HomeMain from '../components/HomeMain';
import HomeStudent from '../components/HomeStudent';
import HomeTutor from '../components/HomeTutor';
var x = 10;
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

export default {
  components: {
    HomeMain,
    HomeStudent,
    HomeTutor   
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
// var WebFont = require('webfontloader');

// WebFont.load({
//     google: {
//       families: ["Montserrat:100,100italic,200,200italic,300,300italic,400,400italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic","Poppins:regular","Roboto:regular"]
//     }
// });

</script>
