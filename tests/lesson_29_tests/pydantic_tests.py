from uuid import uuid4
from typing import List, Self
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict, model_validator, field_validator, ValidationError
from pydantic_core.core_schema import ValidationInfo


# class DeviceModel(BaseModel):
#     name: str              # = Field(pattern=r'/^[Ми]\W+/gm')
#     price: float = Field(ge=1, description='We validaton on price higher than or equals than 1 ', title='We validaton on price higher than or equals than 1 ')
#     quantity: int | None = 1232
#     model_config = ConfigDict(str_strip_whitespace=True, extra='ignore', validate_default=False,)
#
#
# class UserModel(BaseModel):
#     order_id: int
#     customer_name: str  =  Field(alias='customerName' )
#     customer_name_1 : int =  Field(alias='customerName1.customerName1.customerName1')
#     items: List[DeviceModel]
#     order_date: datetime
#
# json = {
#     "order_id": 1024,
#     "customerName1.customerName1.customerName1": 123,
#     "customerName": "Олексій",
#     "items": [
#         {
#             "name": "   Механічна клавіатура     ",
#             "price": 2500.50,
#             "quantity": 123
#         },
#         {
#             "name": "Мишка",
#             "price": 1200.00,
#             "quantity": 2,
#         },
#         {
#             "name": "Мишка",
#             "price": 1200.00,
#             "quantity": 2,
#             'asd': 123,
#         },
#         {
#             "name": "Мишка",
#             "price": 1200.00,
#             "quantity": 2,
#         },
#         {
#             "name": "asd",
#             "price": 1,
#             "quantity": None,
#         }
#
#     ],
#     "order_date": "2023-10-27T14:30:00"
# }
# json_after_validation =  UserModel.model_validate(json)
# print(json_after_validation.customer_name)
# print(json_after_validation.customer_name_1)
# print(json_after_validation.items)
# print(json_after_validation.items[0].name)
# # assert json.get('order_id') is not None
# # for k in json.get('items'):
# #     if not (isinstance(k.get('quantity'), int) and k.get('quantity') > 0):
# #         raise ValueError(f'Wrong with type {k.get('quantity')}')
#
#
# class UserModel(BaseModel):
#     user_id: UUID
#     username: str | int
#
#     @field_validator('username')
#     @classmethod
#     def validate_username(cls, value: str | int):
#         if isinstance(value, str):
#             if value.startswith('iv'):
#                 print(True)
#             print('len of the field is ', len(value))\
#
#         if isinstance(value, int):
#             result = value % 2
#             print(f'{value} % 2 =  {result}')
#
#         return value
#
#
# class dataClass(BaseModel):
#     data: List[UserModel]
#
#     @model_validator(mode='after')
#     def check_uniq_id(self) -> Self:
#         list_ids = [k.user_id for k in self.data]
#         set_ids = set()
#
#         for k in list_ids:
#             if k not in set_ids:
#                 set_ids.add(k)
#             else:
#                 raise ValueError(f'Unique ID already exists, {k}')
#
#         return self
#
#
#
# json_with_UUID = {"data": [{"user_id": "123e4567-e89b-12d3-a456-426614174001", "username": "ivan"},
#                            {"user_id": "123e4567-e89b-12d3-a456-426614174000", "username": "asdasddas"},
#                            {"user_id": "123e4567-e89b-12d3-a456-426614174003", "username": 123}]}
# json_with_UUID_solo = {"data": {"user_id": "123e4567-e89b-12d3-a456-426614174001", "username": "ivan"}}
# resp_after_valid = dataClass.model_validate(json_with_UUID)
# print(resp_after_valid)
# print(resp_after_valid.data[0].username)


from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class ASDf(BaseModel):
    item_id: UUID = Field(default_factory=uuid4)
    id: UUID = Field(default_factory=uuid4)


asd = ASDf()
print(asd.model_dump_json())

class ASDf(BaseModel):
    item_di: UUID = Field(default_factory=lambda :str(uuid4())) #-> NONE  # NONE ->
    id: UUID #= str(uuid4()) #-> 1 раз





asd = ASDf()
ssss = ASDf()#id = asd.id item_di-> NONE
print(asd.model_dump_json())

# class userAge(BaseModel):
#     age: int
#     type: str
#
# class dataClassAge(BaseModel):
#     data: List[userAge]
#
#     @model_validator(mode='after')
#     def check_uniq_id(self, info: ValidationInfo) -> Self:
#         for k in self.data:
#             if not (k.age >= 18 and k.type == 'adult'):
#                 raise ValueError('age or type not equal')
#         return self
#
# json_age ={"data": [{'age': 18, 'type': 'adult'},{'age': 15, 'type': 'adult'}, {'age': 18, 'type': 'asd'}, ]}
# try:
#     dataClassAge.model_validate(json_age)
# except ValidationError as e:
#     print(e)
#     print(e.errors())
#     print(repr(e.errors()[0]['type']))

