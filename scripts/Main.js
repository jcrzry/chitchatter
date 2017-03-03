import * as React from 'react';
import * as ReactDOM from 'react-dom';

import { MessageForm } from './Button';
import { Content } from './Content';
import {LoginButtons} from './Login';
import {UserList} from './UserList';

ReactDOM.render(<LoginButtons/>, document.getElementById('fbButton'));
ReactDOM.render(<UserList/>, document.getElementById('userList'))
ReactDOM.render(<Content />, document.getElementById('messageCenter'));
ReactDOM.render(<MessageForm />, document.getElementById('txtFld'));
