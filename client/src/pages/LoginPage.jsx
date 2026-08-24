import { useOutletContext } from 'react-router-dom';
import LoginCard from '../components/AuthForm/LoginCard';


export default function LoginPage() {

    const { setUser } = useOutletContext()

    return (
        <>

            <div>
                <br></br>
            </div>

            <div style = {{display: 'flex', justifyContent: 'center'}}>
                <LoginCard setUser = {setUser}/>
            </div>

        </>
    )
}