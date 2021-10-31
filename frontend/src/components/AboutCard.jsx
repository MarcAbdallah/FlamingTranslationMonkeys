import React, { Component } from 'react';
import { Card } from 'react-bootstrap';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faLinkedin } from '@fortawesome/free-brands-svg-icons'

class AboutCard extends Component {
    // this.props... url (img), name, desc
    render() {
        return(
            <Card style={{ minWidth: '14rem', maxWidth: '18rem', marginBottom: '10px', height: "45rem" }}>
                <Card.Img variant="top" src={this.props.img} />
                <Card.Body>
                    <Card.Title>{this.props.name}</Card.Title>
                    <Card.Subtitle className="mb-2 text-muted">{this.props.role}</Card.Subtitle>
                    <Card.Text>{this.props.bio}</Card.Text>
                </Card.Body>
                <Card.Footer className="text-muted">
                    <Card.Link href={this.props.linkedInUrl} style={{ textAlign: 'center', display: 'block' }}>
                        <FontAwesomeIcon icon={faLinkedin}></FontAwesomeIcon><>&nbsp;</>
                        LinkedIn
                    </Card.Link>
                </Card.Footer>
            </Card>
        );
    }
}

export default AboutCard;