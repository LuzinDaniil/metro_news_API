import os

URL_METRO_NEWS = 'https://mosmetro.ru/news/'
TIMEOUT_PARSE = int(os.environ.get('TIMEOUT_PARSE', str(10 * 60)))

HOST_SERVER = '0.0.0.0'
PORT_SERVER = int(os.environ.get('PORT_SERVER', '5000'))

MONTH_REPLACE = [('января', '01'), ('февраля', '02'), ('марта', '03'), ('апреля', '04'), ('мая', '05'),
                 ('июня', '06'), ('июля', '07'), ('августа', '08'), ('сентября', '09'), ('октября', '10'),
                 ('ноября', '11'), ('декабря', '12')]

LOG_FORMAT_DEBUG = "%(asctime)s %(name)s line: %(lineno)d -%(levelname)s | %(message)s"

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)))
BASEDIR = os.path.split(PATH)[0]
DIRECTORY_OF_LOGS = os.path.join(BASEDIR, 'logs')
print(DIRECTORY_OF_LOGS)
os.makedirs(DIRECTORY_OF_LOGS, exist_ok=True)

