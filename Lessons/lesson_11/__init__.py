# # Є клас Student з полями: full_name, age, avg_grade. +
# # Є клас Group. +
# # У групі може бути тільки один group_leader (староста).
# # Староста не може бути доданий у список students двічі.
# # У групі може бути максимум 30 студентів.
# # У групу не можна додати студента, якщо: age < 16 avg_grade не в діапазоні 0..12
# # Методи: add_student(student) remove_student(full_name) set_leader(student) top_students(n) → повертає топ-N за avg_grade покажи реалізацію
#
#
#
# class Student:
#
#     def __init__(self, full_name, age, avg_grade):
#         self.full_name = full_name
#         self.age = age
#         self.avg_grade = avg_grade
#
#     # def __repr__(self):
#     #     return f"{self.full_name} age: {self.age} grade: {self.avg_grade}"
#     #
#
#
# class Group:
#     MAX_GROUP_SIZE = 30
#
#     def __init__(self):
#         self.students = []
#         self.group_leader = None
#
#     def add_student(self, student: Student):
#         if student.age < 16:
#             raise ValueError("Age must be greater than 16")
#         if not 0 < student.avg_grade <= 12:
#             raise ValueError("Average grade must be between 0 and 12")
#         if len(self.students) > self.MAX_GROUP_SIZE:
#             raise ValueError("Group size maximum")
#
#         self.students.append(student)
#
#     def set_leader(self, student):
#         if student not in self.students:
#             raise ValueError("Student not in group")
#         self.group_leader = student
#
#
#     def top_students(self):
#         return sorted(self.students, key=lambda student: student.avg_grade, reverse=True)
#         # self.students.sort(key=lambda student: student.avg_grade, reverse=True)
#
#
# hillel_group = Group()
# misha_student = Student("Misha", 17, 10)
# sveta_student = Student("Sveta", 22, 1)
# denys_student = Student("Sveta", 22, 2)
# igor_student = Student("Sveta", 22, 4)
#
# misha_student_wrong_age = Student("Misha", 16, 15)
# # hillel_group.add_student(misha_student_wrong_age)
# hillel_group.students.append(misha_student)
# hillel_group.students.append(sveta_student)
# hillel_group.students.append(denys_student)
# hillel_group.students.append(igor_student)
#
# print(hillel_group.students)
# hillel_group.set_leader(misha_student)
#
# print(hillel_group.group_leader, 'first leader')
#
# hillel_group.set_leader(sveta_student)
# print(hillel_group.group_leader, 'second leader')
#
#
# list_student_after_sort = hillel_group.top_students()
# print(list_student_after_sort)
# print(hillel_group.students)
#
# print(list_student_after_sort[0].age)
# print(list_student_after_sort[0].full_name)