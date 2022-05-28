import {Box, Stack} from "@chakra-ui/react"
import {useState} from "react"


import {Header} from "../components/organization/Header"
import {Organization} from "../interfaces/Organizations"


export const Principal = () => {
  
  const [organizations, setOrganizations] = useState<Organization[]>([])
  
  return (
    <Stack h='100%'>
      <Header organization={ organizations[0] } />
      <Stack justifyContent='center' alignItems='center' h='100%'>
        {
          !organizations.length 
            ?
            (
              <Box>
                it seems like you don't have any organization yet
              </Box>

            )
            :
            (
              <Box>Hello again!</Box> 
            )

        }
      </Stack>
    </Stack> 
  )
}
