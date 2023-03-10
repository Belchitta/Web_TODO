import React from 'react'
<<<<<<< HEAD
=======
import {
    Link,Redirect
} from "react-router-dom";

>>>>>>> 61f256aea00144b6b28399642f06426cd796928f
import {
    Link,Redirect
} from "react-router-dom";


function NavbarItem({name, href}) {
    return (
<<<<<<< HEAD
        <li className="nav-item">
          <Link className="nav-link" to={href}>{name}</Link>
=======
        <li className="nav-item active">
<<<<<<< HEAD
          <a className="nav-link" to={href}>{name}</a>
=======
            <Link className="nav-link" to={href}>{name}</Link>
>>>>>>> main
>>>>>>> 61f256aea00144b6b28399642f06426cd796928f
        </li>
    )
}


export default function Navbar({navbarItems, auth, logout}) {
    let login_button = ''
    if (auth.is_login) {
    login_button = <button className="btn btn-outline-success my-2 my-sm-0" onClick={logout}>Hello, {auth.username} Logout</button>
    }
    else {
      login_button = <Link to='/login' className="btn btn-outline-success my-2 my-sm-0">Login</Link>
    }
    return (
<<<<<<< HEAD
            <nav class="navbar bg-body-tertiary">
                <div class="container-fluid">
                       <span class="navbar-brand mb-0 h1">TODO-Lists</span>
                </div>
                <div class="container-fluid_sec">
                    <span class="navbar-brand mb-1 h1">About</span>
                </div>
            </nav>
=======
<<<<<<< HEAD
        <nav className="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            <a className="navbar-brand" href="#">Fixed navbar</a>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarCollapse">
              <ul className="navbar-nav mr-auto">
                  {navbarItems.map((item) => <NavbarItem name={item.name} href={item.href} />)}
              </ul>
              <form className="form-inline mt-2 mt-md-0">
                <input className="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search" />
                <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                {/* {(auth.is_login) ? <Link to='/login' className="btn btn-outline-success my-2 my-sm-0">Login</Link> : <button className="btn btn-outline-success my-2 my-sm-0" onClick={logout}>Logout</button>} */}
                {login_button}

              </form>
            </div>
          </nav>
=======
        <nav className="navbar navbar-expand-sm bg-dark navbar-dark justify-content-end">
            <a className="navbar-brand" href="#">GeekBrains</a>
            {/*<button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse"*/}
            {/*        aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">*/}
            {/*    <span className="navbar-toggler-icon"></span>*/}
            {/*</button>*/}
            <div className="collapse navbar-collapse" id="navbarCollapse">
                <ul className="navbar-nav mr-auto">
                    {/*<li className="nav-item active">*/}
                    {/*    <div className="row">*/}
                    {/*        <div className="col-2">*/}
                                {navbarItems.map((item) => <NavbarItem name={item.name} href={item.href}/>)}
                            {/*</div>*/}
                        {/*</div>*/}
                    {/*</li>*/}
                </ul>
                <form className="form-inline mt-2 mt-md-0">
                    <input className="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search"/>
                    <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                </form>
            </div>
        </nav>
>>>>>>> main
>>>>>>> 61f256aea00144b6b28399642f06426cd796928f
    )
}
// export default Navbar