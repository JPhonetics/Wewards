import { createBrowserRouter } from 'react-router-dom';
import App from './App';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import SignupPage from './pages/SignupPage';
import UserDashboard from './pages/user/UserDashboardPage';
import UserProfilePage from './pages/user/UserProfilePage';
// import RegisterBusinessPage from './pages/RegisterBusinessPage';
// import BusinessDashboard from './pages/business/BusinessDashboard'
import ErrorPage from './pages/ErrorPage';
import NotFoundPage from './pages/NotFoundPage';

import { requireLogin, redirectIfLoggedIn, userConfirmation } from './api/AccountsAPI';


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
        },
        {
          path: 'login',
          element: <LoginPage />,
          loader: redirectIfLoggedIn,
        },
        {
          path: 'signup',
          element: <SignupPage />,
          loader: redirectIfLoggedIn,
        },
        {
          path: "user/dashboard",
          element: <UserDashboard />,
          loader: requireLogin,
        },
        {
          path: "user/profile",
          element: <UserProfilePage />,
          loader: requireLogin,
        },
        // {
        //   path: "business/register",
        //   element: <RegisterBusinessPage />,
        // },
        // {
        //   path: "business/dashboard",
        //   element: <BusinessDashboard />,
        //   loader: requireLogin,
        // },
        {
          path: '*',
          element: <NotFoundPage />
        },
      ],
    },
  ]
);

export default router;