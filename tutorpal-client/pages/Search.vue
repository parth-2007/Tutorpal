<template>
  <search-component></search-component>
</template>
<script>
import SearchComponent from '../components/SearchComponent.vue'
export default {
  components: { SearchComponent },
  head() {
    return {
      title: 'Search',
    }
  },
}
</script>