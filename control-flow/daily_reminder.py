task = input('Enter your task:')
priorty = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priorty:
  case "high":
    if(time_bound == 'yes'):  
      print(f"Finish '{task}' is a {priorty} priorty task that requires immediate attention today!")
    else:
      print(f"Note: '{task}' is a {priorty} priorty task. Consider completing it when you have free time.")
  case "medium":
    if(time_bound == 'yes'):  
      print(f"Finish '{task}' is a {priorty} priorty task that requires immediate attention today!")
    else:
      print(f"Note: '{task}' is a {priorty} priorty task. Consider completing it when you have free time.")
  case "low":
    if(time_bound == 'yes'):  
      print(f"Finish '{task}' is a {priorty} priorty task that requires immediate attention today!")
    else:
      print(f"Note: '{task}' is a {priorty} priorty task. Consider completing it when you have free time.")