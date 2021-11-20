

#Dictionary
o0 = ""
o1 = ""
o2 = ""
o3 = ""
o4 = ""
o5 = ""
o6 = ""
o7 = ""
o8 = ""
o9 = ""
o10 = ""
o11 = ""
o12 = ""
o13 = ""
o14 = ""
o15 = ""
o16 = ""
o17 = ""
o18 = ""
o19 = ""
o20 = ""
o21 = ""
o22 = ""
o23 = ""
hour = {0:o0,1:o1,2:o2,3:o3,4:o4,5:o5,6:o6,7:o7,8:o8,9:o9,10:o10,11:o11,12:o12,13:o13,14:o14,15:o15,16:o16,17:o17,18:o18,19:o19,20:o20,21:o21,22:o22,23:o23}





#User's schedule
#Work schedule cannot be changed (school or job)
def job():
  print("Tell me the schedule of your job or school.")
  jobstart = int(input("When does it start? Please enter only number: "))
  jobend = int(input("When does it end? Please enter only number: "))
  #jobperiod for i in range(jobstart, jobend)
  return jobstart, jobend

#Other appointments
def appointment():
    appointment_name =str(input("Enter the name of the plan: "))
    appointment_starttime =int(input("When does it start? Please enter only number: "))
    appointment_endtime = int(input("When does it end? Please enter only number: "))
    return appointment_name, appointment_starttime,appointment_endtime

#Lifestyle
#Meal
#Taking a bath
def mealANDbath():
  breakfast=int(input("What time do you have breakfast?: "))
  lunch=int(input("What time do you have lunch?: "))
  dinner=int(input("What time do you have dinner?: "))
 
  bath=int(input("When do you take a shawer?: "))

  return breakfast,lunch,dinner,bath

#Sleep
def sleep():
  badsleep =True
  while badsleep:
    sleep_end =int(input("When do you wake up?: "))
    sleep_start=int(input("When do you go to bed? "))
    if(12<=sleep_start<=23):
      if((24-sleep_start+sleep_end)<5):
        print("Get longer sleep! It's good to get asleep for 6-8 hours.")
      elif((24-sleep_start+sleep_end)>9):
        print("Get shorter sleep! It's good to get asleep for 6-8 hours.")
      else:
        badsleep=False
        sleep_period=24-sleep_start+sleep_end
    elif(0<=sleep_start<=11):
      if((sleep_start+sleep_end)<5):
        print("Get longer sleep! It's good to get asleep for 6-8 hours.")
      elif((sleep_start+sleep_end)>9):
        print("Get shorter sleep! It's good to get asleep for 6-8 hours.")
      else:
        badsleep=False
        sleep_period=sleep_start+sleep_end
    else:
      badsleep=False
  return sleep_start, sleep_end,sleep_period

#Other thing what the user wants to achieve

def task():
  task_name= str(input("Enter the name of the task: "))
  task_starttime=int(input("what time will you start the task?: "))
  task_endtime=int(input("what time will you finish the task?: "))

  return task_name,task_starttime,task_endtime

#User’s favorite entertainment (including the case they don’t have any hobbies)
#How long it takes to enjoy it at least once (users can choose two or more from alternatives))
def entertainment ():
  play_name = str(input("What is your hobby?: "))
  #print(" ")
  #print("How long does it take about? ")
  #print("1) 15 minutes")
  #print("2) 45 minutes")
  #print("3) 60 minutes")
  #print("4) 2 hours")
  #print("5) Whatever")
  #play_period = int(input("Select number from the above: "))
  print(" ")
  print("When do you want to put such entertainment time?: ")
  print(" ")
  print("On Weekdays:")
  print("1) Early morning")
  print("2) Between job/school and dinner")
  print("3) Between dinner and sleep")
  print("4) Whenever")
  play_time_weekday = int(input("Select number from the above: "))
  #print(" ")
  #print("On Weekends:")
  #print("1) Morning")
  #print("2) Around noon")
  #print("3) Afternoon until dinner")
  #print("4) After dinner")
  #print("5) Whenever")
  #play_time_weekend = int(input("Select number from the above: "))
  return play_name,play_time_weekday#,play_time_weekend, play_period



#Input
space=" "
remaingtime_counter=0

print ("Please tell me your daily schedule per hour.")
print(space)
jobstart, jobend = job()
for i in range(jobstart,jobend):
  remaingtime_counter+=1
