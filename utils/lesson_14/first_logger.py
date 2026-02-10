import logging
import sys

import requests

# Налаштування конфігурації логування
# logging.basicConfig(filename='example.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stdout)


# Додавання обробника для виводу в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console_handler)


# Логування подій різного рівня (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logging.debug('first level DEBUG')
logging.info('second level INFO')
logging.warning('third WARNING')
logging.error('Це повідомлення рівня ERROR')
logging.critical('Це повідомлення рівня CRITICAL')





# print('asdasdasdasd')
# requests._get()
# logging.debug('first level DEBUG')
