import * as React from 'react';
import { Socket } from './Socket';


export class FBLoginButton extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            'isLoggedIn':0
        }
    }
      render() {
       FB.getLoginStatus((response) => {
           if (response.status == 'connected') {
               console.log('this is the fb response:',response);
               Socket.emit('fb login complete', {
                   'facebook_user_token': response.authResponse.accessToken,
               });
                console.log('token sent to server');
           }
       });
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
}