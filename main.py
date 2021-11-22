print('''
   _______________________-------------------                       `\
 /:--__                                                              |
||< > |                                   ___________________________/
| \__/_________________-------------------                         |
|                                                                  |
 |                       THE LORD OF THE RINGS                      |
 |                                                                  |
 |      "Three Rings for the Elven-kings under the sky,             |
  |        Seven for the Dwarf-lords in their halls of stone,        |
  |      Nine for Mortal Men doomed to die,                          |
  |        One for the Dark Lord on his dark throne                  |
  |      In the Land of Mordor where the Shadows lie.                 |
   |       One Ring to rule them all, One Ring to find them,          |
   |       One Ring to bring them all and in the darkness bind them   |
   |     In the Land of Mordor where the Shadows lie.                |
  |                                              ____________________|_
  |  ___________________-------------------------                      `\
  |/`--_                                                                 |
  ||[ ]||                                            ___________________/
   \===/___________________--------------------------
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice = input('Left or right?')
choice_lowered = choice.lower()

if choice_lowered == 'right':
  print('You are killed by the Orcs')
elif choice_lowered == 'left':
  choice2 = input("swim or wait?")
  choice2_lowered = choice2.lower()
  if choice2_lowered == 'swim':
    print("You are attacked by Stupid orc")
  elif choice2_lowered == 'wait':
    choose_door = input("which door?")
    choose_door_lowered = choose_door.lower()
    if choose_door_lowered == 'yellow':
      print("You win congrats!")
    else:
      print('You sucker lost')


 


