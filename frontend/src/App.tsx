import { useState } from 'react';
import './App.css';

function App() {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState("");

  const fetchUsers = async () => {
    try {
      const res = await fetch('http://127.0.0.1:5000/users');
      if (!res.ok) {
        throw new Error("Failed to load users");
      }
      const users = await res.json();
      setUsers(users);  // Set the list of users
      setError("");
    } catch (er) {
      setError(er instanceof Error ? er.message : String(er));
      setUsers([]);
    }
  };

  return (
    <div>
      <h1>All Users / Response</h1>
      <button onClick={fetchUsers}>Click</button>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {users.length > 0 ? (
        <ul>
          {users.map((user) => (
            <li key={user.id}>
              <strong>{user.name}</strong> ({user.user_name}) - {user.email}
            </li>
          ))}
        </ul>
      ) : (
        <p>No users loaded yet.</p>
      )}
    </div>
  );
}

export default App;
