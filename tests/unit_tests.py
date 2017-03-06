import unittest
import swansonbot
import links

class botTest(unittest.TestCase):
    
    def test_not_command(self):
        response = swansonbot.botResponses('treat yo self')
        self.assertEquals(response,"")
        
    def test_unrecognized_command(self):
        response = swansonbot.botResponses("!! eagleton")
        self.assertEquals(response,"I'm not sure what you're trying to say...You must be from Eagleton.")
        
    def test_say_command(self):
        response = swansonbot.botResponses("!! say i want all the bacon")
        self.assertEquals(response, "i want all the bacon")
        
    def test_ls_command(self):
        response = swansonbot.botResponses("!! neigh")
        self.assertEquals(response, "Here's a wiki for poor lil' sebastian. http://parksandrecreation.wikia.com/wiki/Li'l_Sebastian")
        
    def test_knope_command(self):
        response = swansonbot.botResponses("!! notknope")
        self.assertEquals(response,"Leslie Knope 2012!")
        
    def test_parks_command(self):
        response = swansonbot.botResponses("!! park_info ca redwood")
        expected = "Here's some info on Redwood \n directions: <a href = 'http://www.nps.gov/redw/planyourvisit/directions.htm'> Get Directions</a>\
        \nWebsite: <a href='https://www.nps.gov/redw/index.htm'>https://www.nps.gov/redw/index.htm</a> \n Weather: Visitors should be prepared for cooler and damp weather. \
        Dress in layers and expect to get wet.\nYear-round temperatures along California's redwood coast: mid-40s\u00b0F (7\u00b0C) to mid-60s\u00b0F (18\u00b0C). \
        \n\nSummer can be foggy, with highs occasionally reaching low 70s\u00b0F (20\u00b0C). \
        \nWinters are cooler with considerable rain. October through April averages 60-80 inches of rain over the region."
        self.assertEquals(response,expected)
        
    def test_parks_direction_command(self):
        response = swansonbot.botResponses("!! park_directions ca redwood")
        self.assertEquals(response," Directions: Redwood National and State Parks is located in northernmost coastal California - almost on the Oregon border. The parks are about 60-miles long, with four visitor centers from north to south.\
        \n\nWe are a six to seven-hour drive (325 miles) north of San Francisco, a six-hour drive (330 miles) south of Portland, OR and a four-hour drive (170 miles) west of Redding, CA.")
    
    def test_link_wrapper(self):
        link = links.checkForLink("this is a message containing a link http://google.com")
        response = links.returnLink(link,links.isImage(link))
        self.assertEquals(response, "<a href='http://google.com'>http://google.com</a>")
    
    def test_img_wrapper(self):
        link = links.checkForLink("this is a message with an image https://photobucket.com/images/randomimage.jpg")
        response = links.returnLink(link,links.isImage(link))
        self.assertEquals(response, "<img src ='https://photobucket.com/images/randomimage.jpg'/>")
    
    def test_wrapped_message(self):
        response = links.getWrappedMessage("this message includes a link http://google.com")
        self.assertEquals(response,"this message includes a link <a href='http://google.com'>http://google.com</a>" )
    
    def test_wrapped_message_return_original(self):
        response = links.getWrappedMessage("this message does not include a link")
        self.assertEquals(response,"this message does not include a link")


if __name__ == '__main__':
    unittest.main()