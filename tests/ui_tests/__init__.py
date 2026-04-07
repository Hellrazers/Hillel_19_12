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

#evaluate("el => window.getComputedStyle(el)

#.wait_for_load_state("networkidle")
# "base_url": base_url,


# with page.expect_response("**/api/cars") as response_info:
#     # Твоя дія, яка тригерить POST запит
#
#
# # Отримуємо об'єкт відповіді
# response_id = response_info.value


# dialog_messages = []
# page.on("dialog", lambda d: [dialog_messages.append(d.message), d.accept()])
# page.locator("#alert-btn").click()
# assert "Hello! I am an alert box!" in dialog_messages[0]