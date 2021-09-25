import {React , useState }from 'react';

export default function Login() {
    const [form,setForm] = useState({
        username:'',
        password:'',
    })

    const formHandler = e => {
        const {name,value} = e.target
        setForm( prevState => {
            return {...prevState,[name]:value}
        })
    }
    return (
        <>
        <div className="Container">
            <div className="content">
                <div className="form-header">
                    <div className="text text-center bottom-line">Login</div>
                </div>
                <div className="form">
                    <form action="" type="POST">
                        <div className="Element">
                            <label className="text">Username :</label>
                            <input className="form-input"  name="username" value={form.username} onChange={formHandler} type="email"  required/>
                        </div>
                        <div className="Element">
                            <label className="text">Password :</label>
                            <input className="form-input" name="password" value={form.password} onChange={formHandler} type="password" required/>
                        </div>
                        <div className="form-btn">
                            <button className="btn btn-blue btn-big">Login</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
        </>
    )
}
