import {
  FormControl,
  FormLabel,
  IconButton,
  Input,
  InputGroup,
  InputRightElement,
  useDisclosure,
} from '@chakra-ui/react'
import * as React from 'react'
import { HiEye, HiEyeOff } from 'react-icons/hi'



interface Props{
  displayCustomName?: string
  id?: string
  name?: string
}
export const PasswordField = (props: Props) => {
  const { isOpen, onToggle } = useDisclosure()
  const inputRef = React.useRef<HTMLInputElement>(null)

  const onClickReveal = () => {
    onToggle()
    if (inputRef.current) {
      inputRef.current.focus({ preventScroll: true })
    }
  }

  return (
    <FormControl>
      <FormLabel htmlFor="password">{ props.displayCustomName || 'Password' }</FormLabel>
      <InputGroup>
        <InputRightElement>
          <IconButton
            variant="link"
            aria-label={isOpen ? 'Mask password' : 'Reveal password'}
            icon={isOpen ? <HiEyeOff /> : <HiEye />}
            onClick={onClickReveal}
          />
        </InputRightElement>
        <Input
          id={props.id}
          name={props.name}
          type={isOpen ? 'text' : 'password'}
          autoComplete="current-password"
          required
        />
      </InputGroup>
    </FormControl>
  )
}

