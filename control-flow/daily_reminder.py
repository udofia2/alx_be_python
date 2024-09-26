task = input('Enter your task:')
priorty = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
if(time_bound == 'yes'): 
  
  print(task)
  print(priorty)
  print(time_bound)
  match priorty:
    case "high":
      print(f"Finish '{task}' is a {priorty} priorty task that requires immediate attention today!")
    case "medium":
      print(f"Finish '{task}' is a {priorty} priorty task that requires immediate attention today!")
    case "low":
      print(f"Finish '{task}' is a {priorty} priorty task that requires immediate attention today!")
else: 
  match priorty:
    case "high":
      print(f"Note: '{task}' is a {priorty} priorty task. Consider completing it when you have free time.")
    case "medium":
      print(f"Note: '{task}' is a {priorty} priorty task. Consider completing it when you have free time.")
      
    case "low":
      print(f"Note: '{task}' is a {priorty} priorty task. Consider completing it when you have free time.")
    
    # case _:
    #   print(f"Note: '{task}' is a {priorty} priorty task. Consider completing it when you have free time.")
# Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
# Note: 'Read a book' is a low priority task. Consider completing it when you have free time.