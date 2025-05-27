import { useState } from 'react';
import './App.css';

function App() {
  const [users, setUsers] = useState(null);
  const [usersLog, setUsersLog] = useState(null);

  const handleSubmit = (event) => {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const data = {
      name: formData.get('name'),
      user_name: formData.get('username'),
      email: formData.get('mail'),
      password: formData.get('pass'),
    };

    fetch('http://localhost:5000/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((result) => {
        console.log("Registered:", result);
        setUsers(result);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  const handleLogin = (event) => {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const data = {
      user_name: formData.get('username'),
      password: formData.get('password'),
    };

    fetch('http://localhost:5000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((result) => {
        console.log("Logged in:", result);
        setUsersLog(result);
        if(200 === result.status) {
          alert("Login successful");
        }
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  return (
    <>
      <div>
        <form onSubmit={handleSubmit}>
          <h1>New registration</h1>
          <label>Name</label><input name="name" type="text" placeholder='enter your name' /><br />
          <label>Username</label><input name="username" type="text" placeholder='user name' /><br />
          <label>Email</label><input name="mail" type="email" placeholder='email' /><br />
          <label>Password</label><input name="pass" type="password" placeholder='password' /><br />
          <input type="submit" value="Register" />
        </form>
      </div>

      <div>
        <form onSubmit={handleLogin}>
          <h1>Old registration</h1>
          <label>Username</label><input name="username" type="text" placeholder='user name' /><br />
          <label>Password</label><input name="password" type="password" placeholder='password' /><br />
          <input type="submit" value="Login" />
        </form>
      </div>

      <div>
        <h1>All users / Response</h1>
        <pre>{users && JSON.stringify(users, null, 2)}</pre>
      </div>
    </>
  );
}

export default App;
