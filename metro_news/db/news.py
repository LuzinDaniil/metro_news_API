from .decorate import scoped_session
from .models import NewsModel
from datetime import datetime, timedelta
from metro_news.api.schema import NewsOrmSchema


class NewsManager:
    @scoped_session
    def set(self, session, news_items):
        if len(news_items) > 1:
            news = []
            for new_items in news_items:
                news.append(NewsModel(**new_items))
            session.bulk_save_objects(news)
        else:
            news = NewsModel(**news_items[0])
            session.add(news)
        session.commit()

    @scoped_session
    def get_all_id(self, session):
        return [i[0] for i in session.query(NewsModel.id).all() or [('',)]]

    @scoped_session
    def get_period_ago(self, session, period):
        period_ago = datetime.now() - timedelta(days=period)
        subject_last_period = session.query(NewsModel).filter(NewsModel.date >= period_ago).all()

        return [NewsOrmSchema.from_orm(subj).dict() for subj in subject_last_period]
