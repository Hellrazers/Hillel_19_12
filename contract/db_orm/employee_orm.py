from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from contract.db_orm import Base

class Employee_Orm(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('departments.id'))

    # Встановлення відношення "багато до одного" з таблицею Department
    department = relationship("Department_Orm", back_populates="employees")