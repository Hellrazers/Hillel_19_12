from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from contract.db_orm import Base

class Department_Orm(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Встановлення відношення "один до багатьох" з таблицею Employee
    employees = relationship("Employee_Orm", back_populates="department")
