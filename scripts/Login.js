import * as React from 'react';
import { Socket } from './Socket';

export class LoginButtons extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            'isLoggedIn':0,
            'loggedInFrom': 'none'
        };
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    
    componentDidMount(){
        Socket.on('login success', (data) => {
            console.log('data',data);
            this.setState({
                'isLoggedIn' : data['isLoggedIn'],
                'loggedInFrom': data['loggedInFrom']
            });
        });
    }
    
    handleSubmit(event){
        event.preventDefault();
        FB.getLoginStatus((response) => {
           if (response.status == 'connected') {
               console.log('this is the fb response:',response);
               Socket.emit('login complete', {
                   'fb_user_token': response.authResponse.accessToken,
                   'google_user_token': ''
               });
                console.log('token sent to server');
           } else{
               let auth = gapi.auth2.getAuthInstance();
               let user = auth.currentUser.get();
               if(user.isSignedIn()){
                   console.log("this is the google response:", user.getAuthResponse());
                   Socket.emit('login complete', {
                       'google_user_token': user.getAuthResponse().id_token,
                       'fb_user_token': ''
                   });
               }
           }
       });
    }
      render() {
        if(!this.state.isLoggedIn){
            return (
                <div>
                    <div
                     className="fb-login-button"
                     data-max-rows="1"
                     data-size="medium"
                     data-show-faces="false"
                     data-auto-logout-link="true">
                    </div>
                    <div
                        className="g-signin2"
                        data-theme="dark">
                     </div>
                     <form onSubmit={this.handleSubmit}>
                        <input type = 'submit' value='Go to Chat'/>
                    </form>
                </div>
            );
        }
        else if(this.state.loggedInFrom === 'fb'){
            return(
                    <div
                     className="fb-login-button"
                     data-max-rows="1"
                     data-size="medium"
                     data-show-faces="false"
                     data-auto-logout-link="true">
                    </div>
                );
        }
        else if(this.state.loggedInFrom === 'google'){
            return(
                <div
                        className="g-signin2"
                        data-theme="dark">
                </div>
                )
        }
              
    }
}