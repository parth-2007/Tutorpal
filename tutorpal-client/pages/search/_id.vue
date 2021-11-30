<template>
  <div v-if="!user.unfetched" id="main">
    <MainSearch/>
  </div>
  <div v-else>
    <Loader></Loader>
  </div>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  computed: mapGetters({ user: 'getUser' }),
  async created() {
    await this.fetchUser()
  },
  methods: {
    ...mapGetters(['getUser']),
    ...mapActions(['fetchUser']),
  },
}
</script>
