from threading import Thread
import time
import requests

from metro_news.api.app import app
from metro_news.utils.parser_page import Parsing
from metro_news.config.const import (
    URL_METRO_NEWS, TIMEOUT_PARSE, HOST_SERVER, PORT_SERVER
)
from metro_news.logger import logger

logger = logger("app")


def worker_parser():
    """
    Worker парсинга новостей (каждые TIMEOUT_PARSE секунд)
    """
    while True:
        logger.info('Начало работы worker`a')
        url = URL_METRO_NEWS
        response = requests.get(url)
        response_text = response.text
        logger.info('Статус ответа сайта: {}'.format(response.status_code))
        Parsing(response_text).run()
        time.sleep(TIMEOUT_PARSE)


def main():
    Thread(target=worker_parser).start()
    app.run(host=HOST_SERVER, port=PORT_SERVER)


if __name__ == '__main__':
    main()
