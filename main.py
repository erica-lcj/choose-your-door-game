print('''
*******************************************************************************            
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
ejm        |__________|
*******************************************************************************
''')
print("Welcome.")
print("Your mission is to find treasure.") 
name = input("What's your name?\n")

print(f"{name}, crazy story, but you just woke up somewhere unfamiliar with none of your possesions. There is a path infront of you that forks left and right.")
c1 = input("Do you head left or right?\n") 
c_1 = c1.lower()
if c_1 == "left":
  print("After walking for 15 minutes, you come across a wide lake. The tide is high. You vaguely recall the Atomic Kitten song and wonder, should you swim or wait?")
  c2 = input("Swim or wait?\n")
  c_2 = c2.lower()
  if c_2 == "swim":
    print("The tide is high, and you're not moving on. The tide washed you away and you died. Kerry Katona is disapponited in you. Game Over.")
  else:
    print("You wait for the tide to pass, peforming a beatbox mashup of 2000s girl band music whilst you wait. You cross the lake with ease, and after climbing onto land, you're faced with three doors: one red, one blue, one yellow.")
    c3 = input("Which door do you open?\n")
    c_3 = c3.lower()
    if c_3 == "yellow":
     print("You open the yellow door, and discover 50 pieces of gold. You begin to celebrate, 25 coins richer... but then realise you're none the wiser about where you are or what to do. \nCongrats, I guess? At least you can look at the coins. Game over.")
    if c_3 == "blue":
      print(f"A man waits behind the door. He rises to greet you. \n'{name}, we've been waiting so long to see you. \n He looks at you in horror. {name}, don't you recognise me? Well... it's time we get you home. \n He approaches you, places his hands on your shoulders, and you pass out once again. \n Game over.")
    if c_3 == "red":
      print("fYou know, {name}, you learned in English class that red symbolised danger. As you step in the door, you detonate a mine. You are killed instantly. \nGame Over.")
      
else:
  print("You head right for several hours. Nothing of interest strikes you - until it does, literally. A goblin hits you on the shoulder with a rock. Now what?")
  c15 = input("Attack the goblin or Negotiate?\n")
  c_15 = c15.lower()
  if c_15 == "attack the goblin":
    print("That was stupid, you don't have a weapon. The goblin easily overpowers you. Game over, and rest in peace.")
  else:
      print("Wise choice. You begin bargaining with the goblin and find out he's angry because he can't swim. Ahead of you is a lake, and he says that infront of the lake lie three doors. Behind one is a treasure trove of gold.\n You have a choice - Kill the goblin and take the treasure, or thank the goblin and share the treasure?")
      c20 = input("Kill or Thank?\n")
      c_20 = c20.lower()
      if c_20 == "kill":
        print("That was really unnecessary, but I guess you have your reasons. You go for a swim and when you pull yourself up onto the land, you end up infront of three doors. Which one do you pick?")
        c21 = input("Blue, yellow, or red?\n")
        c_21 = c21.lower()
        if c_21 == "blue":
          print("Behind the door is a goblin mage. He knows you've killed his comrade, catches you off-guard, and ends your life. The treasure is not yours, and your life is not yours anymore, either. \nGame Over.")
        if c_21 == "yellow":
          print(f"You open the yellow door, and discover 50 pieces of gold. Was the life of another creature worth 50 pieces of gold? Yes, you decide, as you jump up and down in celebration. \n Congratulations, {name} you have won.")
        if c_21 == "red":
          print(f"You know, {name}, you learned in English class that red symbolised danger. As you step in the door, you detonate a mine. You are killed instantly. \nGame Over.")
      if c_20 == "thank":
          print("The goblin thanks you in return, and hypes you up to cross the river. You go for a swim and when you pull yourself up onto the land, you end up infront of three doors. Which one do you pick?")
          c25 = input("Blue, yellow, or red?\n")
          c_25 = c25.lower()
          if c_25 == "blue":
            print(f"Behind the door waits a wise goblin. He knows you were gracious and spared the life of his comrade. \n Wise goblin: {name}, we are glad you spared the life of our comrade. Please, take as much gold and material as you need, and we shall accompany you back to Londinium. \n The wise goblin opens chests full of armour, gold, jewellery, and other miscellaneous objects. You take as much as you need, and the goblins take you home. \n Congratulations, {name}, you win!")
          if c_25 == "yellow":
            print("You open the yellow door, and discover 50 pieces of gold. You swim back over and split the gold with the goblin. He's thankful, and you are 25 coins richer... but none the wiser about where you are or what to do. \nCongrats, I guess? Game over.")
          if c_25 == "red":
            print(f"You know, {name}, you learned in English class that red symbolised danger. As you step in the door, you detonate a mine. You are killed instantly. \nGame Over.")  