print(space)

exist = str(input("Do you have any must plan other than job/school(y/n)?: "))
mustplan_name=[]
mustplan_starttime=[]
mustplan_endtime=[]
while exist == "y":
  appointment_name, appointment_starttime,appointment_endtime = appointment()
  if(appointment_starttime == appointment_endtime):
    remaingtime_counter += 1
  elif(appointment_starttime>appointment_endtime):
    for i in range(24-appointment_starttime+appointment_endtime):
      remaingtime_counter+=1
  else:
    for i in range(appointment_starttime,appointment_endtime):
      remaingtime_counter+=1

  mustplan_name.append(appointment_name)
  mustplan_starttime.append(appointment_starttime)
  mustplan_endtime.append(appointment_endtime)
  exist = str(input("Do you have any must plan other than job/school(y/n)?: "))

print(space)
print("Tell me your lifestyle.")
print(space)
breakfast,lunch,dinner,bath =mealANDbath()
remaingtime_counter+=1
print(space)
sleep_start, sleep_end,sleep_period = sleep()
for i in range(sleep_period):
  remaingtime_counter+=1
print(space)

exist = str(input("Do you have any task to do(y/n)?: "))
tryagain = "y"
task_name=""
addfun="n"

minicounter = 0
task_name=[]
task_starttime=[]
task_endtime=[]
while(exist== "y"):
  while(tryagain =="y"):
    task_name1,task_starttime1,task_endtime1 = task()
    if(task_starttime1 == task_endtime1):
      minicounter += 1
    elif(task_starttime1>task_endtime1):
      for i in range(24-task_starttime1+task_endtime1):
        minicounter +=1
    else:
      for i in range(task_starttime1,task_endtime1):
        minicounter+=1
    task_name.append(task_name1)
    task_starttime.append(task_starttime1)
    task_endtime.append(task_endtime1)
    tryagain="n"
    if(remaingtime_counter +minicounter>24):
      print("There is no time to work on all those tasks!")
      print("Please reduce the tasks and resist again.")
      tryagain = str(input("Do you have any task to do(y/n)?: "))
      minicounter = 0
      task_name=[]
      task_starttime=[]
      task_endtime=[]
    elif(remaingtime_counter +minicounter == 24):
      print("You work too much.")
      addfun= str(input("Let's have a fun time in the last 15 minutes of task time (y/n)!: "))
    else:
      tryagain = str(input("Do you have any task to do(y/n)?: "))
      exist ="n"



play_name,play_time_weekday = entertainment()

#play_time_weekend,play_period

#Process

item = {"plan0":"n","plan1":"JOB/SCHOOL","plan2":mustplan_name,"plan3":"MEAL","plan4":"BATH","plan5":"SLEEP","plan6":task_name,"plan7":play_name}


#Put lifestyle or plans that cannot be changed on the schedule first.
for i in range(jobstart, jobend):
  hour[i]+= " "+item["plan1"]

if(sleep_start>sleep_end):
  if(sleep_start ==23):
    hour[23]+=" "+item["plan5"]
  else:
    for i in range(sleep_start,24):
      hour[i]+= " "+item["plan5"]
  if(sleep_end==0):
    hour[0]+=" "+item["plan5"]
  else:
    for i in range(0,sleep_end):
      hour[i]+= " "+item["plan5"]
else: 
  for i in range(sleep_start, sleep_end):
    hour[i]+= " "+item["plan5"]

for i,j,k in zip(mustplan_starttime,mustplan_endtime,mustplan_name):
  item["plan2"]= k
  if(i == j):
    hour[i]+= " "+item["plan2"]
  elif(i>j):
    if(i ==23):
      hour[23]+=" "+item["plan2"]
    else:
      for l in range(i,24):
        hour[l]+= " "+item["plan2"]
    if(j==0):
      hour[0]+=" "+item["plan2"]
    else:
      for l in range(0,j):
        hour[l]+= " "+item["plan2"]
  else:
    for l in range(i,j):
      hour[l] += " "+item["plan2"]
    
#invalid literal for int( with base 10)


hour[breakfast] += " "+item["plan3"]
hour[lunch] += " "+item["plan3"]
hour[dinner] += " "+item["plan3"]
hour[bath] += " "+item["plan4"]

#'builtin_function_ormethod' object is not subscriptable

