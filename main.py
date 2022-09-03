from application.salary import calculate_salary as calculate
from application.db.people import get_employees as employees
from datetime import datetime

if __name__ == '__main__':
    calculate()
    employees()
    print(datetime.today())
    