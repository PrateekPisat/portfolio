<template>
  <div class="text-sm">
    <SidePanelLogo />
    <SidePanelLinkList />
    <SidePanelSocials />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import SidePanelLogo from "@/components/SidePanelLogo.vue";
import SidePanelLinkList from "@/components/SidePanelLinkList.vue";
import SidePanelSocials from "@/components/SidePanelSocials.vue";

@Options({
  components: {
    SidePanelLogo,
    SidePanelLinkList,
    SidePanelSocials,
  },
})
export default class SidePanel extends Vue {}
</script>
