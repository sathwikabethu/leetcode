class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        total_days=0
        months=[31,28,31,30,31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(1900,year):
            if (i%400==0)or(i%4==0 and i%100!=0):
                total_days+=366
            else:
                total_days+=365
        if (year%400==0)or(year%4==0 and year%100!=0):
            months[1]=29
        for i in range(month-1):
            total_days+=months[i]
        total_days+=day-1
        req_day=total_days%7
        days=[ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
        return days[req_day]



        