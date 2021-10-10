from .connect import Session


def scoped_session(func):
    def wrapper(*args, **kwargs):
        session = Session()
        returned = func(*args, session=session, **kwargs)
        session.close()
        return returned
    return wrapper
