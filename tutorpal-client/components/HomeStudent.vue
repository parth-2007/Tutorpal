
<template>
  <client-only>
    <html
      data-wf-page="5f600218af481481a99ffa6a"
      data-wf-site="5f600218af4814e3759ffa69"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <body id="body" class="body">
        <div class="div-block-55">
          <div class="section">
            <a
              href="/"
              aria-current="page"
              class="link-block w-inline-block w--current"
              ><img
                src="./student/images/logo.jpg"
                loading="lazy"
                width="260"
                srcset="
                  ./student/images/logo-p-500.jpeg   500w,
                  ./student/images/logo-p-800.jpeg   800w,
                  ./student/images/logo-p-1080.jpeg 1080w,
                  ./student/images/logo.jpg         1432w
                "
                sizes="(max-width: 479px) 100vw, (max-width: 767px) 33vw, (max-width: 991px) 25vw, (max-width: 1439px) 20vw, (max-width: 1919px) 15vw, 12vw"
                alt=""
            /></a>
            <div class="div-block-4">
              <form action="search_student.html" class="stuff w-form">
                <img
                  src="./student/images/search-1.png"
                  loading="lazy"
                  width="25"
                  height="25"
                  srcset="
                    ./student/images/search-1-p-500.png 500w,
                    ./student/images/search-1.png       512w
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
              <div class="div-block-43">
                <div class="name_profile_pic">
                  <img
                    id="image"
                    width="60"
                    height="60"
                    sizes="(max-width: 479px) 15vw, (max-width: 767px) 8vw, 60px"
                    alt=""
                    class="image-7"
                  />
                  <div
                    data-hover=""
                    data-delay="0"
                    class="dropdown-3 w-dropdown"
                  >
                    <div class="dropdown-toggle-2-copy w-dropdown-toggle">
                      <div class="text-block-18" id="name"></div>
                      <div class="text-block-20">Student</div>
                    </div>
                    <nav class="navigation-dropdown-2 w-dropdown-list">
                      <div class="dropdown-pointer-2">
                        <div style="width: 300px" class="dropdown-wrapper-2">
                          <a
                            href="#"
                            id="logout"
                            class="dropdown-link-2 w-inline-block"
                          >
                            <div class="nav-content-wrap-2">
                              <div class="dropdown-title-2">Logout</div>
                            </div>
                          </a>
                          <a
                            href="profile.html"
                            class="dropdown-link-2 w-inline-block"
                          >
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
            <div
              data-collapse="none"
              data-animation="default"
              data-duration="400"
              role="banner"
              class="navbar-2 w-nav"
            >
              <div class="container-2 w-container">
                <nav role="navigation" class="nav-menu-3 w-nav-menu">
                  <a
                    href="index.html"
                    aria-current="page"
                    class="nav-link-4 w-nav-link w--current"
                    >Explore</a
                  ><a href="inbox_student.html" class="nav-link-4 w-nav-link"
                    >Messages</a
                  ><a href="requests.html" class="nav-link-4 w-nav-link"
                    >Requests</a
                  ><a href="payments.html" class="nav-link-4 w-nav-link"
                    >Payments</a
                  >
                </nav>
                <div class="menu-button-2 w-nav-button">
                  <div class="icon-2 w-icon-nav-menu"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="columns-4 w-row">
          <div class="column-18 w-col w-col-8">
            <div class="div-block-44">
              <div class="div-block-45">
                <img
                  src="./student/images/question.png"
                  loading="lazy"
                  width="30"
                  alt=""
                /><a
                  href="mailto:the2tor4u@gmail.com?subject=Website%20Email"
                  class="link-2"
                  >Need help? Send us an email</a
                >
              </div>
              <div class="div-block-48">
                <div class="text-block-23">Trending</div>
                <p class="paragraph">
                  Find the highest-ranked tutors and the ones everybody is
                  learning from.
                </p>
              </div>
              <div class="trending">
                <div id="trending"></div>
              </div>
            </div>
          </div>
          <div class="column-15 w-col w-col-4">
            <div style="margin-bottom: 20px" class="div-block-53">
              <h1 class="heading-2">Starting:</h1>
              <div class="upcoming_loop">
                <div id="started"></div>
              </div>
            </div>
            <div
              style="height: 300px; margin-bottom: 20px"
              class="div-block-53"
            >
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
<script>

export default {
  head() {
    return {
      title: 'Home',
    }
  },
}
</script>



