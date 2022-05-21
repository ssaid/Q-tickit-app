import {Container} from "@chakra-ui/react"
import {Outlet} from "react-router-dom"
import {Navbar} from "../components/navbar/Navbar"

export const Home = () => {
  return (
    <Container h='100vh' m={0} p={0} maxW='container.sm'>
      <Outlet />
      <Navbar />
    </Container>
  )
}
