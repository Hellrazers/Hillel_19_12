#
# let el = $('#addCarBrand');
# console.log(el.options[el.selectedIndex].text)


#



# # 1. Глобально передаємо доступи (Basic Auth) для всіх тестів
# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         "http_credentials": {
#             "username": "guest",
#             "password": "welcome2qauto"
#         }
#     }

# addopts = -s -v --headed --output=my_results --tracing=on


# playwright show-trace my_results/*/trace.zip
