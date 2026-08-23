import { useOutletContext } from 'react-router-dom';
import LoginCard from '../components/AuthForm/LoginCard';

export default function HomePage() {

    const { setUser } = useOutletContext()

    return (
        <>
            <h1>Welcome</h1>

            <div style={{display: 'flex', justifyContent: 'center'}}>
                <LoginCard setUser={setUser}/>
            </div>

        </>
    )
}