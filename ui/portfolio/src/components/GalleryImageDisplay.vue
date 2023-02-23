<template>
  <div class="mx-20">
    <img :src="fullPath" />
  </div>
</template>
<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";
import { getPathToImages } from "../api";
import { Image } from "../types";

@Options({})
export default class GalleryImageDisplay extends Vue {
  @Prop() image!: Image;

  get fullPath(): string {
    return getPathToImages() + this.image.fullPath;
  }
}
</script>
