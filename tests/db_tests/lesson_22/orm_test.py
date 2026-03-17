import os
import random

from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, func, select, desc
from sqlalchemy.orm import sessionmaker

from constant import BASE_DIR
from contract.db_orm import Base
from contract.db_orm.department_orm import Department_Orm
from contract.db_orm.employee_orm import Employee_Orm
from contract.db_orm.user_orm import User_Orm
from faker import Faker


f = Faker()
load_dotenv()

dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
DB_TYPE = os.getenv("DB_TYPE", 'postgresql')
# З'єднання з базою даних PostgreSQL (замініть дані на ваші)

if DB_TYPE == 'postgresql':
    DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
else:
    DATABASE_URL = f'sqlite:///{BASE_DIR}/sql_lite/my_db.db'
print(DATABASE_URL, 'path to db')
# engine = create_engine(DATABASE_URL)
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

# Створення сесії для взаємодії з базою даних
Session = sessionmaker(bind=engine)
session = Session()
add_user = User_Orm(name='John', age=30)
# Додавання користувачів до бази даних
session.add(add_user)
session.commit()
print(add_user)
add_user.name =  'Alex'
session.commit()
print(add_user)
bulk_users = [User_Orm(name=f.first_name(), age= random.choice(range(18, 60))) for k in range(5)]
# SQL аналог:
# INSERT INTO users (name, age) VALUES ('John', 30), ('Alice', 25), ('Bob', 35);
session.add_all(bulk_users)
session.commit()
print(bulk_users)

last_user_in_bulk = bulk_users[-1]
last_user_in_bulk.age = 60
bulk_users_2 = list(bulk_users)

for index, _value in enumerate(range(4)):
    print(bulk_users[index])
    session.delete(bulk_users[index])
    bulk_users_2.pop(0)

print(bulk_users[4:], "our slice ")
print(f'len of obj {len(bulk_users_2)}')
print(bulk_users_2)
session.commit()
our_select = select(User_Orm).where(User_Orm.age == 30, User_Orm.name == 'John')
user_after_secect = session.execute(our_select).all()
print(user_after_secect)
# user_after_secect[0][0].name = 'Alex'

session.commit()

# Використання виразів для складного запиту: обчислення середнього віку користувачів
average_age = session.query(func.avg(User_Orm.age)).scalar()
print("Середній вік користувачів:", average_age)
# SQL аналог: SELECT AVG(age) FROM users;

# Використання виразів для складного запиту: підрахунок кількості користувачів
user_count = session.query(func.count(User_Orm.id)).scalar()
print("Кількість користувачів:", user_count)
# SQL аналог: SELECT COUNT(id) FROM users;




# # Додавання департаментів та співробітників до бази даних
# it_department = Department_Orm(name='IT')
# hr_department = Department_Orm(name='HR')


all_users_by_id_qury = select(Department_Orm).where(Department_Orm.id == 1)
all_users_by_id_execute = session.execute(all_users_by_id_qury).first()

session.delete(all_users_by_id_execute[0])
session.commit()


# john = Employee_Orm(name='John', department=it_department)
# alice = Employee_Orm(name='Alice', department=hr_department)
# bob = Employee_Orm(name='Bob', department=it_department)
#
# session.add_all([it_department, hr_department, john, alice, bob])
# session.commit()
#
# # Вибірка співробітників та їх департаментів
# all_users_by_id_qury = select(Employee_Orm).where( Department_Orm.name=='IT')
# all_users_by_id_execute = session.execute(all_users_by_id_qury).all()
# print(all_users_by_id_execute)
# count = 0
# for user_ in all_users_by_id_execute:
#     value = user_[0]
#     if value.department.name == 'IT':
#         count += 1
#
# print(f"My count is {count} and len of list {len(all_users_by_id_execute)}")
# # print(len(session.execute(select(Employee_Orm).where(Employee_Orm.department_id=1))))
# employees = session.query(Employee_Orm).limit(5)
# for employee in employees:
#     # if employee.department_id == 5:
#         print(f"Ім'я: {employee.name}, Департамент: {employee.department.name} DEP_ID : {employee.department_id} / {employee.department.id}")



# Закриття сесії
session.close()