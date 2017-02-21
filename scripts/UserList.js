import * as React from 'react';
import {Socket} from './Socket';



export class UserList extends React.Component{
    consructor(props){
        super(props);
        this.state ={
            'users':[]
        }
    }
    
    
    
    
    
    
    
    render(){
        let currentUsers = this.state.users.map(
             (n, index) => <div key={index}>{n}</div>
             );
        return(
             
            <div>
                {currentUsers}
            </div>
            )
            
        
    }
    
    
    
    
}