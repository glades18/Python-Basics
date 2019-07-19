from datetime import datetime, date
    
    
def current_date_time():
        return datetime.now()

print(current_date_time())


def current_time():
        return datetime.now().time()

print(current_time())


def current_date():
        todays_date = str(date.today())

        return todays_date

print(current_date())


def current_year():
        todays_year = datetime.now().year

        return todays_year

print(current_year())


def current_day():
        todays_day = datetime.now().day

        return todays_day

print(current_day())


def current_month():
        todays_month = datetime.now().month

        return todays_month

print(current_month())


def week_day():
        todays_weekday = datetime.now()
        weekDay = todays_weekday.strftime('%A')

        return weekDay

print(week_day())


def am_pm():
        time = datetime.now()
        final_time = time.strftime('%p')

        return final_time

print(am_pm())


def check_day(day):
        todays_date = datetime.now().strftime('%D')

        if day == todays_date:
            return True
        else:
            return False

print(check_day(day)) 


def check_year(year):
        todays_year = datetime.now().strftime('%Y')

        if todays_year ==  year:
            return True
        else:
            return False

print(check_year(year))






            
            