import unittest
import swansonbot

class botTest(unittest.TestCase):
    
    def test_not_command(self):
        response = swansonbot.botResponses('treat yo self')
        self.assertEquals(response,"")
        
    def test_say_command(self):
        response = swansonbot.botResponses("!! say i want all the bacon")
        self.assertEquals(response, "i want all the bacon")
        
    def test_ls_command(self):
        response = swansonbot.botResponses("!! neigh")
        self.assertEquals(response, "Here's a wiki for poor lil' sebastian. http://parksandrecreation.wikia.com/wiki/Li'l_Sebastian")
        
    def test_knope_command(self):
        response = swansonbot.botResponses("!! notknope")
        self.assertEquals(response,"Leslie Knope 2012!")
        
    def parks_command(self):
        response = swansonbot.botResponses("!! park_info ca redwood")
        expected = "Here's some info on Redwood \n directions: <a href = 'http://www.nps.gov/redw/planyourvisit/directions.htm'> Get Directions</a>\
        \nWebsite: <a href='https://www.nps.gov/redw/index.htm'>https://www.nps.gov/redw/index.htm</a> \n Weather: Visitors should be prepared for cooler and damp weather. \
        Dress in layers and expect to get wet.\nYear-round temperatures along California's redwood coast: mid-40s\u00b0F (7\u00b0C) to mid-60s\u00b0F (18\u00b0C). \
        \n\nSummer can be foggy, with highs occasionally reaching low 70s\u00b0F (20\u00b0C). \
        \nWinters are cooler with considerable rain. October through April averages 60-80 inches of rain over the region."
        
if __name__ == '__main__':
    unittest.main()