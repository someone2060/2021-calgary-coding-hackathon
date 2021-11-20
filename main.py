import time
import data, credits

# How long the progam will wait to make the progam seem cleaner
delayTime = 0.2
# Document append variable
dataA = open('data.py', 'a')

'''Class that creates + manages schedules for a user'''
class Schedule:
  def __init__(self, n: str, e: list):
    self.name = n
    self.events = e
    # Sees if there is anything in the user's events. If there is nothing, firstTime is toggled, and survey() is ran.
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
      
      # Increments current[day] up by one if the final hour of the event is passed, only if there is something inside the current day
      for j in range(7):
        if len(self.events[j]) != 0:
          if i == self.events[j][current[j]][2]:
            current[j] += 1

  # Tries to find an event in a day with the name given. Is case sensitive. Returns all instances of the event when it works; returns False otherwise.
  def findEvent(self, day: int, name: str):
    instances = []
    # Loops for every day in the selected day
    for i in self.events[day]:
      # Finds if the selected event is the same as the input
      if i[0] == name:
        instances.append([day] + i[1:])
    # Runs when instances has no length (ie found nothing)
    if not len(instances):
      return [False]
    return [True, instances]

  # Adds an event to self.events, and puts it in the correct place. Returns a bool reporting if the action was successful or not. 
  def addEvent(self, day: int, name: str, startH: int, endH: int) -> bool:
    # startH must be less than endH for the function to work
    if startH >= endH:
      return False
    
    # Adds the event if there is nothing inside the day yet.
    if len(self.events[day]) == 0:
      self.events[day].append([name, startH, endH])
      return True
    # if endH is less than the first event, then the event wanted to be added will be in the right place and will be slotted in.
    elif endH <= self.events[day][0][1] or len(self.events[day]) == 0:
      self.events[day].insert(0, [name, startH, endH])
      return True
    # Loops for each item-1, checks if the event can be slotted in the middle
    for i in range(len(self.events[day]) - 1):
      # Sees if the event that's wanted to be added fits into the hours of the events
      if self.events[day][i][2] <= startH and endH <= self.events[day][i + 1][1]:
        print('b')
        self.events[day].insert(i + 1, [name, startH, endH])
        return True
    # Checks if the event can be added to the end of the selected day
    if self.events[day][-1][2] <= startH:
      self.events[day].append([name, startH, endH])
      return True
    return False
  
  # Removes one instance of the specified event from self.events, returning a bool based on whether something was deleted or not. startH makes the function start from the hour, essentially making the function 
  def removeEvent(self, day: int, name: str, startH: int = 0) -> bool:
    # Sees if the selected day has any events, exits if that is the case (for optimization)
    if len(self.events[day]) == 0:
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

'''Page related variables/functions directly accessed by main loop'''
divider = '━' + '◦○◦━'*15
noFind = 'Invalid entry!'

