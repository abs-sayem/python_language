# total_salary = amount except mobile bill
# leave_over_taken = taken_leaves_this_month - remaining_leave_days; otherwise 0
total_salary = 23500
days_of_running_month = 31
leave_over_taken = 0.5
total_late_days = 2
total_late_hours = 5.29

if total_late_days < 3: total_late_days = 0
per_day_salary = total_salary / days_of_running_month
leave_deduction = leave_over_taken * per_day_salary
late_days_deduction = (total_late_days / 3) * per_day_salary
late_hour_deduction = total_late_hours / (per_day_salary/2)

salary = total_salary - (leave_deduction + late_days_deduction + late_hour_deduction)

print(f"Counted : Leave: {leave_over_taken}D, Late_Days: {total_late_days}D, Late_Hours: {total_late_hours}H, Per_Day_Salary: {per_day_salary:.2f}BDT")
print(f"Received: {salary:.2f} BDT ({total_salary} - ({leave_deduction:.2f} + {late_days_deduction:.2f} + {late_hour_deduction:.2f}))")
print(f"Deducted: {total_salary - salary:.2f} BDT")