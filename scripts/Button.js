import * as React from 'react';
import { Socket } from './Socket';
import { MessageField } from './MessageField';

export class Button extends React.Component {
    handleSubmit(event) {
        event.preventDefault();

        let messageText = document.getElementById('messageText').val();
        
        console.log('message sent: ', messageText);
        Socket.emit('new message', {
            'message': messageText,
            // 'user' : username
        });
        console.log('message sent');
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <button>Send</button>
            </form>
        );
    }
}