# 'Add event' menu (outside because it is used by scheduleView() and scheduleChange())
def add():
  weekStr = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  
  # Gets the user to input the days that they want an event, and checks if it is a valid input
  def promptDay():
    global inpDay
    while True:
      inpDay = list(input('\nWhat day(s) do you want this event held? Type integers from 0-6, with each number pertaining to a day in a week (Sunday is 0, Monday is 1, Tuesday is 2…). If you want the event to be on more than one day, then type one of each of the numbers.\n').strip())
      
      # Checks to see if the input is valid, converting it into usable data in the process
      # Variable to see if inpDay can be used
      valid = True
      try:
        # Stores the true/false statement for each day in a week. (eg. if there's an event on sunday, holder[0] = True) Will replace inpDay at the end of the loop.
        holder = [0]*7
        # Loops for each item in inpDay
        for i in range(len(inpDay)):
          inpDay[i] = int(inpDay[i])
          if inpDay[i] in (7, 8, 9):
            valid = False
            break
          holder[inpDay[i]] = 1
      except:
        print('\n' + noFind)
        continue
      
      if not valid or sum(holder) == 0:
        print('\n' + noFind)
        continue
      else:
        inpDay = holder
        break
  
  # Gets the user to input the hours that they want an event, and checks if it can be used
  def promptHour():
    global inpHour
    while True:
      inpHour = input('\nWhat times would you like the event to be held from? Use \"-\" to divide the starting and ending time, and use 24 hour time. (Example: type \"11-15\" if you want to schedule your event to be from 11AM to 3PM.)\n').split('-')
      # If at any time this breaks, it's because the inputs can't be converted to integers, and it makes the entry invalid.
      try:
        for i in range(len(inpHour)):
          inpHour[i] = inpHour[i].strip()
          inpHour[i] = int(inpHour[i])
      except:
        print('\n' + noFind)
        continue

      # Sees if inpHour is able to be used in addEvent() from Schedule class
      if len(inpHour) == 2 and inpHour[0] < inpHour[1] and 0 <= inpHour[0] <= 24 and 0 <= inpHour[1] <= 24:
        break
      else:
        print('\n' + noFind)
  
  inpName = input('\nWhat is the name of the event that you would like to add?\n')

  promptDay()
  
  promptHour()
  
  inpDayStr = ''
  # Turns inpDay into a readable string
  for i in range(len(inpDay)):
    if inpDay[i]:
      inpDayStr += weekStr[i] + ', '
  # Removes the ', ' at the end
  inpDayStr = inpDayStr[:-2]

  # Second subpage
  while True:
    print('\nCURRENT SETTINGS\n' +
        'Event name: ' + inpName + '\n' +
        'Event day(s): ' + inpDayStr + '\n' +
        'Event time: ' + str(inpHour[0]) + ':00 – ' + str(inpHour[1]) + ':00\n' +
        '\n' +
        '''Options:
  1. Change event name
  2. Change event day
  3. Change event time
  4. Confirm changes
  5. Cancel and exit
    
Input the number of what you want to access.''')
    inp = input()
    
    # Prevents an error from happening
    try:
      if 1 <= int(inp) <= 5: 
        inp = int(inp)
        # Changing event name
        if inp == 1:
          inpName = input('What would you like to change the name of the event to?\n')

        # Changing event days
        elif inp == 2:
          promptDay()

        # Changing event time
        elif inp == 3:
          promptHour()
        
        # Save changes option
        elif inp == 4:
          break

        # Cancel option
        else: 
          return
      else:
        print('\n' + noFind)
        continue
    except:
      print('\n' + noFind)
      continue

  # Tells the program if something went wrong with adding an event
  problem = False
  # Loops for each day in a week
  for i in range(7):
    if inpDay[i]:
      if not user.addEvent(i, inpName, inpHour[0], inpHour[1]):
        problem = True
  # Writes user.events to data.py, so that the data is saved for long-term use
  dataA.write('\nevents = ' + str(user.events))

  if problem:
    print('Some or all of your changes were unable to be added. This is due to a scheduling conflict. Please view your schedule, and see which items weren\'t able to be added.\n\nEnter anything to exit.')
  else:
    user.toString()
    print(user.display + '\nYour changes have been saved! Here is your new schedule:\n\nEnter anything to exit.')

  input()

# Page that views the schedule
def scheduleView():
  # Initialized when the program is first ran. Uses info from data.py to decide this. (DOESN'T EXIST YET, TODO)
  def survey():
    user.firstTime = False
    
    user.name = input('What is your name?\n')
    dataA.write('\nname = \'' + str(user.name)+ '\'')
    
    # Used to see if add() has been ran yet
    prompted = False
    while True:
      if not prompted:
        add()
      prompted = True
      inp = input('\nWould you like to add another event? (Yes/No)\n')
      if inp in ('yes', 'y'):
        prompted = False
        continue
      elif inp in ('no', 'n'):
        break
      else:
        print('\n' + noFind)

  if user.firstTime:
    while True:
      print('It seems that you don\'t have a schedule yet. Would you like to use our tool to quickly create one? (Yes/No)\n')
      inp = input().lower()
      if inp in ('yes', 'y'):
        survey()
        break
      elif inp in ('no', 'n'):
        user.toString()
        input('A blank schedule:\n\n' +
          user.display + '\n'
          'If the table appears weird, make your window wider.\n' +
          'Enter anything to exit!\n')
        break
      else:
        print('\n' + noFind)
  else:
    user.toString()
    input(user.name + '\'s schedule:\n\n' +
          user.display + '\n'
          'If the table appears weird, make your window wider.\n' +
          'Enter anything to exit!\n')

