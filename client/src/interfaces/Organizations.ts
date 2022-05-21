
export interface Organization{
  id: string;
  name: string;
  image: string;
  users : User[];
}

export interface User{
  id: string;
  name: string;
  image: string;
}
