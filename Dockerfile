FROM python:3
COPY metro_news/ metro_news/
ADD app.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
WORKDIR "metro_news"
RUN alembic upgrade head
WORKDIR "../"
CMD [ "python", "app.py" ]
