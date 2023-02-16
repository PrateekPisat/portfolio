<template>
  <router-link to="/">
    <div class="grid grid-cols-2 grid-flow-row place-items-stretch">
      <img
        class="rounded-full mr-8"
        :src="profilePicture"
        alt="Profile Picture"
      />
      <div class="">
        <div>{{ user.lastName }} {{ user.lastName }}</div>
        <div class="text-zinc-300">{{ user.username }}</div>
      </div>
    </div>
  </router-link>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";
import { User } from "../types";
import { getPathToImages } from "../api";

export default class GalleryImageHeaderProfile extends Vue {
  @Prop() user!: User;

  get profilePicture() {
    return getPathToImages() + this.user.profilePicturePath;
  }
}
</script>
