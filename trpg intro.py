input ('''                   Hello! And welcome to''')
input ('''
 \_\_\_\_\_  \_          \_\_\_\_\_  \_      \_  \_\_\_\_\_
  \_      \_  \_          \_      \_  \_      \_  \_      \_
   \_\_\_\_\_  \_          \_\_\_\_\_  \_\_\_\_\_  \_\_\_\_\_
    \_      \_  \_          \_          \_      \_  \_      \_
     \_      \_  \_          \_          \_      \_  \_      \_
      \_      \_  \_\_\_\_\_  \_          \_      \_  \_      \_

        \_\_\_\_\_  \_      \_  \_\_\_\_\_  \_\_\_\_\_  \_\_\_\_\_
         \_      \_  \_      \_  \_          \_              \_
          \_      \_  \_      \_  \_\_\_      \_\_\_\_\_      \_
           \_      \_  \_      \_  \_                  \_      \_
            \_      \_  \_      \_  \_                  \_      \_
             \_\_\_\_\_  \_\_\_\_\_  \_\_\_\_\_  \_\_\_\_\_      \_''')
name = input('''                               What's your name?
''').strip().title()
yn = input('Oh! So your name is ' +name +' right? (Y/N)').strip().title()
if yn == ('Y'):
    print ('''GAME START''')
#Game goes here
    
if yn == ('N'):
    input ("Oh?")
    input ("So that's not your name?")
    input ("Well then...")
    input ("I suppose we could sit here for a while and do nothing")
    input ("Or instead, here's an idea, you could tell me your REAL name!")
    input ("Sound good?")
#Back to "What's your name?"
if yn != ('N','Y'):
    input ("Sorry, I don't know what that means, answer Y for yes or N for no")
#Back to "So your name is___________?"
