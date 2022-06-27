export default {
  // components: true,
  target: 'static',
  webfontloader: {
    google: {
      families: [
        'Montserrat:100,100italic,200,200italic,300,300italic,400,400italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic',
        'Poppins:regular',
        'Roboto:regular',
      ], // Loads Lato font with weights 400 and 700
    },
  },
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'tutorpal-client',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.jpg' }],
  },
  router: {
    base: '/',
  },
  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    "~/node_modules/bootstrap/dist/css/bootstrap.min.css"
  ],
  plugins: [
      { src: "~/node_modules/bootstrap/dist/js/bootstrap.bundle.min.js", mode: "client" }
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    '@nuxtjs/dotenv',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    'nuxt-webfontloader',
    // '@nuxtjs/proxy',
  ],

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en',
    },
  },

  env: {
    // If api url is specified as local use that, otherwise default to prod url
    API_URL: process.env.API_URL || 'https://api.tutorpal.org',
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  // build: {
  // proxy: {
  //   '/api': {
  //     target: 'https://api.tutorpal.org',
  //     changeOrigin: true,
  //     pathRewrite: { '^/api': '/' },
  //   },
  // },
  // },

  // devServer: {
  // proxy: {
  //   '/api': {
  //     target: 'http://localhost:5000/api',
  //     changeOrigin: true,
  //     logLevel: 'debug',
  //     pathRewrite: { '^/api': '/' },
  //   },
  // },
  // },

  // proxy: {
  //   '/api': {
  //     target:
  //       process.env.NODE_ENV === 'PROD'
  //         ? 'http://localhost:5000/api'
  //         : 'https://api.tutorpal.org',
  //     changeOrigin: true,
  //     logLevel: 'debug',
  //     pathRewrite: { '^/api': '/' },
  //   },
  // },
}
