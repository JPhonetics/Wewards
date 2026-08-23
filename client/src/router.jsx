import { createBrowserRouter } from 'react-router-dom';
import App from './App';
import HomePage from './pages/HomePage';
import ErrorPage from './pages/ErrorPage';
import NotFoundPage from './pages/NotFoundPage';

import { redirectIfLoggedIn, userConfirmation } from './utilities';


const router = createBrowserRouter(
  [
    {
      path: "/",
      element: <App />,
      loader: userConfirmation,
      errorElement: <ErrorPage />,
      children: [
        {
            index: true,
            element: <HomePage />,
            loader:redirectIfLoggedIn,
        },
        {
            path: "home",
            element: <HomePage />,
        },
        {
            path: '*',
            element: <NotFoundPage />
        }
      ],
    },
  ]
);

export default router;