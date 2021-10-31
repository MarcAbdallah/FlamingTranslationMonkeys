import React, { Component } from 'react'
import { Container, Row, Col } from 'react-bootstrap'

import AIDubbing from '../components/AIDubbing';

class Service extends Component {
    render() {
        return (
            <Container>
                <Row className="d-flex justify-content-center" style={{ marginTop: "50px"}}>
                    <Col>            
                        <AIDubbing />
                    </Col>
                </Row>
            </Container>
        )
    }
}

export default Service;