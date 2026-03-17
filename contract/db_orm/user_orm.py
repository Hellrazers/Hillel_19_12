from sqlalchemy import Column, Integer, String

from contract.db_orm import Base


# Створення базового класу для визначення моделей даних


# Визначення моделі даних (таблиці) за допомогою класу
class User_Orm(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    desc = Column(Integer)

    def __str__(self):
        return f'id : {self.id}, name : {self.name}, age : {self.age}'


    def __repr__(self):
        return f'id:{self.id} name:{self.name} age:{self.age}'