def calculate_salary(work, rate):
    ot_time = work - 40
    if ot_time > 0:
        salary = 40 * rate
        salary += ot_time * rate * 1.5
        return salary
    return work * rate


work_hour = float(input("How many hours did you work last week?"))
rate_per_hour = float(input("What is your pay rate per hour(between 10-25)"))
print(calculate_salary(work_hour, rate_per_hour))
