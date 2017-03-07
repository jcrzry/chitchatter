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
        self.assertEquals(response, "Here's a wiki for poor lil' sebastian. <a href='http://parksandrecreation.wikia.com/wiki/Li'l_Sebastian'>Info</a>")
        
    def test_knope_command(self):
        response = swansonbot.botResponses("!! notknope")
        self.assertEquals(response,"Leslie Knope 2012!")
        
    def test_parks_command(self):
        response = swansonbot.botResponses("!! park_info ca redwood")
        shortened = response[:16]
        print(shortened)
        expected = "Here's some info"
        self.assertEquals(shortened,expected)
        
    def test_parks_direction_command(self):
        response = swansonbot.botResponses("!! park_directions ca redwood")
        shortened = response[:24]
        print("shortened", shortened)
        self.assertEquals(response,"Here's the directions to Redwood National and State Parks: Redwood National and State Parks is located in northernmost coastal California - almost on the Oregon border. The parks are about 60-miles long, with four visitor centers from north to south.\n\nWe are a six to seven-hour drive (325 miles) north of San Francisco, a six-hour drive (330 miles) south of Portland, OR and a four-hour drive (170 miles) west of Redding, CA.")
        
    def test_link_wrapper(self):
        link = links.checkForLink("this is a message containing a link http://google.com")
        response = links.returnLink(link,links.isImage(link))
        self.assertEquals(response, "<a href='http://google.com'>http://google.com</a>")
    
    def test_img_wrapper(self):
        link = links.checkForLink("this is a message with an image https://photobucket.com/images/randomimage.jpg")
        response = links.returnLink(link,links.isImage(link))
        self.assertEquals(response, "<img class ='submittedImg' src='https://photobucket.com/images/randomimage.jpg'/>")
    
    def test_wrapped_message(self):
        response = links.getWrappedMessage("this message includes a link http://google.com")
        self.assertEquals(response,"this message includes a link <a href='http://google.com'>http://google.com</a>" )
    
    def test_wrapped_message_return_original(self):
        response = links.getWrappedMessage("this message does not include a link")
        self.assertEquals(response,"this message does not include a link")
    
    def test_help_message(self):
        response = swansonbot.botResponses("!! help")
        self.assertEquals(response,"Try one of these commands: about, \n say (i'll repeat something), \n neigh, \n notknope, \n park_info [State abreviation] [name] \n park_directions [State abreviation] [name]")

if __name__ == '__main__':
    unittest.main()