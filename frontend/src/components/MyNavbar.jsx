import React from 'react'
import { Container, Nav, Navbar, NavbarBrand } from "react-bootstrap";

function MyNavbar() {
    return (
        <Navbar collapseOnSelect expand="sm" bg="dark" variant="dark">
            <Container>
                <NavbarBrand href="/">EasyDubs</NavbarBrand>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                    <Navbar.Collapse className="justify-content-end" id="responsive-navbar-nav">
                        <Nav>
                            <Nav.Link href="/">Home</Nav.Link>
                            <Nav.Link href="/Service">Service</Nav.Link>
                            <Nav.Link href="/About">About</Nav.Link>
                        </Nav>
                    </Navbar.Collapse>
            </Container>
        </Navbar>
    )
}

export default MyNavbar