import { extendTheme, theme } from "@chakra-ui/react"

export default extendTheme({
  colors: {
    primary: theme.colors.blackAlpha[700],
    secondary: theme.colors.blackAlpha[200],
    textPrimary: theme.colors.white,
    textSecondary: theme.colors.gray[400],
  },
})
