<template>
  <div>
    <button>
      <router-link :to="routerLink">
        <img :class="aspectRatioClass" :src="thumbnailPath" :alt="image_id" />
      </router-link>
    </button>
  </div>
</template>

<script lang="ts">
import { Image } from "@/types";
import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";
import { getPathToImages } from "../api";

@Options({})
export default class GalleryItem extends Vue {
  @Prop() image!: Image;

  get image_id(): string {
    return "image" + this.image.id;
  }

  get aspectRatioClass(): string {
    const aspectRatio = this.image.width / this.image.height;
    return "aspect-[" + aspectRatio + "]";
  }

  get thumbnailPath(): string {
    return getPathToImages() + this.image.thumbnailPath;
  }

  get routerLink() {
    return "/image/" + this.image.id;
  }
}
</script>
