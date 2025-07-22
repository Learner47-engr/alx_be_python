task_description = input("Enter the task description: ")
task_priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound (yes or no)? ").lower()

reminder = ""

match task_priority:
    case "high":
        reminder = f"Reminder: '{task_description}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task_description}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task_description}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task_description}' has an unrecognized priority. Please set it correctly."
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += " that is not time-bound. Consider completing it when you have free time."
else:
    reminder += " (Time-bound status unclear.)"

print("\n" + reminder)