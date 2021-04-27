<template>
  <div>
    <label for="firstname" class="form-label">{{ name }}</label>
    <input
      :v-model="model"
      type="text"
      class="form-control"
      :id="model"
      :aria-label="name"
      required
    />
  </div>
</template>
<script>
export default {
  name: 'FormInput',
  props: {
    name: {
      type: String,
      default: '',
    },
    model: {
      type: String,
      default: '',
    },
  },
}
</script>