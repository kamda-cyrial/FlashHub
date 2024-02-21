import { Api } from '../api/api';
import { CustomState, LoginState, activePage, useCustomState, handleLogin } from '../utils';
import './forms.css';
import React, { useState, FormEvent } from 'react';
import GoogleAuth from '../api/GoogleAuth';

interface LoginProps {
    api: Api;
    loginState: CustomState<LoginState>;
    activePageState: CustomState<activePage>;
    clientId: CustomState<string>;
}


export default function Login({ api, loginState, activePageState, clientId }: LoginProps) {
    // const username = useCustomState<string>('');
    // const password = useCustomState<string>('');

    // const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    //     event.preventDefault();
    //     api.login(username.get(), password.get()).then((response) => {
    //         handleLogin(loginState, activePageState, response);
    //         console.log('cookie updated to:', document.cookie);
    //     }).catch((error) => {
    //         console.error(error);
    //     });
    // };

    return (
        <div>
            <form className="form-container">
                {/* <form onSubmit={handleSubmit} className="form-container"> */}
                {/* <h2 className="form-heading">Login</h2>
                <div className="form-field">
                    <label htmlFor="username">Username:</label>
                    <input
                        type="text"
                        id="username"
                        value={username.get()}
                        onChange={(e) => username.set(e.target.value)}
                        required
                    />
                </div>
                <div className="form-field">
                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        value={password.get()}
                        onChange={(e) => password.set(e.target.value)}
                        required
                    />
                </div>

                <div className="form-submit">
                    <button type="submit" className="form-button">Login</button>
                </div> */}
                <div className="form-field">
                    <GoogleAuth clientId={clientId.get()} api={api} activePageState={activePageState} loginState={loginState} />
                </div>
            </form>


        </div>
    );
}
