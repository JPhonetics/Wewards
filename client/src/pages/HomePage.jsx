import LoginCard from '../components/AuthForm/LoginCard'

export default function HomePage({ setUser }) {

    return (
        <>
            <h1>Welcome</h1>

            <div style={{display: 'flex', justifyContent: 'center'}}>
                <LoginCard setUser={setUser}/>
            </div>
        </>
    )
}