<template>
  <div>
    <GalleryImageStatsItem
      iconName="fa-solid fa-location-dot"
      :text="location"
    />
    <GalleryImageStatsItem
      iconName="fa-solid fa-calendar"
      :text="publishedOn"
    />
    <GalleryImageStatsItem iconName="fa-solid fa-camera" text="NIKON D5300" />
    <GalleryImageStatsItem
      iconName="fa-solid fa-file-contract"
      text="Free to use"
    />
  </div>
</template>
<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";
import { Image } from "../types";
import GalleryImageStatsItem from "./GalleryImageStatsItem.vue";

@Options({ components: { GalleryImageStatsItem } })
export default class GalleryImageStats extends Vue {
  @Prop() image!: Image;

  dateFormat(date: string) {
    return new Date(date).toLocaleDateString("en-US", {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric",
    });
  }

  get location() {
    return this.image.city + ", " + this.image.country;
  }

  get publishedOn() {
    return "Published on " + this.dateFormat(this.image.createdAt);
  }
}
</script>
