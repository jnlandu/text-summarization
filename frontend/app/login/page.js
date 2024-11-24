'use client';
import { useContext, useState } from "react";

import { useRouter } from "next/navigation";
import AuthContext from "../../context/AuthContext";

const Login = () => {
    const router = useRouter();
    const { login } = useContext(AuthContext);
    const [Email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        login(Email, password);
    };

    return (
        <div className="container login">
            <h2 className="hr">Sign in</h2>
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="Email" className="form-label">Username</label>
                    <input 
                        type="text" 
                        className="form-control" 
                        id="Email" 
                        value={Email} 
                        placeholder="Enter your email"
                        onChange={(e) => setEmail(e.target.value)} 
                        required 
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="password" className="form-label">Password</label>
                    <input 
                        type="password" 
                        className="form-control" 
                        id="password"
                        value={password}
                        placeholder="Enter your password"
                        onChange={(e) => setPassword(e.target.value)} 
                        required 
                    />
                <a href=""
                 onClick={() => router.push('/forgot-password/')}
                //  To be implemented
                 ><small>Forgot password ? </small> </a>
                </div>
                <button type="submit" className="btn btn-primary">Sign In</button>
            </form>
            <div className="d-flex container mt-3">
                <div className="flex-fill">
              <small>Don't have an account yet ? </small> 
              <a className="text-primary" href="#"
              onClick={() => router.push('/register/')}
              >Sign up</a>
              </div>
              <div className="flex-fill text-end">
                <a href="#"
                 onClick = {() => router.push('/admin/login')}
                 >
                <small className="text-primary">Admin ? </small>
                </a>
            </div>
          </div>
        </div>
    );
};

export default Login;
