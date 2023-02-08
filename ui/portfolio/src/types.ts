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
  createdAt: Date;
  updatedAt: Date;
}

export interface User {
  username: string;
  firstName: string;
  lastName: string;
  instagramUsername: string;
  bio: string;
  location: string;
  totalPhotos: number;
  createdAt: Date;
  updatedAt: Date;
}
