import {
  Avatar,
  AvatarGroup,
  HStack, Text

} from '@chakra-ui/react';


import { Organization } from '../../interfaces/Organizations';

interface Props {
  organization: Organization;
}

export const Header = ({ organization }: Props) => {


  // if (!organization){
  //   return(
  //     <HStack
  //       bg="blackAlpha.700"
  //       h='24'
  //     >
  //       <Text> Not implemented </Text>
  //     </HStack> 

  //   )
  // }


  return (
    <HStack
      bg="blackAlpha.700"
      h='24'
      p={4}
    >
      <Avatar size='lg' name='Dan Abrahmov' src='https://bit.ly/dan-abramov' />
      <AvatarGroup max={4} size='md'>
        <Avatar size='md' name='Kola Tioluwani' src='https://bit.ly/tioluwani-kolawole' />
        <Avatar size='md' name='Christian Nwamba' src='https://bit.ly/code-beast' />
        <Avatar size='md' name='Dan Abrahmov' src='https://bit.ly/dan-abramov' />
        <Avatar size='md' name='Kola Tioluwani' src='https://bit.ly/tioluwani-kolawole' />
        <Avatar size='md' name='Kola Tioluwani' src='https://bit.ly/tioluwani-kolawole' />
        <Avatar size='md' name='Dan Abrahmov' src='https://bit.ly/dan-abramov' />
        <Avatar size='md' name='Christian Nwamba' src='https://bit.ly/code-beast' />
      </AvatarGroup>
    </HStack> 
  )
}
