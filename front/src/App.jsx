import './App.css'
import AuthForm from "./components/auth/Register.jsx";

function App() {
    const token = localStorage.getItem('token')
  return (
    <>
        {token ? '' : <AuthForm/>}

    </>
  )
}

export default App
