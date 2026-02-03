import unittest



import sys
import pathlib

# DATA_DIR = str(pathlib.Path(__file__).resolve().parents[2])
DATA_DIR = str(pathlib.Path(__file__).parent.parent.parent)

sys.path.insert(0, DATA_DIR)

from core.fuction import function_sub
# pathlib.Path(__file__).resolve().parents[2]




class MyTest(unittest.TestCase):

    def setUp(self):
        # print("Set Up")
        self.a = 3
        self.b = 4
        self.result = None

    def tearDown(self):
        # print("Tear Down")
        # if self.result is not None:
        #     print(f"Our test finish with this result {self.result}")
        pass
    def test_example_pass(self):
        # print('test_example_pass')
        self.result = function_sub(self.b, self.a)


    def test_example_json(self):
        data = [
            {
                "user_id": 1,
                "name": "Den",
                "some_list": ["value1", "value2"]
            },
            {
                "user_id": 2,
                "name": "Vlad",
                "some_list": ["value1", "value2"]
            }
        ]
        # ()
        list_name: list  = []
        for e in data:
            value = e.get('user_id')            # e['user_id']
            if value == 1:
                list_name.append(e)

        list_2 = [k for k in data if k.get('user_id') == 1][0]
        dict_of_value = list_name[0]
        expected_result = {
                "user_id": 2,
                "name": "Den",
                "some_list": ["value1", "value2"]
            }
        # self.assertEqual(list_name[0].get('user_id'), expected_result.get('user_id'))


        list_of_assert = []
        try:
            assert list_name[0].get('user_id') == expected_result.get('user_id'), f'assert user_id where AR: {list_name[0].get('user_id')} and EXP { expected_result.get('user_id')}'
        except AssertionError as e:
            list_of_assert.append(f'assert user_id where AR: {list_name[0].get('user_id')} and EXP { expected_result.get('user_id')}')
        try:
            assert dict_of_value.get('name') == expected_result.get('name'),  f"assert name where AR: {list_name[0].get('name')} and EXP { expected_result.get('name')}"
            self.assertEqual(dict_of_value.get('name'), expected_result.get('name'))
        except AssertionError as e:
            list_of_assert.append( f"assert name where AR: {list_name[0].get('name')} and EXP { expected_result.get('name')}")


        # list = [] false
        # list = [1,2 ]
        # assert  1 == 2
        assert len(list_of_assert) ==0 , f'our prblem with this assert, {list_of_assert}'


        # print(list_name)


    def test_example_assert(self):
        self.assertIs(True, True)
        self.assertIn(2, [2,4,5])
        self.assertAlmostEqual(5, 6, delta=1)

        self.assertGreater(5, 2)
        assert 5 > 2
        #
        # self.asse

    def test_example_1(self):
        # print('test_example_1')

        a = self.a
        b = self.b
        result = a + b
        EXCEPTED_RESULT = 7
        # assert result == 6
        self.assertEqual(result, EXCEPTED_RESULT, f'something is wrong {a} - {b} != {EXCEPTED_RESULT}')
        self.result = result
        # self.ass
        # self.assertEqual(expected_result, result)

    def test_example_2(self):
        # print('test_example_2')
        self.result = self.a ** self.b



if __name__ == '__main__':
    unittest.main(verbosity=1)




# def test_   _test():


'''

Pre -step 
autrorization  = login 
token 
Auth: Berare token 


        pre_step_before_test :
            mike -> vasya 
            id  - deleted
            Create user



Test     -f 
test2 


        post_step:   is_delted: True
            delete user


finish step
logout 






'''

