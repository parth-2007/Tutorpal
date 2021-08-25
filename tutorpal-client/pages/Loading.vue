<template>
  <client-only>
    <div>
      <Loader></Loader>
    </div>
  </client-only>
</template>
<script>
export default {
  created(){
    setTimeout(function () {
      this.$router.push('/loading')
    }, 3000);
  }
}
</script>
