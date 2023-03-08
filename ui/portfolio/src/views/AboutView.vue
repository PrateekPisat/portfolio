<template>
  <div class="flex flex-row">
    <div class="basis-1/6 p-3 lg:m-2">
      <SidePanel />
    </div>
    <div class="basis-5/6 p-3 lg:m-2">
      <About :user="user" />
    </div>
  </div>
</template>
<script lang="ts">
import About from "../components/About.vue";
import { Options, Vue } from "vue-class-component";
import SidePanel from "../components/SidePanel.vue";
import { User } from "../types";
import { getUser } from "../api";

@Options({
  components: { About, SidePanel },
})
export default class AboutView extends Vue {
  user: User | null = null;

  async mounted() {
    this.user = await getUser(1);
  }

  async beforeCreate() {
    this.user = await getUser(1);
  }
}
</script>
