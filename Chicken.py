import time
class Pet:
  health = 100
  patient = 100
  love = 100
  alive = True

  def __init__(self, name):
    self.name = name

    
  def help(self):
    return "All commands:\n\
      \tintroduse\n\
      \thug\n\
      \tfeed\n\
      \tflog\n\
      \tcaress\n\
      \tkill"

  def display_vital_statistics(self):
    print("\nCurrent stats:")
    print("\tname:      \t" + str(self.name))
    print("\thealth:    \t" + str(self.health))
    print("\tlove:      \t" + str(self.love))
    print("\tpatient:" + str(self.patient))
    print("\talive:     \t" + str(self.alive) + "\n\n")

  def introduse(self):
    if self.patient <=0:
      print("print 'rest' or admit your failure ")
    else:
      return "My name is " + self.nyoume

  def caress(self):
    if self.patient <=0:
      print("print 'rest' or admit your failure ")
    else:
      self.love += 10
      self.patient -= 10
      print(str(self.name)+"> \(｡•ㅅ•｡)♡")
      return "You are so sweet,master."


  def flog(self):
    if self.patient <=0:
      print("print 'rest' or admit your failure ")
    else:    
      self.patient+= 20
      self.love -= 10
      self.health -= 30
      print("ok...")
      time.sleep(1.5)
      print((str(self.name)+"> (☍﹏⁰。)\n\n")*20)
      time.sleep(1)
      return ("You toy had a really bad time")

  def kill(self):
    self.alive = False
    time.sleep(1)
    print (self.name+"> Goodbye, my love,for ever")
    return "Actually you are the toy"

  def feed(self):
    if self.patient <=0:
      print("print 'rest' or admit your failure ")
    else:     
      print("I had already told you toy doesn't need to eat anything,so what do you want?")
      time.sleep(1)
      print("Oh")
      time.sleep(1)
      print("I will do anything you want,my master")
      time.sleep(1)
      self.patient+= 10
      self.love -= 20
      self.health -= 5
      print(str(self.name)+"> (´ﾟдﾟ`)")
      time.sleep(0.5)
      return ("Your toys are full of food")
  

  def hug(self):
    if self.patient <=0:
      print("print 'rest' or admit your failure ")
    else: 
      self.patient-= 20
      self.love += 10
      print(str(self.name)+"> (つ´ω`)つ\n")
      time.sleep(1.5)
      return("Such a kid")

  def rest(self):
    self.patient+=10
    return("It's OK,have a rest")
    

      

  


    
print("Welcome to the omochatchi.")
time.sleep(0.5)
print("This is not tamagotchi,so you don't need to feed it.")
time.sleep(0.5)
print("Only you need to do is treating your toy like your self.")
time.sleep(0.5)


pet_name = input("Please, give a name for your little toy and let's start  \n")

pet = Pet(pet_name)

while pet.alive:
  pet.display_vital_statistics()
  wishes = input("Whats your wishes?\n")
  print("I will carry out any order you ask for, my master.\n")
  try:
    exec("print(pet." + wishes + "())")
  except:
    print("I don't know this command(write 'help' to get list of commands)")
  if pet.health <=0:
    print("You can stop now...She is dead,")
    time.sleep(0.5)
    print("Restar your window")
    pet.alive==False
    break
import time
class Pet:
  health = 100
  patient = 100
  love = 100
  alive = True

  def __init__(self, name):
    self.name = name

    
  def help(self):
    return "All commands:\n\
      \tintroduse\n\
      \thug\n\
      \tfeed\n\
      \tflog\n\
      \tcaress\n\
      \tkill"

  def display_vital_statistics(self):
    print("\nCurrent stats:")
    print("\tname:      \t" + str(self.name))
    print("\thealth:    \t" + str(self.health))
    print("\tlove:      \t" + str(self.love))
    print("\tpatient:" + str(self.patient))
    print("\talive:     \t" + str(self.alive) + "\n\n")

  def introduse(self):
    if self.patient <=0:
      print("print 'rest' or admit your failure ")
    else:
      return "My name is " + self.nyoume

  def caress(self):
    if self.patient <=0:
      print("print 'rest' or admit your failure ")
    else:
      self.love += 10
      self.patient -= 10
      print(str(self.name)+"> \(｡•ㅅ•｡)♡")
      return "You are so sweet,master."


  def flog(self):
    if self.patient <=0:
      print("print 'rest' or admit your failure ")
    else:    
      self.patient+= 20
      self.love -= 10
      self.health -= 30
      print("ok...")
      time.sleep(1.5)
      print((str(self.name)+"> (☍﹏⁰。)\n\n")*20)
      time.sleep(1)
      return ("You toy had a really bad time")

  def kill(self):
    self.alive = False
    time.sleep(1)
    print (self.name+"> Goodbye, my love,for ever")
    return "Actually you are the toy"

  def feed(self):
    if self.patient <=0:
      print("print 'rest' or admit your failure ")
    else:     
      print("I had already told you toy doesn't need to eat anything,so what do you want?")
      time.sleep(1)
      print("Oh")
      time.sleep(1)
      print("I will do anything you want,my master")
      time.sleep(1)
      self.patient+= 10
      self.love -= 20
      self.health -= 5
      print(str(self.name)+"> (´ﾟдﾟ`)")
      time.sleep(0.5)
      return ("Your toys are full of food")
  

  def hug(self):
    if self.patient <=0:
      print("print 'rest' or admit your failure ")
    else: 
      self.patient-= 20
      self.love += 10
      print(str(self.name)+"> (つ´ω`)つ\n")
      time.sleep(1.5)
      return("Such a kid")

  def rest(self):
    self.patient+=10
    return("It's OK,have a rest")
    

      

  


    
print("Welcome to the omochatchi.")
time.sleep(0.5)
print("This is not tamagotchi,so you don't need to feed it.")
time.sleep(0.5)
print("Only you need to do is treating your toy like your self.")
time.sleep(0.5)


pet_name = input("Please, give a name for your little toy and let's start  \n")

pet = Pet(pet_name)

while pet.alive:
  pet.display_vital_statistics()
  wishes = input("Whats your wishes?\n")
  print("I will carry out any order you ask for, my master.\n")
  try:
    exec("print(pet." + wishes + "())")
  except:
    print("I don't know this command(write 'help' to get list of commands)")
  if pet.health <=0:
    print("You can stop now...She is dead,")
    time.sleep(0.5)
    print("Restar your window")
    pet.alive==False
    break
  if pet.love <=0:
    print("You can stop now...She is dead,")
    time.sleep(0.5)
    print("Restar your window")
    pet.alive==False
    break

 
