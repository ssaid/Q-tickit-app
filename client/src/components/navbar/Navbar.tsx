import{
  Link
} from 'react-router-dom';
import {
  Box,
  Stack,
  Icon,

} from '@chakra-ui/react';

import {
  IoHome,
  IoBarChartSharp,
  IoQrCodeSharp,
} from 'react-icons/io5';

import {
  BsGearFill,
  BsFillCalendar2EventFill,
} from 'react-icons/bs';


import {
  MdMapsHomeWork
} from 'react-icons/md';


export const Navbar = () => {
  return (
    <Stack 
      position='fixed'
      bottom='0'
      bg='blackAlpha.700' 
      h={12} 
      p={0}
      m={0}
      w='inherit'
      maxW='container.sm'
      direction='row'
      justifyContent='space-around'
      alignContent='center'
    >
      <Link to='/'>
        <Box 
          p={4}
          display='flex'
          alignSelf='center'
          color='white'
        >
          <Icon w={6} h={6} as={ MdMapsHomeWork } />
        </Box>
      </Link>
      <Link to='events'>
        <Box 
          p={4}
          display='flex'
          alignSelf='center'
          color='white'
        >
          <Icon w={5} h={5} as={ BsFillCalendar2EventFill } />
        </Box>
      </Link>
      <Link to='/camera'>
        <Box 
          p={4}
          display='flex'
          alignSelf='center'
        >
          <Icon w={5} h={5} as={ IoQrCodeSharp } />
        </Box>
      </Link>
      <Link to='stats'>
        <Box 
          p={4}
          display='flex'
          alignSelf='center'
          color='white'
        >
          <Icon w={5} h={5} as={ IoBarChartSharp } />
        </Box>
      </Link>
      <Link to='/configuration'>
        <Box 
          p={4}
          display='flex'
          alignSelf='center'
          color='white'
        >
          <Icon w={5} h={5} as={ BsGearFill } />
        </Box>
      </Link>
    </Stack>
  )
}
