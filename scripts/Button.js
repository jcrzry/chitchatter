import * as React from 'react';
import { Socket } from './Socket';
// import { MessageField } from './MessageField';

export class MessageForm extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            'chatroomID':1,
            'value': "",
            'user':[],
            'isLoggedIn':false
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }
    handleChange(event){
        this.setState({value: event.target.value});
    }
    
    handleSubmit(event) {
        let messageText = this.state.value;
        event.preventDefault();
        if(this.state.value.trim() !== ""){
             console.log('message', this.state.value)
             Socket.emit('new message', {
            'message': messageText,
            'user' : this.state.user['userID'],
            'roomID':this.state.chatroomID
        });
        }
       
    }
    componentDidMount(){
        Socket.on('fb login success', (data) =>{
            this.setState({
                'isLoggedIn': data['isLoggedIn'],
                'user':data['user']
            })
        })
    }

    render() {
        if(this.state.isLoggedIn){
           return (
            <form onSubmit={this.handleSubmit}>
                <textarea value ={this.state.value} onChange = {this.handleChange} placeholder="Enter mesaage.." />
                <input type = "submit" value = "Send"/>
            </form>
            ); 
        }
        else{
            return null;
        }
        
    }
}
