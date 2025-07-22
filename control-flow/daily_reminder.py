task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

base_reminder = ""

match priority:
    case "high":
        base_reminder = f"'{task}' is a high priority task"
    case "medium":
        base_reminder = f"'{task}' is a medium priority task"
    case "low":
        base_reminder = f"'{task}' is a low priority task"
    case _:
        base_reminder = f"'{task}' has an unrecognized priority. Please set it correctly."

final_reminder = base_reminder

if time_bound == "yes":
    final_reminder += " that requires immediate attention today!"
elif time_bound == "no":
    final_reminder += " that is not time-bound. Consider completing it when you have free time."
else:
    final_reminder += " (Time-bound status unclear.)"

print("Reminder:",final_reminder)