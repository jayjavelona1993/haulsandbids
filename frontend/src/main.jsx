import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import apollo_client from "@/apollo_client/apollo_client.js";
import {ApolloProvider} from "@apollo/client";
import GoogleMapsProvider from "@/GoogleMapsProvider.jsx";

createRoot(document.getElementById('root')).render(
  <StrictMode>
      <ApolloProvider client={apollo_client}>
          <GoogleMapsProvider>
            <App />
          </GoogleMapsProvider>

      </ApolloProvider>

  </StrictMode>,
)
