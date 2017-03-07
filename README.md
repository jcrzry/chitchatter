#H1 Joshua Ryan Cruz
#Project 2 - H2.
##1. THEME
    The theme is pretty straight forward to begin with. It's going to revolve around the great city of Pawnee indiana. I think
    there will eventually be a more developed or refined theme. The theme is extended by the Ron Swansot, a helpful ron swanson bot. 
    I've expanded the theme by incorporating the national park service's beta api to retrieve information on this country's wonderful 
    places. The background is also a great ron swanson/pawnee tribute.
    
##2. KNOWN PROBLEMS:
1.Login Bar:
  1. When users logout of facebook, the facebook button still displays 'logout' as if they are logged in.
  2. pulling user information from my database. I have it, and I have a user id being returned currently. 
2.CSS:
  1. I would have enjoyed making it more responsive to window resizing as the size is somewhat statically set. As  
     is right now there could be some improvements to formatting.
  2. There is sometimes overflow in the messages, where message text will overflow out of the message container (rare).
3. MISC:
  1. Images are rendered inline, but if the dimensions are funny, they look weird (because of general css class).


##IMROVEMENTS:
1.THEME:
  1. There could be more elements revolving around pawnee and actual user images. I would also would have likeed to 
      include the use of pivate rooms. But this might be something to look into in the future.
2.APPEARANCE:
  1. I would have just wanted it to be have a unified style.
3. Unicode
  1. Emojis, I would have liked to add an emoji library to the chat.



# Regrading:
1. USERLIST: 
  1.  all connected users in a list is always visible
  2.  current number of connected users is always visible
2.BOT:
  1. chatbot is clearly identifiable
  2. bot messages room when people connect or leave
  3. !! about makes the bot message the room with a description
  4. !! help makes the bot message the room with a list of all commands
  5. !! say <something> makes the bot say <something> to the room
  6. 1 other command 'neigh'
  7. another command 'notknope'
  8. bot acknowledges unrecognized commands
3. CLIENTS:
  1.  all clients show new user on connect
  2.  all clients update count on connect
  3.  all clients remove user on disconnect
  4.  all clients update count on disconnect
  5.  database is not SQLite (barely noticed i didn't get points for this, but my db was set up as postgres since last submit..)
  6.  chat log at / loads with recent or all history (same as above)
  7.  messages are persisted via database (please see h1 repository)
  8.  user doesn’t count as connected user until authenticated
