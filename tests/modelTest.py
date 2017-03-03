import models

def fillUsers():
    chat = models.chatroom("public",True)
    user1 = models.user("jcrzry","https://i.ytimg.com/vi/ptkytDOVFN0/maxresdefault.jpg")
    user2 = models.user("userDos","http://www.rd.com/wp-content/uploads/sites/2/2016/04/01-cat-wants-to-tell-you-laptop.jpg")
    models.db.session.add(chat)
    models.db.session.add(user1)
    models.db.session.add(user2)
    models.db.session.commit()
    
def fillMessages():
    mess1 = models.message(1,1,"this is a dirst test message")
    mess2 = models.message(1,2,"this is response message")
    mess3 = models.message(1,1,"response to user dos")
    mess4 = models.message(1,2, "USER 2 reply")
    models.db.session.add(mess1)
    models.db.session.add(mess2)
    models.db.session.add(mess3)
    models.db.session.add(mess4)
    models.db.session.commit()
    
