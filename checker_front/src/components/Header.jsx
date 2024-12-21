import { useState, useEffect } from "react"
import axios from 'axios'
import '../App.css'

function Header() {
    const [userInput, setUserInput] = useState('');
    const [response, setResponse] = useState('');
    const [status, setStatus] = useState('');

    function handleChange(e) {
        setUserInput(e.target.value);
    }

    function sendData() {
        axios.post('http://127.0.0.1:5000/api/password', {input: userInput})
        .then(r => {
            setResponse(r.data.message)
        }).catch(err => {
            console.log('Error: ', err)
        });
    }

    return (
        <>
            <div className="description">
                <h1>How Secure is Your Password?</h1>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Dignissimos iste ducimus architecto nam illum maiores fuga iure porro, quaerat, repellat, quidem provident. 
                    Quis, tenetur. Ut id doloremque et consectetur neque.
                </p>

                <div className="inputField">
                    <label htmlFor="">Enter your password:</label>
                    <input type="text" value={userInput} onChange={handleChange} placeholder="Enter password here..."/>
                    <button onClick={sendData}>Check</button>
                    <p>{response}</p>
                </div>
            </div>
        </>
    )
}

export default Header;