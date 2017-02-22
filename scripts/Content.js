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
        
        Socket.on('fb login success content', (data) => {
            console.log("Content received data:", data)
            this.setState({
                'isLoggedIn': data['isLoggedIn'],
                'user':data['user'],
                'messages': data['messages']['all_messages']
            });
        });
    }
    

    render() {
        if(this.state.isLoggedIn === 1){
            let messages = this.state.messages.map(
            (n,index) => <div key={index} className='messageContainer'><div>{n['user']}</div>
            <div>{n['text']} </div>
            </div>
            );
            return(
                // <div><h1> hello world</h1></div>
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