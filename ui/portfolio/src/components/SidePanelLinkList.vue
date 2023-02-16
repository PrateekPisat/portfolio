<template>
  <div class="mb-10">
    <ul class="flex flex-col space-y-3">
      <SidePanelLinkListItem name="Editorial" to="/" />
      <SidePanelLinkListItem name="Lifestyle" to="/" />
      <SidePanelLinkListItem name="Beauty" to="/" />
      <SidePanelLinkListItem name="Music" to="/" />
      <SidePanelLinkListItem name="Motion" to="/" />
      <SidePanelLinkListItem name="Product Still Life" to="/" />
      <SidePanelLinkListItem name="Fine Art/Personal" to="/" />
      <SidePanelLinkListItem name="About + Contact" to="/about/" />
    </ul>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import SidePanelLinkListItem from "./SidePanelLinkListItem.vue";

@Options({ components: { SidePanelLinkListItem } })
export default class SidePanelLinkList extends Vue {}
</script>
