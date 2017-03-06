#integration_tests
import app, flask_testing 
import unittest, urllib2, json

class ServerIntegrationTest(flask_testing.LiveServerTestCase):
    
    def create_app(self):
        return app.app
    
    def test_server_is_running(self):
        resp = urllib2.urlopen(self.get_server_url())
        
        # 200 code means connection was ok
        self.assertEquals(resp.code,"200") 
        
if __name__ == '__main__':
    unittest.main()