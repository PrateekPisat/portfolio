<template>
  <div class="text-sm w-40 h-full">
    <SidePanelLogo />
    <SidePanelLinkList />
    <SidePanelSocials />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import SidePanelLogo from "./SidePanelLogo.vue";
import SidePanelLinkList from "./SidePanelLinkList.vue";
import SidePanelSocials from "./SidePanelSocials.vue";

@Options({
  components: {
    SidePanelLogo,
    SidePanelLinkList,
    SidePanelSocials,
  },
})
export default class SidePanel extends Vue {}
</script>
