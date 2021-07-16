<template>
  <div id="main">
    <MainHome></MainHome>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  head() {
    return {
      title: 'Home - TutorPal',
    }
  },
  computed: mapGetters({ user: 'getUser' }),
  async created() {
    await this.fetchUser()
  },
  methods: {
    ...mapActions(['fetchUser']),
  },
}
</script>
