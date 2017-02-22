import * as React from 'react';

import { MessageForm } from './Button';
import { Socket } from './Socket';

export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'user': 0,
            'isLoggedIn': 0,
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
            console.log("Content received data:", data)
            this.setState({
                'isLoggedIn': data['isLoggedIn'],
                'user':data['user'],
                'messages' : data['messages']
            })
        })
    }
    

    render() {
        if(this.state.isLoggedIn === 1){
            let messages = this.state.messages.map(
            (n,index) => <div className='messageContainer' key={index}><div>{n['user']}</div>
            <div>{n['text']} </div></div>
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