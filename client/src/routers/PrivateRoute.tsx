import {
  Navigate,
} from 'react-router-dom'

import moment from 'moment'

interface Props {
  children: JSX.Element[] | JSX.Element;
}

export const PrivateRoute = ({ children }: any) => {

  const session = localStorage.getItem('session') ?? ''

  const valid_session = !!session &&
    moment(JSON.parse(session).expiration).utc() >= moment().utc()

  return valid_session ? children : <Navigate replace to='/login' />

}

