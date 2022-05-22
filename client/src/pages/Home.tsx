import {Box, Container} from "@chakra-ui/react"
import {Outlet} from "react-router-dom"
import {Navbar} from "../components/navbar/Navbar"

export const Home = () => {
  return (
    <Container h='100vh' m={0} p={0} maxW='container.sm'>
      <Box h={'calc(100% - 3rem)'}> {/* 3rem = navbar height */}
        <Outlet />
      </Box>
      <Navbar />
    </Container>
  )
}
