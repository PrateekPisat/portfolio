<template>
  <div class="">
    <router-link to="/">
      <img class="inline" :src="logoPath" alt="Prateek Pisat" />
    </router-link>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { getPathToImages } from "../api";

@Options({})
export default class SidePanelLogo extends Vue {
  get logoPath(): string {
    return getPathToImages() + "thumbnails/homepage_logo.png";
  }
}
</script>
