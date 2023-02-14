import http from "./https";
import { Image, User } from "./types";

export async function getImages(): Promise<Image[]> {
  try {
    const response = await http.get("/images");
    return response.data["images"];
  } catch (error) {
    console.error(error);
    return [];
  }
}

export async function getImage(imageId: number): Promise<Image | null> {
  try {
    const response = await http.get("/image/" + imageId);
    return response.data["image"];
  } catch (error) {
    console.error(error);
    return null;
  }
}

export async function getUser(userId: number): Promise<User | null> {
  try {
    const response = await http.get("/user/" + userId);
    return response.data["user"];
  } catch (error) {
    console.error(error);
    return null;
  }
}

export function getPathToImages(): string {
  return process.env.VUE_APP_PATH_TO_IMAGES;
}
