import { Outlet, useLoaderData } from 'react-router-dom';
import { useState } from 'react';
import Heading from './components/Heading/Heading';
import NavBar from "./components/NavBar";

export default function App() {

  const [user, setUser] = useState(useLoaderData())

  return (
    <>
      <Heading />
      <NavBar user={user} setUser={setUser} />
      <Outlet context={{ user, setUser }} />
    </>
  );
}