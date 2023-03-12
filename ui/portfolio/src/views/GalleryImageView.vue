<template>
  <div class="grid grid-flow-row auto-rows-max mx-10 space-y-5 p-3 lg:m-2">
    <GalleryImageHeader :user="user" :image="image" />
    <GalleryImageDisplay :image="image" />
    <GalleryImageStats :image="image" />
  </div>
</template>
<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";
import { Image, User } from "../types";
import GalleryImageHeader from "../components/GalleryImageHeader.vue";
import GalleryImageDisplay from "../components/GalleryImageDisplay.vue";
import GalleryImageStats from "../components/GalleryImageStats.vue";
import { getUser, getImage } from "../api";

@Options({
  components: {
    GalleryImageHeader,
    GalleryImageDisplay,
    GalleryImageStats,
  },
})
export default class GalleryImage extends Vue {
  @Prop() id!: number;

  user?: User | null = null;
  image?: Image | null = null;

  async mounted() {
    this.user = await getUser(1);
    this.image = await getImage(this.id);
  }

  async beforeCreate() {
    this.user = await getUser(1);
    this.image = await getImage(this.id);
  }
}
</script>
