<template>
  <div class="pb-8">
    <p class="font-bold">
      Photographer / Director / Cinematographer currently based in LA
    </p>
    <p class="text-sm">{{ bio }}</p>
  </div>
</template>
<script lang="ts">
import { Vue } from "vue-class-component";
import { Prop } from "vue-property-decorator";

export default class AboutBio extends Vue {
  @Prop() bio!: string;
}
</script>
