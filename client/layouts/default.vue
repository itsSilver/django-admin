<template>
  <div>
    <client-only>
      <div class="main-app">
        <Nuxt />
      </div>
    </client-only>
  </div>
</template>
<script>
import Nav from '~/components/Nav'
export default {
  middleware: 'auth',
  components: {
    Nav,
  },
}
</script>