# Allows the user to change their schedule. Uses the Schedule class to do this.
def scheduleChange():
  # 'Remove event' menu
  def remove():
    # Prompts the user for the day that's wanted to be searched
    def promptDay():
      global inpDay, useInt
      while True:
        inpDay = input('\nWhich day\'s events do you want to remove? Type \"all\" if you want to delete all events with the name ' + inpName + '. If you want to delete specific days from ' + inpName + ', type integers from 0-6, with each number pertaining to a day in a week (Sunday is 0, Monday is 1, Tuesday is 2…). If you want the event to be on more than one day, then type one of each of the numbers.\n').strip().lower()

        if inpDay == 'all':
          useInt = False
          break
        else:
          '''Copied from add() function'''
          # Checks to see if the input is valid, converting it into usable data in the process
          # Variable to see if inpDay can be used
          valid = True
          try:
            # Converts the string into int, so that it will be easily used in the copied code
            inpDay = list(inpDay)
            # Stores the true/false statement for each day in a week. (eg. if there's an event on sunday, holder[0] = True) Will replace inpDay at the end of the loop.
            holder = [0]*7
            # Loops for each item in inpDay
            for i in range(len(inpDay)):
              inpDay[i] = int(inpDay[i])
              if inpDay[i] in (7, 8, 9):
                valid = False
                break
              holder[inpDay[i]] = 1
          except:
            print('\n' + noFind)
            continue
          
          if not valid or sum(holder) == 0:
            print('\n' + noFind)
            continue
          else:
            inpDay = holder
            useInt = True
            break
          '''end of copy'''

    inpName = input('\nWhat\'s the name of the event that you want to remove? Input is case sensitive.\n')
    
    promptDay()

    # Variable that stores all instances of events named inpName
    instances = []
    # Loops for each day in a week
    for i in range(7):

      # Checks whether or not specific dates have been requested from the user, and if there is anything inside the date
      if ((not useInt) or (useInt and inpDay[i])) and user.findEvent(i, inpName)[0]:
        # Saves the events found in that day, then adds it to instances so that the list is 2D instead of 3D
        raw = user.findEvent(i, inpName)[1]
        for j in raw:
          instances.append(j)

    # Runs if no events were found
    if len(instances) == 0:
      input('Nothing was found. Try doublechecking the cases of your text, and enter this menu again.\nEnter anything to continue.\n')
    else:
      while True:
        inp = input('\nThe events that you have stated have been found. Would you like to confirm your changes? (Type yes/no)\n').strip().lower()
        
        # Deletes all events stated
        if inp in ('yes', 'y'):
          for i in instances:
            user.removeEvent(i[0], inpName, i[1])
          dataA.write('\nevents = ' + str(user.events))
          
          user.toString()
          print(user.display)
          input('Your changes has been saved, and your new schedule is above.\nEnter anything to continue.')
          break
        # Returns to the menu
        elif inp in ('no', 'n'):
          input('Your request has been cancelled.\nEnter anything to continue.')
          break
  
  # Adds a way to change the user's name
  def nameChange():
    user.name = input('\nWhat is your new name?\n')
    dataA.write('\nname = \'' + user.name + '\'')

  subpages = {('add', 'a', '1'): add,
              ('remove', 'r', '2'): remove,
              ('changename', 'name', 'n', '3'): nameChange}

  while True:
    inp = input(divider + '''\nHow would you like to change your schedule?
  1. Add an event (add)
  2. Remove an event (remove)
  3. Change your name (changeName, name)
  4. Exit this page (exit)
    
Use the numbers next to the line, or the text in parentheses to access each item.\n''')

    # Variable used to see if there is one that is referenced in pages dict
    contains = False
    if inp in ('exit', 'e', '4'):
      break
    for i in subpages:
      if inp in i:
        contains = True
        inp = i
        break
    if contains:
      subpages[i]()
    else:
      print('\n' + noFind)

def about():
  credits.credits();

# Dict of all the accessible subpages
pages = {('viewschedule', 'view', 'v'): scheduleView,
         ('changeschedule', 'change', 'c'): scheduleChange,
         ('about', 'a'): about}

'''MAIN LOOP'''
while True:
  time.sleep(delayTime)

  print(divider)
  print('''Welcome to our schedule tool!
Access pages by typing the text of what you want to see. (eg. type "About" if you want to see the about page)

Menu: You are here!
View Schedule: View your schedule
Change Schedule: Add or remove events from your schedule.
About: See the point of this program, and the credits.
Exit: Exit the program, and save your schedule.\n''')
  # Changes the user's input so that keywords are less strict
  inp = input().lower().replace(' ', '')
  # Variable used to see if there is one that is referenced in pages dict
  contains = False

  if inp in ('exit', 'e'):
    print('\n' + divider)
    break

  else:
    for i in pages:
      if inp in i:
        # Signals that the input contains something that the 
        contains = True
        inp = i
        break
    
    if contains:
      print('\n' + divider)
      pages[inp]()
    else:
      print('\n' + noFind)

'''Makes data.py look nicer, then closes files and exits the program'''
try:
  dataA.close()

  dataW = open("data.py","w")
  dataW.write('name = \'' + str(user.name) + '\'')
  dataW.write('\nevents = ' + str(user.events))
  dataW.close()
except:
  pass
print("Have a nice day!")
quit()
