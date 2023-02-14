<template>
  <div class="flex space-x-6">
    <SidePanelSocialsItem
      iconName="fa-brands fa-instagram"
      linkUrl="https://www.instagram.com/prateekpisat/"
    />
    <SidePanelSocialsItem
      iconName="fa-brands fa-unsplash"
      linkUrl="https://unsplash.com/@prateekpisat"
    />
    <SidePanelSocialsItem
      iconName="fa-brands fa-github"
      linkUrl="https://github.com/PrateekPisat"
    />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import SidePanelSocialsItem from "./SidePanelSocialsItem.vue";

@Options({ components: { SidePanelSocialsItem } })
export default class SidePanelSocials extends Vue {}
</script>
