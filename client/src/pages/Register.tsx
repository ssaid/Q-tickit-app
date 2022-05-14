import { useNavigate } from 'react-router-dom';
import {
  Box,
  Button,
  Container,
  FormControl,
  FormLabel,
  Heading,
  Icon,
  Input,
  Stack,
} from '@chakra-ui/react'


import { IoHappyOutline } from 'react-icons/io5'

import { PasswordField } from '../components/login/PasswordField';


export const Register = () => {

  const navigate = useNavigate()

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    let form = Object.fromEntries(new FormData(e.currentTarget).entries())

    //TODO: mejorar contrasenias no coinciden
    if (form?.confirm_password !== form?.password) 
      return


    delete form.confirm_password

    const API_URL: string = import.meta.env.VITE_API_URL?.toString() ?? ''

    fetch(`${API_URL}/users`, {
      method: 'POST',
      body: JSON.stringify(form),
      headers: {
            'Content-Type': 'application/json'
          }
    })
      .then( res => {
        if (!res.ok)
          return
        return res.json()

      })
      .then(data => localStorage.setItem('session', JSON.stringify(data)))
      .then(() => navigate('/', {replace: true}))
      .catch(console.warn)

  }

  return(
    <Container maxW="sm" py={6} px={8}>
      <Stack spacing="8">
        <Stack spacing="6">
          <Stack 
            justifyContent="center"
            alignItems="center"
          >
            <Icon h={16} w={16} as={IoHappyOutline} />
          </Stack>
          <Stack spacing={{ base: '2', md: '3' }} textAlign="center">
            <Heading size="md">
              Register
            </Heading>
          </Stack>
        </Stack>
        <Box
        >
          <form
            onSubmit={handleSubmit}
          >
            <Stack spacing={6}>
              <Stack 
                p={6}
                spacing={2}
                boxShadow="2xl"
              >
                <FormControl>
                  <FormLabel htmlFor="name">Your name</FormLabel>
                  <Input boxShadow="2xl" name="name" id="name" type="text" autoComplete="off" />
                </FormControl>
                <FormControl>
                  <FormLabel htmlFor="login">Username</FormLabel>
                  <Input name="login" id="login" type="text" autoComplete="off" />
                </FormControl>
                <PasswordField name="password" id="password"/>
                <PasswordField name="confirm_password" id="confirm_password" displayCustomName="Confirm Password"/>

                <FormControl>
                  <FormLabel htmlFor="email">Email</FormLabel>
                  <Input name="email" id="email" type="email" autoComplete="off" />
                </FormControl>
              </Stack>
            <Button
              colorScheme="blue"
              isFullWidth={true}
              type="submit"
            >
              Register
            </Button>
            </Stack>
          </form>
        </Box>
      </Stack>
    </Container>
  )
}
