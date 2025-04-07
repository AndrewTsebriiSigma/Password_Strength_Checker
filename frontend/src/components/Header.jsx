import { useState } from 'react';


function Header() {
    const [password, setPassword] = useState('');

    return (
        <div className="header">
            <h1>Password Strength Checker</h1>
            <form action="">
                <label htmlFor="password">Enter Password</label>
                <input type="password" id="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)}/>
                <button type="submit">Check</button>
            </form>
        </div>
    )
}

export default Header;