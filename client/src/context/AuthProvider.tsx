import { createContext, useState } from "react"


interface Props {
  children: JSX.Element
}

interface User {
  token: string
  expirationDate: number
}

interface AuthContext{
  user: any
  setUser: (user: User) => void
}


const AuthContext = createContext<AuthContext>({} as AuthContext)

export const AuthProvider = ({ children }: Props) => {

  const [user, setUser] = useState<User>({} as User)

  return (
    <AuthContext.Provider value={{ user, setUser }}>
      {children}
    </AuthContext.Provider>
  )
}
