import * as React from 'react';

import { MessageForm } from './Button';
import { Socket } from './Socket';

export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'user': [],
            'loggedIn': false,
            'messages': [] 
        };
    }

    componentDidMount(){
    
        Socket.on('all messages',(data) => {
            this.setState({
            'messages' : data['messages']
            });
        });
    }
    

    render() {
        if(!this.state.loggedIn){
            return (
                <div>
                    <div
                     className="fb-login-button"
                     data-max-rows="1"
                     data-size="medium"
                     data-show-faces="false"
                     data-auto-logout-link="true">
                    </div>
                </div>
            );
            
        }
        else{
           let messages = this.state.messages.map(
            (n, index) => <div className ="messageContainer" key={index}>{n}</div>
            );
            return (
                    <div>{messages}</div>
            ); 
        }
        
    }
}
