import data

#w = open('data.py', 'w')

'''Class that creates + manages schedules for each user'''
class Schedule:

  def __init__(self, n: str, e: list):
    self.name = n
    self.events = e

  # Creates a string that displays a user friendly schedule for quick access
  def toString(self):
    # Will be the final product
    self.display = '    ┃  Sunday   ┃  Monday   ┃  Tuesday  ┃ Wednesday ┃ Thursday  ┃  Friday   ┃ Saturday\n━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━'
    
    # Finds what position the string writing is at, so there are no duplicates
    current = [0] * 7
    # Loops for each hour
    for i in range(24):
      '''Analyzing'''
      # Determines if the schedule text should be written
      apply = [0] * 7
      # Sets the amount of lines needed for each box
      lines = 1

      # Loops for each day in a week, sees if there is anything during the time
      for j in range(7):
        # Goes to the next iteration if the day's events have been exhausted
        if current[j] == -1:
          continue
        try:
          # Runs if the hour (i) is in the boundaries of the current list item of the day selected (j)
          if self.events[j][current[j]][1] <= i <= self.events[j][current[j]][2]:
            # Sets it so that the selected day (j) should be written
            apply[j] = 1
            # Sees the amount of lines needed to display the text in each box, and replaces the lines var if necessary
            if int(len(self.events[j][current[j]][0]) / 11) + 1 > lines:
              lines = int(len(self.events[j][current[j]][0]) / 11) + 1
            # Increments the current[j] by 1 if it's the final hour of the current event
        except:
          # Sets the current[day] to -1, which is impossible otherwise (for optimization)
          current[j] = -1
      
      # Adds the hour for each row, and aligns it as well
      if len(str(i)) == 2:
        self.display += '\n' + str(i) + '00│'
      else:
        self.display += '\n' + '0' + str(i) + '00│'
      
      '''Printing'''

      def addLine():
        # Loops for each day in a week
        for k in range(7):
          # If the selected day in the week needs text, the text in current[day] is added
          if apply[k]:
            # When more than one line is needed. A specific line is added, and apply[day] stays as 1
            if len(self.events[k][current[k]][0][11 * j:]) > 11:
              self.display += self.events[k][current[k]][0][11 * j:11 * (j+1)] + '│'
              print('ONE', self.events[k][current[k]][0][11 * j:11 * (j+1)] + '│')
            # Otherwise, the rest of the text is printed, and apply[day] is set to 0 for optimization
            else:
              self.display += self.events[k][current[k]][0][11 * j:] + (' ' * (11 - len(self.events[j][current[j]][0][11 * j:]))) + '│'
              print('TWO', self.events[k][current[k]][0][11 * j:] + (' ' * (11 - len(self.events[j][current[j]][0][11 * j:]))) + '│', self.events[j][current[j]][0][11 * j:])
              apply[k] = 0
          # Prints a blank box otherwise
          else:
            self.display += ' ' * 11 + '│'

      if lines == 1:
        # Sees if any part of the schedule needs to be inputted. If not, a blank row is printed (with column lines).
        if sum(apply) != 0:
          # Loops for each day in a week
          for j in range(7):
            # If the day applies, the text in current is added (with whitespace to make the table a table)
            if apply[j]:
              self.display += self.events[j][current[j]][0] + (' ' * (11 - len(self.events[j][current[j]][0]))) + '│'
            # Prints a blank box otherwise
            else:
              self.display += ' ' * 11 + '│'
        # Adds a blank row if nothing needs to be added
        else:
          self.display += (' ' * 11 + '│') * 7

      # Runs if the box needs more than one line
      else:
        # Loops for each line
        for j in range(lines):
          # Runs for the first line
          if j == 0:
            addLine()
          # Runs for the rest of the lines
          else:
            self.display += '\n    │'
            addLine()

      # Adds box boundary - ┼ or ┴ depending on the location
      if i == 24-1:
        self.display += '\n────┴' + '───────────┴'*6 + '───────────┘'
      else:
        self.display += '\n────┼' + '───────────┼'*6 + '───────────┤'
      
      # Increments current[day] up by one if the final hour of the event is passed
      for j in range(7):
        if i == self.events[j][current[j]][2]:
          current[j] += 1



  # Adds an event to the user's schedule
  def makeEvent(self):
    start = 0
    length = 0
    def inputattend():
      name=input("Name of the event?")
      time=input("When does this event start?")
      length=input("How long does this event last?")

  def makeachieve(self):
    name=""
    length=0
    def inputachieve():
      name=input("Name of the thing you want to do?")
      length=input("How long does this take?")

# Takes information from data.py to be used and updated
user = Schedule(data.name, data.events)
user.toString()
print(user.display)

''''''
# Initialized when the program is first ran. Uses info from data.py to decide this. (DOESN'T EXIST YET)


'''Page related variables/functions directly accessed by menu'''
# Variable for dividing different pages
divider = '━◦○◦━◦○◦━◦○◦━◦○◦━◦○◦━◦○◦━'

def scheduleView():
  
  def survey():
    pass

  if not user.firstTime:
    print(user.name + '\'s schedule:\n\n' +
          '')
  else:
    survey()
  
  input()

def scheduleChange():
  print()

def about():
  r = open('credits.txt', 'r')
  text = r.read()
  print(text)
  r.close()
  input()

# Dict of all the accessible subpages
pages = {'viewschedule': scheduleView,
         'changeschedule': scheduleChange,
         'about': about}

#w.write('users = [\'billy\', \'bob\', \'joe\']')
#users = ['billy', 'bob', 'joe']
while True:
  print(divider)
  print('''Welcome to PROGRAM NAME!
Access pages by typing the text of what you want to see. (eg. type "About" if you want to see the about page)

Menu: You are here!
View Schedule: View your schedule
Change Schedule: Add or remove events from your schedule.
About: See the point of this program, and the credits.
Exit: Exit the program, and save your schedule.\n''')

  # Changes the user's input so that keywords are less strict
  user = input().lower().replace(' ', '')
  if user == 'exit':
    print('\n' + divider)
    break
  elif not(user in pages):
    print('\nIt seems that what you inputted isn\'t in the menu list.')
  # Runs the user's wanted function when all above checks pass
  else:
    print('\n' + divider)
    pages[user]()

print("Have a nice day!")
try:
  w.close()
except:
  pass
quit()
