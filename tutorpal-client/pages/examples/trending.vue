<template>
  <div>
    {{ trending }}
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  computed: mapGetters({ trending: 'getTrending' }),
  async created() {
    await this.fetchTrending()
  },
  methods: {
    ...mapActions(['fetchTrending']),
  },
}
</script>
