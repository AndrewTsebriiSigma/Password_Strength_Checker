import { useState } from 'react';
import { checkPassword } from '../../services/api';

function Header() {
    const [password, setPassword] = useState('');
    const [result, setResult] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await checkPassword(password);
            setResult(response.data);
        } catch (error) {
            console.error('Error checking password:', error);
        }
    };
    
    return (
        <div className="header">
            <h1>Password Strength Checker</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="password">Enter Password</label>
                <input 
                    type="password" 
                    id="password" 
                    name="password" 
                    value={password} 
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button type="submit">Check</button>
            </form>
            {result && (
                <div className="result">
                    <p>{result.message}</p>
                </div>
            )}
        </div>
    )
}

export default Header;