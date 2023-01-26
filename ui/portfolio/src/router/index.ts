import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router";
import GalleryView from "../views/GalleryView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: GalleryView,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
