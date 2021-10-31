import React, { Component } from 'react'
import { Container, Row, Col } from 'react-bootstrap'

import { members } from "../assets/aboutInfo"
import AboutCard from '../components/AboutCard';

class About extends Component {
    constructor() {
        super();
        this.state = {
            memberInfo: members
        }
        // console.log(this.state);
    }

    createMemberCards() {
        let cards = [];
        let memberInfo = this.state.memberInfo;

        const keys = Object.keys(memberInfo);
        keys.forEach((key) => {
            let m = memberInfo[key];
            cards.push(<Col className="d-flex">
                <AboutCard
                    key={m.id}
                    name={m.name}
                    role={m.job}
                    bio={m.bio}
                    img={m.img}
                    linkedInUrl={m.linkedin}>
                </AboutCard>
            </Col>);
        });

        return cards;
    }

    render() {
        return(
            <>
                <Container>
                    <Row style={{ marginTop: "60px"}}>
                        {this.createMemberCards()}
                        {/* <Col>             
                            <div style={{ padding: '30px', marginTop: '10px' }}>
                                <h1>{blurb.title}</h1>
                                <hr></hr>
                                <p className="lead">
                                    {blurb.text}
                                </p>
                            </div>
                        </Col> */}
                    </Row>
                </Container>
            </>
        );
    }
}

export default About;