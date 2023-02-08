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
