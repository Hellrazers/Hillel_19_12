# from faker import Faker
#
# fake = Faker()
# create_table = '''CREATE TABLE public.users (
# 	id serial4 NOT NULL,
# 	"name" varchar NULL,
# 	jobs varchar NULL,
# 	CONSTRAINT users_pk PRIMARY KEY (id)
# );'''
#
# add_user = '''INSERT INTO public.users ("name", jobs) VALUES ('Oleksii', 'AQA');'''
#
#
# update_user = '''UPDATE public.users SET "name" = 'Vlad', jobs = 'Manager' WHERE id >= 5;'''
#
#
#
# delete_user = '''DELETE FROM users WHERE id = 5;'''
#
#
#
#
#
# def test_add_user(cursor_con):
#     cursor, conn = cursor_con
#     name_er = fake.first_name()
#     print(name_er)
#     jobs_er = fake.job()
#     print(jobs_er)
#
#     cursor.execute(f'''INSERT INTO public.users ("name", jobs) VALUES ('{name_er}', '{jobs_er}') RETURNING id;''')
#     user_id = cursor.fetchone()[0] #-> ({id}, )
#
#     cursor.execute(f'''SELECT "name", jobs FROM public.users WHERE id = {user_id}''')
#     name_ar, jobs_ar = cursor.fetchone()
#
#     assert name_er == name_ar
#     assert jobs_er == jobs_ar
#
#
# def test_del_user(cursor):
#     cursor = cursor
#     name_er = fake.first_name()
#     print(name_er)
#     jobs_er = fake.job()
#     print(jobs_er)
#
#     cursor.execute(f'''INSERT INTO public.users ("name", jobs) VALUES ('{name_er}', '{jobs_er}') RETURNING id;''')
#     user_id = cursor.fetchone()[0]  # -> ({id}, )
#
#     cursor_extcute_str = f'''DELETE FROM users WHERE id = {user_id} returning id;'''
#     cursor.execute(cursor_extcute_str)
#     user_id_delete = cursor.fetchone()[0]
#     assert user_id == user_id_delete
#
#     cursor.execute(f'''SELECT id jobs FROM public.users WHERE id = {user_id}''')
#     result = cursor.fetchone()
#
#     assert result is None
#
#
# def test_join_user(cursor):
#     cursor = cursor
#     name_er = fake.first_name()
#     print(name_er)
#     jobs_er = fake.job()
#     print(jobs_er)
#
#     cursor.execute(f'''SELECT id, "name", surname, phone FROM public.users JOIN public.user_details ON public.users.id = public.user_details.user_id;''')
#     result = cursor.fetchall()
#
#     assert len( result) == 2
#
#     # conn.commit()
