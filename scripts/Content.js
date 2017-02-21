import * as React from 'react';

import { MessageForm } from './Button';
import { Socket } from './Socket';

export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'user': [],
            'loggedIn': false,
            'messages': [],
            'chatroomID': 1
        };
    }

    componentDidMount(){
        Socket.on('all messages',(data) => {
            this.setState({
            'messages' : data['messages']
            });
        });
        Socket.on('fb login success', (data) =>{
            this.setState({
                'isLoggedIn': data['isLoggedIn'],
                'user':data['user']
            })
        })
    }
    

    render() {
        if(this.state.loggedIn){
            let messages = this.state.messages.map(
            (n,index) => <div className='messageContainer' key={index}>{n.text} </div>
            );
            return(
                <div>{messages}</div>
                );
        }
        else{
            return(
                <h1>You Must Be Logged In to Participate.</h1>
            );
        }
        
            
       
    }
}
