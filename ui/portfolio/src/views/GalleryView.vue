<template>
  <div class="flex flex-row m-2 p-1 md:m-4 md:p-3 lg:m-4 lg:p-3 xl:m-8 xl:p-6">
    <div class="basis-1/6">
      <SidePanel />
    </div>
    <div class="basis-5/6">
      <Gallery :images="images" />
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import SidePanel from "../components/SidePanel.vue";
import Gallery from "../components/Gallery.vue";
import { Image } from "../types";
import { getImages } from "../api";
import { Prop } from "vue-property-decorator";

@Options({
  components: { SidePanel, Gallery },
})
export default class GalleryView extends Vue {
  @Prop() groupId!: number;

  images: Image[] = [];

  async mounted() {
    this.images = await getImages(this.groupId);
  }

  async beforeCreate() {
    this.images = await getImages(this.groupId);
  }
}
</script>
