import './App.css'
import { BrowserRouter as Router, Routes, Route, Outlet } from 'react-router-dom';
import Layout from "../Layout.jsx";
import HomePage from "./components/main/HomePage.jsx";

function App() {
  return (

        <Router>
            <Routes>
                <Route element={<Layout />}>
                    <Route path="/" element={<HomePage />} />
                </Route>
            </Routes>
        </Router>


  )
}

export default App
