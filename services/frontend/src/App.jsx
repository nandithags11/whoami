import { useAuth0 } from "@auth0/auth0-react";
import { useState, useEffect } from "react";
import LoginButton from "./components/LoginButton";
import LogoutButton from "./components/LogoutButton";
import ProfileDisplay from "./components/ProfileDisplay";
import "./App.css";

function App() {
  const { user, isAuthenticated, getAccessTokenSilently, isLoading } = useAuth0();
  const [apiData, setApiData] = useState(null);
  const [error, setError] = useState(null);

  const callWhoAmI = async () => {
    try {
      setError(null);
      const token = await getAccessTokenSilently();

      const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}/whoami`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (!response.ok) throw new Error("Backend authentication failed");

      const data = await response.json();
      setApiData(data);
    } catch (err) {
      setError(err.message);
    }
  };

  useEffect(() => {
    if (isAuthenticated) {
      callWhoAmI();
    }
  }, [isAuthenticated]);

  if (isLoading) return <div className="loading">Loading Authentication...</div>;

  return (
    <div className="parent-container">
        <div className="container">
        <h1>Who Am I ?</h1>

        {!isAuthenticated ? (
            <div className="hero">
            <p>Please log in to verify your identity.</p>
            <LoginButton />
            </div>
        ) : (
            <div className="dashboard">
            <div className="user-info">
                <img src={user.picture} alt={user.name} className="avatar" />
                <ProfileDisplay data={apiData} />
                <div className="actions">
                <LogoutButton />
                </div>
            </div>

            {error && <p className="error-msg">{error}</p>}
            
            </div>
        )}
        </div>
    </div>
  );
}

export default App;