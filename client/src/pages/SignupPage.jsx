import { useOutletContext } from 'react-router-dom';
import SignupCard from '../components/AuthForm/SignupCard';


export default function SignupPage() {

    const { setUser } = useOutletContext()

    return (
        <>

            <div>
                <br></br>
            </div>

            <div style = {{display: 'flex', justifyContent: 'center'}}>
                <SignupCard setUser = {setUser}/>
            </div>

        </>
    )
}