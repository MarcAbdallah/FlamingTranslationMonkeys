import React, { Component } from "react";
import {
    BrowserRouter as Router,
    Switch,
    Route
  } from 'react-router-dom' 

import About from "../pages/About";
import Service from "../pages/Service";
import Splash from "../pages/Splash";

class Routes extends Component {
    render() {
        return(
            <Router>
                <Switch>
                    <Route exact path="/">
                        <Splash />
                    </Route>
                    <Route exact path="/about">
                        <About />
                    </Route>
                    <Route exact path="/service">
                        <Service />
                    </Route>
                </Switch>
            </Router>
        );
    }
}

export default Routes;