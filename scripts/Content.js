import * as React from 'react';

import { MessageForm } from './Button';
import { Socket } from './Socket';

export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
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
        let messages = this.state.messages.map(
            (n, index) => <div className ="messageContainer" key={index}>{n}</div>
        );
        return (
                <div>{messages}</div>
        );
    }
}
