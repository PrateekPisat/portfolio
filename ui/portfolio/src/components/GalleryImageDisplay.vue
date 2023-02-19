<template>
  <div class="mx-20">
    <Blurhash
      src="https://blurha.sh/assets/images/img2.jpg"
      :punch="1"
      hash="LGF5]+Yk^6#M@-5c,1J5@[or[Q6."
      height="100%"
      width="100%"
    ></Blurhash>
  </div>
</template>
<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";
import { getPathToImages } from "../api";
import { Image } from "../types";
import Blurhash from "vue3-blurhash";

@Options({ components: { Blurhash } })
export default class GalleryImageDisplay extends Vue {
  @Prop() image!: Image;

  get fullPath(): string {
    return getPathToImages() + this.image.fullPath;
  }
}
</script>
