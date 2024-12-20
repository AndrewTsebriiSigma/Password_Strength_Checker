import { useState } from "react"
import '../App.css'

function Header() {
    const [response, setResponse] = useState('')

    function handleResponse() {
        setResponse("Strong") // retrieve response from model (either strong or weak)
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
                    <input type="text"/>
                    <button onClick={handleResponse}>Check</button>
                    <p>{response}</p>
                </div>
            </div>
        </>
    )
}

export default Header;