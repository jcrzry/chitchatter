#socketio_tests.py

import app, unittest

class SocketioTestCases(unittest.TestCase):
    def test_server_connect(self):
        client = app.socketio.test_client(app.app)
        r = client.get_received()
        
        self.assertEquals(len(r), 1)
        from_server = r[0]
        self.assertEquals(
            from_server['name'], 
            'isConnected'
        )
        data = from_server['args'][0]
        self.assertEquals(data['connected'], 1)
    
    def test_message_relay_response(self):
        client = app.socketio.test_client(app.app)
        
        client.emit("new message", {'message': "this is a test message!!", 'userID' : 1, 'roomID': 1})
        r = client.get_received()
        from_server = r[1]
        # print r
        self.assertEquals(len(r),2)
        
        self.assertEquals(len(r[0]),3)
        mess_path = r[1]['args'][0]['messages']['all_messages']
        response = mess_path[len(mess_path)-1]['text']
        self.assertEquals(response, "this is a test message!!")
        
    def test_client_login_join_room(self):
        client = app.socketio.test_client(app.app)
        client.emit('test client login', {'userID': 12322})
        from_server = client.get_received()
        room  =from_server[1]['args'][0]['room']
        self.assertEquals(room, 12322)
        
    def test_client_logout_response_to_all(self):
        client = app.socketio.test_client(app.app)
        client.emit('logout', {'userID':1})
        r = client.get_received()
        response = r[1]['name']
        # print response
        self.assertEquals(response, "someone left")
if __name__ == '__main__':
    unittest.main()
