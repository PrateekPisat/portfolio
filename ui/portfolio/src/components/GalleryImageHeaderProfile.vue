<template>
  <router-link to="/">
    <div class="flex space-x-3">
      <img
        class="rounded-full w-14 h-14"
        :src="profilePicture"
        alt="Profile Picture"
      />
      <div>
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
