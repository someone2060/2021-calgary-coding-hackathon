import data

w = open('data.py', 'w')

'''Class that creates + manages schedules for each user'''
class Schedule:
  def __init__(n: str):
    name = n
    events = []

  # Adds an event to the user's schedule
  def makeEvent():
    start = 0
    length = 0
    def inputattend():
      name=input("Name of the event?")
      time=input("When does this event start?")
      length=input("How long does this event last?")

  def makeachieve():
    name=""
    length=0
    def inputachieve():
      name=input("Name of the thing you want to do?")
      length=input("How long does this take?")


'''Page related variables/functions'''
# Initialized when the program is first ran. Uses info from data.py to decide this. (DOESN'T EXIST YET)
def survey():
  print('survey')
  pass

def scheduleView():
  pass

def scheduleChange():
  pass

def about():
  r = open('credits.txt', 'r')
  print(r.read())

# Closes the program, removing writing variables if they exist
def exit():
  print('Have a nice day!')
  try:
    w.close()
  except:
    pass

# Dict of all the accessible subpages
pages = {'viewschedule': scheduleView(),
         'changeschedule': scheduleChange(),
         'about': about(),
         'exit': exit()}

# Main page to access other pages
def menu():

#w.write('users = [\'billy\', \'bob\', \'joe\']')
#users = ['boffa', 'joe', 'e']
while True:
  print('''Welcome to PUT NAME HERE!\nAccess pages by typing the text of what you want to see.\n
  Menu: You are here!\n
  View Schedule: View your schedule\n
  Change Schedule: Add or remove events.\n
  Schedule Remove: Remove events that you don't have anymore.\n
  About: See credits, and know the point of this program.\n
  Exit: Exit the program, and save your schedule.\n\n''')

  user = input().lower().replace(' ', '')
  if not(user in pages):
    print('It seems that what you inputted isn\'t in the menu list.')
    menu()
  else:
    pages[user]
