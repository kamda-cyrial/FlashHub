import './App.css';
import Navbar from './components/Navbar/Navbar';
import Login from './components/Login/Login';
import { useCustomState, LoginData, activePage, parseCookies } from './components/utils';
import { Api, MockApi } from './components/api/api';
import FlashCard from './components/FlashCard/FlashCard';
import { Card } from './components/FlashCard/utils';
import { useEffect } from 'react';
import google_oauth_client from './components/api/google_oauth_client.json';
import Profile from './components/profile/Profile';
import { LoginState } from './components/utils';
function App() {

    const api: Api = new MockApi();
    const loginState = useCustomState<LoginState>(new LoginState());
    const activePageState = useCustomState<activePage>("login");
    const cards = useCustomState<Card[]>([]);
    const clientId = useCustomState<string>('');

    useEffect(() => {

        parseCookies(loginState, activePageState, api);

        api.getCards('flashcard_id').then((response) => {
            console.log(response);
            cards.set(response);
        }

        ).catch((error) => {
            console.error(error);
        });

        console.log('cloudAuth Data:', google_oauth_client.web.client_id);
        clientId.set(google_oauth_client.web.client_id);

    }, []);
    return (
        <>
            <Navbar loginState={loginState} activePageState={activePageState} />
            {(() => {
                switch (activePageState.get()) {
                    case "flashcard":
                        return <FlashCard cards={cards} />;
                    case "profile":
                        return <Profile avatarName={loginState.get().first_name} loginState={loginState} />
                    default:
                        return <Login api={api} loginState={loginState} activePageState={activePageState} clientId={clientId} />;
                }
            })()}
        </>
    );
}

export default App;