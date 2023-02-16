<template>
  <div class="pb-10">
    <router-link to="/">
      <img class="inline" src="assets/logo.png" alt="Prateek Pisat" />
    </router-link>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";

@Options({})
export default class SidePanelLogo extends Vue {}
</script>
