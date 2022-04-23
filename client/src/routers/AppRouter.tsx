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


export const AppRouter = () => {
  return (
    
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={ <Home /> } >
            <Route path="/stats" element={ <Stats /> } />
            <Route path="/configuration" element={ <Configuration /> } />
            <Route path="/events" element={ <Events /> } />
            <Route path="/camera" element={ <Camera /> } />
          </Route>
          <Route path="/login" element={ <Login /> } />
          <Route path="/register" element={ <Register /> } />
        </Routes>
      </Router>
    </AuthProvider>

  )
}
