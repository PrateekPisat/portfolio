<template>
  <div class="grid xs:grid-cols-1 lg:grid-cols-3 md:grid-cols-2 gap-4">
    <GalleryItem v-for="image in images" :key="image.id" :image="image" />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import GalleryItem from "./GalleryItem.vue";
import { Image, User } from "../types";
import { getImages, getUser } from "../api";

@Options({ components: { GalleryItem } })
export default class Gallery extends Vue {
  images: Image[] = [];
  user: User | null = null;

  async mounted() {
    this.images = await getImages();
    this.user = await getUser(1);
  }
}
</script>
