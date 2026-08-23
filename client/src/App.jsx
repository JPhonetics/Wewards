import { Outlet } from 'react-router-dom';
import Heading from './components/Heading/Heading';
import NavBar from "./components/NavBar";

export default function App() {
  return (
    <>
      <Heading />
      <NavBar />
      <Outlet />
    </>
  );
}