<template>
<client-only>
<html data-wf-page="5f5d0db29d3d2a83a01fb34a" data-wf-site="5f5d0db29d3d2a6ab81fb349">
<head>
  <meta charset="utf-8">
</head>
<body id="body" class="body">
  <div id="main">
    <div class="section"><a href="/" aria-current="page" class="link-block w-inline-block w--current"><img src="./tutor/images/logo.jpg" loading="lazy" width="260" srcset="./tutor/images/logo-p-500.jpeg 500w, ./tutor/images/logo-p-800.jpeg 800w, ./tutor/images/logo-p-1080.jpeg 1080w, ./tutor/images/logo.jpg 1432w" sizes="(max-width: 479px) 100vw, (max-width: 767px) 34vw, (max-width: 991px) 25vw, (max-width: 1439px) 21vw, (max-width: 1919px) 15vw, 12vw" alt=""></a>
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
                    <a id="logout" href="#" class="dropdown-link-2 w-inline-block">
                      <div class="nav-content-wrap-2">
                        <div class="dropdown-title-2">Logout</div>
                      </div>
                    </a>
                    <a href="account.html" class="dropdown-link-2 w-inline-block">
                      <div class="nav-content-wrap-2">
                        <div class="dropdown-title-2">Account</div>
                      </div>
                    </a>
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
          <nav role="navigation" class="nav-menu-3 w-nav-menu"><a href="index.html" aria-current="page" class="nav-link-4 w-nav-link w--current">Requests</a><a href="inbox_tutor.html" class="nav-link-4 w-nav-link">Messages</a><a href="payments.html" class="nav-link-4 w-nav-link">Payments</a></nav>
          <div class="menu-button-2 w-nav-button">
            <div class="icon-2 w-icon-nav-menu"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="columns-4 w-row">
    <div class="w-col w-col-8">
      <div class="div-block-44">
        <div class="div-block-45"><img src="./tutor/images/question.png" loading="lazy" width="30" alt=""><a href="mailto:the2tor4u@gmail.com?subject=Website%20Email" class="link-2">Need help? Send us an email</a></div>
        <h1 class="heading">Student Requests</h1>
        <div class="div-block-48">
          <div class="text-block-23">Inbox</div>
          <p class="paragraph">Please accept or deny these requests based off of your comfort ability.</p>
        </div>
        <div id="inbox" class="loop"></div>
      </div>
    </div>
    <div class="column-15 w-col w-col-4">
      <div style="  margin-bottom: 20px;" class="div-block-53">
        <h1 class="heading-2">Starting:</h1>
        <div class="upcoming_loop">
            <div id="started"></div>
        </div>
      </div>
      <div style="height: 300px; margin-bottom: 20px;" class="div-block-53">
        <h1 class="heading-2">Upcoming Classes:</h1>
        <div class="upcoming_loop">
            <div id="upcoming"></div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
</client-only>
</template>
<style>

</style>
<script>
export default{
  head (){
    return{
      title: "Home",
    }
  },
}
</script>