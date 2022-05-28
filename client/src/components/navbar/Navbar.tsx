import{
  NavLink
  
} from 'react-router-dom';
import {
  Box,
  Stack,
  Icon,
  Link,

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
      position='absolute'
      bottom='0'
      bg='primary' 
      h={12} 
      p={0}
      m={0}
      w='inherit'
      maxW='container.sm'
      direction='row'
      justifyContent='space-around'
      alignContent='center'
    >
      <Link 
        as={NavLink} to='/'
        color='textSecondary'
        _activeLink={{color: 'textPrimary'}}
        _focus={{ringColor: 'transparent'}}

      >
        <Box 
          p={4}
          display='flex'
          alignSelf='center'
        >
          <Icon w={6} h={6} as={ MdMapsHomeWork } />
        </Box>
      </Link>
      <Link 
        as={NavLink} to='events'
        color='textSecondary'
        _activeLink={{color: 'textPrimary'}}
        _focus={{ringColor: 'transparent'}}
      >
        <Box 
          p={4}
          display='flex'
          alignSelf='center'
        >
          <Icon w={5} h={5} as={ BsFillCalendar2EventFill } />
        </Box>
      </Link>
      <Link
        as={NavLink}
        to='/camera'
        color='textSecondary'
        _activeLink={{color: 'textPrimary'}}
        _focus={{ringColor: 'transparent'}}
      >
        <Box 
          p={4}
          display='flex'
          alignSelf='center'
        >
          <Icon w={5} h={5} as={ IoQrCodeSharp } />
        </Box>
      </Link>
      <Link
        as={NavLink}
        to='stats'
        color='textSecondary'
        _activeLink={{color: 'textPrimary'}}
        _focus={{ringColor: 'transparent'}}
      >
        <Box 
          p={4}
          display='flex'
          alignSelf='center'
        >
          <Icon w={5} h={5} as={ IoBarChartSharp } />
        </Box>
      </Link>
      <Link
        as={NavLink}
        to='/configuration'
        color='textSecondary'
        _activeLink={{color: 'textPrimary'}}
        _focus={{ringColor: 'transparent'}}
      >
        <Box 
          p={4}
          display='flex'
          alignSelf='center'
        >
          <Icon w={5} h={5} as={ BsGearFill } />
        </Box>
      </Link>
    </Stack>
  )
}
