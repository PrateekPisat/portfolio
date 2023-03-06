<template>
  <div :class="aspectRatioClass">
    <button>
      <router-link :to="routerLink">
        <img :src="thumbnailPath" :alt="image_id" />
      </router-link>
    </button>
  </div>
</template>

<script lang="ts">
import { Image } from "@/types";
import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";
import { getPathToImages } from "../api";

@Options({ components: {} })
export default class GalleryItem extends Vue {
  @Prop() image!: Image;

  get image_id(): string {
    return "image" + this.image.id;
  }

  get aspectRatioClass(): string {
    let aspectRatio = this.image.width / this.image.height;

    if (aspectRatio <= 0.8) {
      return "row-span-2";
    }

    return "";
  }

  get thumbnailPath(): string {
    return getPathToImages() + this.image.thumbnailPath;
  }

  get routerLink() {
    return "/image/" + this.image.id;
  }
}
</script>
