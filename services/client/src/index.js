import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

class App extends Component {
    constructor() {
      super();
      this.state = {
        tweets: [],
      }
    }
    componentDidMount() {
      this.getTweets()
    }
    getTweets() {
        axios.get(`${process.env.REACT_APP_TWEETS_SERVICE_URL}/tweets`)
        .then((res) => { this.setState({tweets:res.data.tweets}) })
        .catch((err) => { console.log(err); });
      }
    render() {
      return (
        <section className="section">
          <div className="container">
            <div className="columns">
              <div className="column is-one-third">
                <br/>
                <h1 className="title is-1">All Users</h1>
                <hr/><br/>
                {
                  this.state.tweets.map((tweet) => {
                    return (
                      <h4
                        key={tweet.id}
                        className="box title is-4"
                      >{ tweet.name }
                      </h4>
                    )
                  })
                }
              </div>
            </div>
          </div>
        </section>
      )
    }
  };
  
  ReactDOM.render(
    <App />,
    document.getElementById('root')
  );