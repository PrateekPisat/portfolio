<template>
  <div class="xs:flex-col xs:space-y-4 md:flex md:space-x-8 xs:space-x-4">
    <img src="asd" alt="About Picture" />
    <div class="font-mono md:w-96 xs:w-72">
      <AboutBio :bio="user.bio" />
      <AboutItem
        title="Email"
        value="pratekpisat12@gmail.com"
        link="mailto:pratekpisat12@gmail.com"
      />
      <AboutItem
        title="Instagram"
        :value="instagramUsername"
        :link="instagramLink"
      />
      <AboutItem title="GitHub" value="PrateekPisat" :link="gitHubLink" />
      <AboutItem title="Unsplash" :value="user.username" :link="unsplashLink" />
    </div>
  </div>
</template>
<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";
import { User } from "../types";
import AboutBio from "./AboutBio.vue";
import AboutItem from "./AboutItem.vue";

@Options({ components: { AboutItem, AboutBio } })
export default class About extends Vue {
  @Prop() user!: User;

  get instagramUsername(): string {
    return "@" + this.user.instagramUsername;
  }

  get instagramLink(): string {
    return "https://www.instagram.com/" + this.user.instagramUsername;
  }

  get unsplashLink(): string {
    return "https://unsplash.com/" + this.instagramUsername;
  }

  get gitHubLink(): string {
    return "https://github.com/PrateekPisat";
  }
}
</script>
