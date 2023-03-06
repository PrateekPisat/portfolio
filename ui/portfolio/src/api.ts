import http from "./https";
import { Group, Image, User } from "./types";

export async function getImages(groupId: number | null): Promise<Image[]> {
  try {
    const response = await http.get("/api/images", {
      params: { groupId: groupId },
    });
    return response.data["images"];
  } catch (error) {
    console.error(error);
    return [];
  }
}

export async function getImage(imageId: number): Promise<Image | null> {
  try {
    const response = await http.get("/api/image/" + imageId);
    return response.data["image"];
  } catch (error) {
    console.error(error);
    return null;
  }
}

export async function getUser(userId: number): Promise<User | null> {
  try {
    const response = await http.get("/api/user/" + userId);
    return response.data["user"];
  } catch (error) {
    console.error(error);
    return null;
  }
}

export async function listGroups(): Promise<Group[]> {
  try {
    const response = await http.get("/api/groups");
    return response.data["groups"];
  } catch (error) {
    console.error(error);
    return [];
  }
}

export function getPathToImages(): string {
  return process.env.VUE_APP_PATH_TO_IMAGES;
}
