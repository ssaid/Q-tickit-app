import {useState} from "react"


import {Header} from "../components/organization/Header"
import {Organization} from "../interfaces/Organizations"


export const Principal = () => {
  
  const [organizations, setOrganizations] = useState<Organization[]>([])
  
  return (
    <>
      <Header organization={ organizations[0] } />
      Principal 
    </> 
  )
}
