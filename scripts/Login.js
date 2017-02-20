import * as React from 'react';
import {Socket} from './Socket';


export class ViewChat extends React.Component{
    handleViewChat(event){
        event.preventDefault();
        
        FB.getLoginStatus((response) => {
        if(response.status == 'connected'){
            Socket.emit('login status',{
                'facebook_user_token': response.authResponse.accessToken
            });
        }
    });
    }
    render(){
        
    }
}