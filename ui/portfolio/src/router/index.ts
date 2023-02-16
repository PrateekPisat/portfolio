import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router";
import GalleryView from "../views/GalleryView.vue";
import GalleryImageView from "../views/GalleryImageView.vue";
import AboutView from "../views/AboutView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: GalleryView,
  },
  {
    path: "/image/:id",
    name: "image.show",
    component: GalleryImageView,
    props: true,
  },
  {
    path: "/about/",
    name: "about",
    component: AboutView,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
