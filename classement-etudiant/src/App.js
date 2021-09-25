import './App.css';
import { BrowserRouter as Router,Switch,Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import  Login  from './pages/Login';
import  Sign from './pages/Sign';
function App() {
  return (
    <div className="App">
      <Router>
        <Switch> 
          <Route exact path="/">
              <Navbar/>
          </Route>
          <Route exact path="/login">
            <Login/>
          </Route>
          <Route exact path="/sign">
            <Sign/>
          </Route>
        </Switch>
      </Router>
    </div>
  );
}



export default App;
