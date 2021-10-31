import React, { Component } from 'react'
import { Container, Row, Col } from 'react-bootstrap'

import FileUpload from '../components/FileUpload';

class Service extends Component {
    render() {
        return (
            <Container>
                <Row>
                    <Col>            
                        <FileUpload />
                    </Col>
                </Row>
            </Container>
        )
    }
}

export default Service;