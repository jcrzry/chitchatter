import * as React from 'react';
import * as ReactDOM from 'react-dom';

import { MessageForm } from './Button';
import { Content } from './Content';
import {FBLoginButton} from './Login';

ReactDOM.render(<FBLoginButton/>, document.getElementById('fbButton'));
ReactDOM.render(<Content />, document.getElementById('messageCenter'));
ReactDOM.render(<MessageForm />, document.getElementById('txtFld'));
