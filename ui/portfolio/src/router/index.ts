import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router";
import GalleryView from "../views/GalleryView.vue";
import GalleryImage from "../components/GalleryImage.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: GalleryView,
  },
  {
    path: "/image/:id",
    name: "image.show",
    component: GalleryImage,
    props: true,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
