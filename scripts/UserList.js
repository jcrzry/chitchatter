import * as React from 'react';
import {Socket} from './Socket';



export class UserList extends React.Component{
    constructor(props){
        super(props);
        this.state ={
            'connected_ users':[]
        };
    }
    
    componentDidMount(){
        Socket.on('fb login success', (data) => {
            this.setState({
                'connected_users' :  data['connected_users']
            });
        });
    }
    
    
    render(){
        if(this.state.connected_users != undefined){
            let currentUsers = this.state.connected_users.map(
             (n, index) => <div className = 'userContainer' key={index}>
             <img className = 'userImg'src={n['imgLink']}/>
             <div>{n['username']}</div>
             </div>
             );
            return(
                 
                <div>
                    {currentUsers}
                </div>
            )}
            else{
                return(
                    <h2> No Users Online </h2>
                    )}
    }
    
    
    
    
}