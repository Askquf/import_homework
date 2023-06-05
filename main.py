import application.db.people
import application.salary
import datetime
import pandas

if __name__ == '__main__':
    application.salary.calculate_salary()
    application.db.people.get_employees()
    print(datetime.date.today())