#Put other tasks on the schedule second.
    #45/15 minutes each to work(other than school or job)/rest
    #If there is anything to do, ask how many hours that job will take, and then repeat the 45-minute work 15-minute break.
   


for i,j,k in zip(task_starttime,task_endtime,task_name):
    item["plan6"]= k
    if(i == j):
      hour[i] += " "+item["plan6"]+" REST(15min.)"
    elif(i>j):
      if(i ==23):
        hour[23]+=" "+item["plan6"]+" REST(15min.)"
      else:
        for l in range(i,24):
          hour[l]+= " "+item["plan6"]+" REST(15min.)"
        for l in range(0,j):
          hour[l]+= " "+item["plan6"]+" REST(15min.)"
    else:
      for l in range(i,j):
        hour[l] += " "+item["plan6"]+" REST(15min.)"

#Put entertainment plans on the schedule third on the time when users want to do or the remaining time until sleep.
     

if(play_time_weekday == 1):
  if(sleep_end>jobstart):
    if(sleep_end == 23):
      if hour[23] == "":
        hour[23]+=" "+item["plan7"]
    else:
      for i in range(sleep_end,24):
        if hour[i] == "":
          hour[i]+=" "+item["plan7"]
    if(jobstart == 0):
      if hour[0] == "":
        hour[0]+=" "+item["plan7"]
    else:
      for l in range(0,jobstart):
        if hour[0] == "":
          hour[i]+= " "+item["plan7"]
  else:
    for i in range(sleep_end,jobstart):
      if hour[i] == "":
          hour[i]+=" "+item["plan7"]
elif(play_time_weekday == 2):
  if(jobend>dinner):
    if(jobend == 23):
      if hour[23]== "":
        hour[23]+=" "+item["plan7"]
    else:
      for i in range(jobend,24):
        if hour[i] == "":
          hour[i]+=" "+item["plan7"]
    if(dinner == 0):
      if hour[0] == "":
        hour[0]+=" "+item["plan7"]
    else:
      for l in range(0,dinner):
        if hour[0] == "":
          hour[i]+= " "+item["plan7"]
  else:
    for i in range(jobend,dinner):
      if hour[i] == "":
          hour[i]+=" "+item["plan7"]

elif(play_time_weekday == 3):
  if(dinner+1>sleep_start):
    if(dinner+1 == 23):
      if hour[23] == "":
        hour[23]+=" "+item["plan7"]
    else:
      for i in range(dinner+1,24):
        if hour[i] == "":
          hour[i]+=" "+item["plan7"]
    if(sleep_start == 0):
      if hour[0]== "":
        hour[0]+=" "+item["plan7"]
    else:
      for l in range(0,sleep_start):
        if hour[0] == "":
          hour[i]+= " "+item["plan7"]
  else:
    for i in range(dinner+1,sleep_start):
      if hour[i] == "":
          hour[i]+=" "+item["plan7"]
else:
  for i,j in zip(hour.values(),hour.keys()):
    if i == "":
      hour[j]+=" "+item["plan7"]

#If the time to work on other tasks is equal or longer than the remaining time until sleep, suggest to set time for at least fifteen minutes for entertainment
if(addfun == "y"):
  a = task_endtime[len(task_endtime)-1]
  if(a == 0):
    a=23
  else:
    a -=1
  hour[a]+=" "+item["plan7"]+"(15min.)"


#Output
print(" ")
print("    Today's schedule")
print("--------------------------")
print(" 0:00 | ",hour[0])
print(" 1:00 | ",hour[1])
print(" 2:00 | ",hour[2])
print(" 3:00 | ",hour[3])
print(" 4:00 | ",hour[4])
print(" 5:00 | ",hour[5])
print(" 6:00 | ",hour[6])
print(" 7:00 | ",hour[7])
print(" 8:00 | ",hour[8])
print(" 9:00 | ",hour[9])
print("10:00 | ",hour[10])
print("11:00 | ",hour[11])
print("12:00 | ",hour[12])
print("13:00 | ",hour[13])
print("14:00 | ",hour[14])
print("15:00 | ",hour[15])
print("16:00 | ",hour[16])
print("17:00 | ",hour[17])
print("18:00 | ",hour[18])
print("19:00 | ",hour[19])
print("20:00 | ",hour[20])
print("21:00 | ",hour[21])
print("22:00 | ",hour[22])
print("23:00 | ",hour[23])

