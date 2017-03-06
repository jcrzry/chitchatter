import * as React from 'react';
import {Socket} from './Socket';



export class UserList extends React.Component{
    constructor(props){
        super(props);
        this.state ={
            'connected_users':[],
            'numberOfUsers': 0,
            'isLoggedIn': 0
        };
    }
    
    componentDidMount(){
        Socket.on('login success', (data) => {
            this.setState({
                'connected_users' :  data['connected_users'],
                'numberOfUsers' : data['numberOfUsers'],
                'isLoggedIn' : data['isLoggedIn']
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
    
    
    render(){
        if(this.state.connected_users != undefined){
            let currentUsers = this.state.connected_users.map(
             (n, index) => <div className = 'userContainer' key={index}>
             <img className = 'userImg'src={n['imgLink']}/>
             <div><strong>{n['username']}</strong></div>
             </div>
             );
            return(
                 
                <div>
                    <h1> {this.state.numberOfUsers} Users Online</h1>
                    <div>{currentUsers}</div>
                </div>
            )}
            else{
                return(
                    <h2> No Users Online </h2>
                    )}
    }
    
    
    
    
}