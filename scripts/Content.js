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
            console.log("messages received:", data['messages']['all_messages'])
            this.setState({
            'messages' : data['messages']['all_messages']
            });
        });
        
        Socket.on('login success', (data) => {
            console.log("Content received data:", data)
            this.setState({
                'isLoggedIn': data['isLoggedIn'],
                'user':data['user'],
                'messages': data['messages']['all_messages']
            });
        });
        Socket.on('someone left', (data) => {
            this.setState({
                'connected_users' :  data['connected_users'],
                'numberOfUsers' : data['numberOfUsers']
            });
        });
        Socket.on('i left', (data) => {
            this.setState({
                'isLoggedIn' : data['isLoggedIn']
            });
        });
    }
    

    render() {
        if(this.state.isLoggedIn === 1){
            let messages = this.state.messages.map(
            (n,index) => <div className = 'messageContainer'key={index}>
            <div className = 'userContainer'>
                <img className='userImg' src={n['user']['imgLink']}/>
                <div>{n['user']['username']}</div>
                </div>
            <div className = 'messageTextContainer'>{n['text']} </div>
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