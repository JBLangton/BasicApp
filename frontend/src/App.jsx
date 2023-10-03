import React, { useState, useEffect } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';

function App() {
    const [count, setCount] = useState(0);
    const [users, setUsers] = useState([]);

    useEffect(() => {
        // Fetch users from the backend
        fetch('http://localhost:8000/users')
            .then((response) => response.json())
            .then((data) => setUsers(data))
            .catch((error) => console.error('Error fetching users:', error));
    }, []);

    return (
        <div className="App">
            {/* ...existing code... */}
            <div>
                <h2>Users:</h2>
                <ul>
                    {users.map((user) => (
                        <li key={user.id}>
                            {user.name} ({user.email})
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default App;
