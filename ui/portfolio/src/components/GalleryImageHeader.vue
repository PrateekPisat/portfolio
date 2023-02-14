<template>
  <div>
    <div class="float-left">
      <GalleryImageHeaderProfile :user="user" />
    </div>
    <div class="float-right">
      <button
        v-on:click="downloadFile"
        class="inline-block px-6 py-2.5 bg-green-500 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-green-600 hover:shadow-lg focus:bg-green-600 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-green-700 active:shadow-lg transition duration-150 ease-in-out"
      >
        Download
        <font-awesome-icon class="px-1" icon="fa-solid fa-download" />
      </button>
    </div>
  </div>
</template>
<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";
import { Image, User } from "../types";
import GalleryImageHeaderProfile from "./GalleryImageHeaderProfile.vue";
import { getPathToImages } from "../api";

@Options({ components: { GalleryImageHeaderProfile } })
export default class GalleryImageHeader extends Vue {
  @Prop() user!: User;
  @Prop() image!: Image;

  downloadFile() {
    const link = document.createElement("a");
    link.href = getPathToImages() + this.image.fullPath;
    link.download = this.image.fullPath.replace("full/", "");
    link.click();
  }
}
</script>
