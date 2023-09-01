# %%
from pathlib import Path
import csv
csv_file_path= ("../Users/terrencetrimuel/Desktop/Python-homework/Python_Act1/Homework Instructions/PyBank/Resources/budget_data.csv")


# %%
from pathlib import Path
import csv
csv_file_path= Path("/Users/terrencetrimuel/Desktop/Python-homework/Instructions from class/PyBank/Resources/budget_data.csv")
#Defining Variables
total_months = 0
total_profit = 0
previous_profit = None
change_sum = 0
greatest_increase = ["", 0] 
greatest_decrease = ["", 0]


with open(csv_file_path,'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        date = row[0]
        profit = int(row[1])
        total_months += 1
        total_profit += profit
        
        if previous_profit is not None:
            change = profit - previous_profit
            change_sum += change

            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            elif change < greatest_decrease[1]:
                greatest_decrease = [date, change]   
    previous_profit = profit
    
    average_change= change_sum / (total_months - 1)               

print("financial analysis")
print("----------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit: ,}")
print(f"Average Change: ${average_change: .2f}")
print(f"Greatest Increase in Profts: {greatest_increase[0]} (${greatest_increase[1]:,})")
print(f"Greatest Decrease in Profit: {greatest_decrease[0]} (${greatest_decrease[1]:,})")

  


# %%
 


