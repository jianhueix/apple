from datetime import date

def days_between_dates(date1, date2):
    return (date2 - date1).days

print(days_between_dates(date(2019, 1, 1), date(2019, 1, 21)))
print(days_between_dates(date(2019, 1, 21), date(2019, 1, 1)))


# Output: 1
