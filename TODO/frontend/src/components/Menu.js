import React from 'react'
import UserList from "./User";

function NavbarItem({name, href}) {
    return (
        <li className="nav-item active">
          <a className="nav-link" to={href}>{name}</a>
        </li>
    )
}


export default function Navbar({navbarItems}) {
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