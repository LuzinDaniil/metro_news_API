import lxml.html
from lxml import html
import re
from datetime import datetime
from metro_news.db.news import NewsManager
from metro_news.api.schema import NewsSchema
from metro_news.config.const import MONTH_REPLACE

from metro_news.logger import logger

logger = logger("parser_page")

COMPILE_RE = re.compile('http[^)]+')


class Parsing:
    def __init__(self, response_text: str):
        self.response_text = response_text

    def run(self) -> None:
        """
        Запуск парисинга страницы и запись в БД
        """
        insert_news = self.parse_news(self.response_text)
        logger.debug('Количество добавлямых новостей: {}'.format(len(insert_news)))
        if insert_news:
            NewsManager().set(news_items=insert_news)

    def parse_news(self, page: str) -> list:
        """
        Парсинг страницы, вывести список новых новостей для сохранения
        """
        parsed_body = html.fromstring(page)
        insert_news = []

        links_parsed = set(parsed_body.xpath('//a[contains(@class,"news-card")]'))
        all_news = NewsManager().get_all_id()
        for link_parse in links_parsed:
            title, image, url, date = None, None, None, None
            for a_block in link_parse.getchildren():
                div_class = a_block.classes
                if 'news-card__caption' in div_class:
                    title = self._parse_title(a_block)
                elif 'news-card__image' in div_class:
                    image = self._parse_image(a_block)
                elif 'news-card__date' in div_class:
                    date = self._parse_date(a_block)

            url = self._parse_url(link_parse)
            news_id = url.rsplit('news=')[-1]
            if news_id not in all_news:
                news_obj = NewsSchema(id=news_id, title=title, image=image, url=url, date=date,
                                      processing_date=datetime.now())
                insert_news.append(news_obj.dict())
                logger.debug('Добавлена новая новость {}'.format(news_id))
                all_news.append(news_id)

        return insert_news

    def _parse_title(self, div_obj: lxml.html.HtmlElement) -> str:
        """
        Парсинг заголовка новости
        """
        return div_obj.text

    def _parse_image(self, div_obj: lxml.html.HtmlElement) -> str:
        """
        Парсинг url картинки
        """
        style_str = div_obj.attrib.get('style')
        match = COMPILE_RE.search(style_str)
        return match[0]

    def _parse_date(self, div_obj: lxml.html.HtmlElement) -> datetime:
        """
        Парсинг даты публикации
        """
        date_raw = div_obj.text
        for old, new in MONTH_REPLACE:
            date_raw = date_raw.replace(old, new)
        date_raw = str(datetime.now().year) + ' ' + date_raw
        date = datetime.strptime(date_raw, '%Y %d %m, %H:%M')
        return date

    def _parse_url(self, a_obj: lxml.html.HtmlElement) -> str:
        """
        Парсинг url новости
        """
        return a_obj.attrib.get('href')
