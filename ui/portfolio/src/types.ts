export interface Image {
  id: number;
  width: number;
  height: number;
  blurHash: string;
  description: string;
  city: string;
  country: string;
  fullPath: string;
  thumbnailPath: string;
  createdAt: string;
  updatedAt: string;
}

export interface User {
  username: string;
  firstName: string;
  lastName: string;
  instagramUsername: string;
  bio?: string;
  location: string;
  totalPhotos: number;
  profilePicturePath?: string;
  createdAt: string;
  updatedAt: string;
}

export interface Group {
  id: number;
  name: string;
  createdAt: string;
  updatedAt: string;
}
