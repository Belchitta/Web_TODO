import React from 'react'
import {
    Link,Redirect
} from "react-router-dom";

import {
    Link
} from "react-router-dom";

function NavbarItem({name, href}) {
    return (
        <li className="nav-item active">
          <a className="nav-link" to={href}>{name}</a>
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
            <nav class="navbar bg-body-tertiary">
                <div class="container-fluid">
                       <span class="navbar-brand mb-0 h1">TODO-Lists</span>
                </div>
                <div class="container-fluid_sec">
                    <span class="navbar-brand mb-1 h1">About</span>
                </div>
            </nav>
    )
}
// export default Navbar