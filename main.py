import data, eventfile

#eventlist=[]

dataA = open('data.py', 'a')

'''Class that creates + manages schedules for a user'''
class Schedule:

  def __init__(self, n: str, e: list):
    self.name = n
    self.events = e
    # Sees if there is anything in the user's events. If there is nothing, firstTime is toggled, and survey is ran.
    self.firstTime = True
    for i in self.events:
      if len(i) > 0:
        self.firstTime = False
        break

  # Creates a string that displays a user friendly schedule for quick access
  def toString(self):
    # Will be the final product
    self.display = '     ┃  Sunday   ┃  Monday   ┃  Tuesday  ┃ Wednesday ┃ Thursday  ┃  Friday   ┃ Saturday  ┃\n━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━┩'
    
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
          if self.events[j][current[j]][1] <= i <= self.events[j][current[j]][2] - 1:
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
        self.display += '\n' + str(i) + ':00│'
      else:
        self.display += '\n' + '0' + str(i) + ':00│'
      
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
            # Otherwise, the rest of the text is printed, and apply[day] is set to 0 for optimization (BUG: When multi line text runs through this part, the whitespace that gets subtracted somehow becomes blank [\'EP\' becomes \'\'] and full whitespace is shown. For some reason, it doesn\'t apply to three line text.)
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
          # Runs the first loop time
          if j == 0:
            addLine()
          # Runs for the rest of the loop times
          else:
            self.display += '\n    │'
            addLine()

      # Adds box boundary (┼ or ┴ depending on the location). 24 is from hours in a day
      if i == 24 - 1:
        self.display += '\n─────┴' + '───────────┴'*6 + '───────────┘'
      else:
        self.display += '\n─────┼' + '───────────┼'*6 + '───────────┤'
      
      # Increments current[day] up by one if the final hour of the event is passed
      for j in range(7):
        if i == self.events[j][current[j]][2]:
          current[j] += 1

  # Tries to find an event with the name given. Is case sensitive. Returns all instances of the event when it works; returns False otherwise.
  def findEvent(self, day: int, name: str):
    instances = []
    # Loops for every day in self.events
    for i in self.events:
      # Loops for every event in a selected day
      for j in i:
        # Finds if the selected event is the same as 
        if j[0] == name:
          instances.append(j)
    # Runs when instances has no length (ie found nothing)
    if not len(instances):
      return False
    return instances

  # Adds an event to self.events, and puts it in the correct place. Returns a bool reporting if the action was successful or not. 
  def addEvent(self, day: int, name: str, startH: int, endH: int) -> bool:
    # startH must be less than endH for the function to work
    if startH >= endH:
      return False
    
    # if endH is less than the first event, then the event wanted to be added will be in the right place and will be slotted in. Also works if there are no events in the selected day.
    if endH <= self.events[day][0][1] or len(self.events[day]) == 0:
      self.events[day].insert(0, [name, startH, endH])
      return True
    # Loops for each item
    for i in range(len(self.events[day]) - 1):
      print(range(len(self.events[day]) - 1), len(self.events[day]) - 1)
      # Sees if the event that's wanted to be added fits into the hours of the events
      if self.events[day][i][2] <= startH and endH <= self.events[day][i + 1][1]:
        print('b')
        self.events[day].insert(i + 1, [name, startH, endH])
        return True
    return False
  
  # Removes the specified event, returning a bool based on whether something was deleted or not. Use startH if you want to delete a specific item
  def removeEvent(self, day: int, name: str, startH: int = 0) -> bool:
    # Sees if the selected day has any events, exits if that is the case (for optimization)
    if not(self.events[day]):
      return False
    
    # Loops for every event in the selected day
    for i in self.events[day]:
      # Sees if the wanted item to be deleted is the same as the current item, and deletes the item if it is. If startH is set, it also checks if the start hour is the same (to prevent earlier events to be deleted)
      if i[0] == name and i[1] >= startH:
        self.events[day].remove(i)
        return True
    return False

# Takes information from data.py to be used and updated
user = Schedule(data.name, data.events)
'''while user.removeEvent(1, 'SLEEP') == True:
  pass'''
print(user.addEvent(6, 'testing', 9, 12))
user.toString()
print(user.display)

'''Page related variables/functions directly accessed by menu'''
# Variable for dividing different pages
divider = '━' + '◦○◦━'*15

def scheduleView():
  # Initialized when the program is first ran. Uses info from data.py to decide this. (DOESN'T EXIST YET)
  def survey():
    pass

  if not user.firstTime:
    user.toString()
    print(user.name + '\'s schedule:\n\n' +
          user.display + '\n'
          )
  else:
    survey()
  
  input()

def scheduleChange():
  print()

# Dict of all the accessible subpages
pages = {'viewschedule': scheduleView,
         'changeschedule': scheduleChange}

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
  input = input().lower().replace(' ', '')
  if input == 'exit':
    print('\n' + divider)
    break
    
  elif input == "about":
    import credits
    credits.credits();

  elif not(input in pages):
    print('\nIt seems that what you inputted isn\'t in the menu list.')
  # Runs the user's wanted function when all above checks pass
  else:
    print('\n' + divider)
    pages[input]()

print("Have a nice day!")
try:
  #w = open("data.py","w")
  w.close()
  a.close()
except:
  pass
quit()
