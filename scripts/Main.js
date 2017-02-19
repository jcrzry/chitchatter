import * as React from 'react';
import * as ReactDOM from 'react-dom';

import { MessageForm } from './Button';
import { Content } from './Content';

ReactDOM.render(<Content />, document.getElementById('messageCenter'));
ReactDOM.render(<MessageForm />, document.getElementById('txtFld'));
