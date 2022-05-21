import {
  BrowserRouter as Router,
  Routes,
  Route,
} from 'react-router-dom';
import {AuthProvider} from '../context/AuthProvider';
import {
  Home,
  Stats,
  Configuration,
  Events,
  Camera,
  Login,
  Register,
} from '../pages';
import {Principal} from '../pages/Principal';
import { PrivateRoute } from './PrivateRoute';


export const AppRouter = () => {
  return (
    
    <AuthProvider>
      <Router>
        <Routes>
            <Route path="/" element={ 
                <PrivateRoute>
                  <Home />
                </PrivateRoute> 
              } 
            >
              <Route path="/" element={ <PrivateRoute><Principal /></PrivateRoute> } />
              <Route path="/stats" element={ <PrivateRoute><Stats /></PrivateRoute> } />
              <Route path="/configuration" element={ <PrivateRoute><Configuration /></PrivateRoute> } />
              <Route path="/events" element={ <PrivateRoute><Events /></PrivateRoute> } />
              <Route path="/camera" element={ <PrivateRoute><Camera /></PrivateRoute> } />
            </Route>
          <Route path="/login" element={ <Login /> } />
          <Route path="/register" element={ <Register /> } />
        </Routes>
      </Router>
    </AuthProvider>

  )
}
