<template>
  <div class="pb-8">
    <p class="font-bold">
      Software Engineer / Photographer / Noob currently based in Boston
    </p>
    <p class="text-sm">{{ userBio }}</p>
  </div>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";

export default class AboutBio extends Vue {
  @Prop() bio!: string;

  get userBio(): string {
    return this.bio || "";
  }
}
</script>
