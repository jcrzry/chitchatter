import * as React from 'react';
import { Socket } from './Socket';
// import { MessageField } from './MessageField';

export class MessageForm extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            'chatroomID':1,
            'value': "",
            'user':{},
            'isLoggedIn':0,
            'messages': []
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }
    handleChange(event){
        this.setState({value: event.target.value});
    }
    
    handleSubmit(event) {
        event.preventDefault();
        console.log("userID",this.state.user['userID']);
        let messageText = this.state.value;
        if(messageText.trim() !== ""){
             console.log('message:', this.state.value)
             Socket.emit('new message', {
            'message': messageText,
            'userID' : this.state.user['userID'],
            'roomID':this.state.chatroomID
        });
        this.setState({
            'value' :''
        });
        }
       
    }
    componentDidMount(){
        Socket.on('login success', (data) => {
            console.log("button received data: ", data)
            this.setState({
                'isLoggedIn': data['isLoggedIn'],
                'user': data['user'],
                'messages': data['all_messages']
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
           return (
            <form onSubmit={this.handleSubmit}>
                <textarea className = 'textField' value ={this.state.value} onChange = {this.handleChange} placeholder="Enter mesaage.." />
                <input type = "submit" value = "Send"/>
            </form>
            ); 
        }
        else{
            return null;
        }
        
    }
}
