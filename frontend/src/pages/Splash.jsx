import React, { Component } from 'react'
import { Button, Container, Row, Col } from 'react-bootstrap'
import cinemaImg from "../assets/img/cinema.png"

class Splash extends Component {
    // TODO: Center this garbage
    render() {
        return (
            <Container style={{ height: "100%"}}>
                <Row>
                    <Col className="d-flex justify-conter-center align-items-center">
                        <img src={cinemaImg} alt="A bustling cinema." style={{maxWidth: "100%", maxHeight: "100%"}}/>
                    </Col>
                    <Col className="d-flex align-items-center">
                        <div>
                            <h1>AI Generated Dubbing</h1>
                            <h5>Discover a whole new world of revolutionary cinema and artistry</h5><br/>
                            <Button variant="dark" href="/Service">Try Now!</Button>
                        </div>
                    </Col>
                </Row>
            </Container>
        )
    }
}

export default Splash;