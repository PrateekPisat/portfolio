<template>
  <div class="flex flex-row m-2 p-1 md:m-4 md:p-3 lg:m-4 lg:p-3 xl:m-8 xl:p-6">
    <div class="sm:basis-1/6">
      <SidePanel />
    </div>
    <div class="sm:basis-5/6">
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
