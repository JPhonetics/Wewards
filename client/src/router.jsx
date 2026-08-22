import { createBrowserRouter } from 'react-router-dom'
import App from "./App"
import HomePage from "./pages/HomePage"
import NotFoundPage from "./pages/NotFoundPage"


const router = createBrowserRouter(
  [
    {
      path: "/",
      element: <App />,
      children: [
        {
          index: true,
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