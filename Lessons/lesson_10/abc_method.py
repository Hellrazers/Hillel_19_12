from abc import ABC, abstractmethod

class DB(ABC):
    @abstractmethod
    def db_conn(self):
        pass

    @abstractmethod
    def db_close(self):
       pass
    #
    # @staticmethod
    # @abstractmethod
    # def db_test():
    #     pass

    # @abstractmethod
    # def db_test_2(self):
    #     pass

    # @staticmethod
    # def db_close_1():
    #     pass


    def new_method(self):
        raise NotImplementedError()

class PostresDB(DB):
    def db_conn(self):
        # self.print_1(1 , 0)
        print('PostresDB.db_conn()')

    def db_close(self):

        print('PostresDB.db_close()')
    #
    def db_test(self):
        print('PostresDB.db_test()')
        balance = self.print_1(1423, 123)
        assert balance == 0
        print("Test Correct")

    @staticmethod
    def print_1(debit, credit):
        print('-' * 20)

        return debit - credit


    def db_test_2(self):
        pass

class MysqlDB(DB):
    def db_conn(self):
        print('MysqlDB.db_conn()')

    def db_close(self):
        print('MysqlDB.db_close()')

    def db_test(self):
        print('MysqlDB.db_test()')


    def new_method(self):
        print('MysqlDB.new_method()')


class DbRequest:
    def __init__(self, db_name):
        if db_name == 'MysqlDB':
            self.db = MysqlDB()
        elif db_name == 'PostresDB':
            self.db = PostresDB()


    def find_users_by_id(self, id):
        self.db.db_conn()
        self.db.db_test()
        # print('find_users_by_id({id})'.format(id=id))
        print(f'find_users_by_id({id})')
        self.db.db_close()

    def new_method(self):
        self.db.new_method()

    # def db_test(self):
    #     pass

mysql_db = DbRequest('MysqlDB')
postres_db = DbRequest('PostresDB')
# mysql_db.find_users_by_id(5)
print('\n')
postres_db.find_users_by_id(111111115)