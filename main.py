import logging
import sys
sys.path.append('lib')
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root@localhost/test',
                       echo=True,
                       pool_recycle=60,
                       encoding="utf-8" )

Base = declarative_base()
class User(Base):
    __tablename__  = 'users'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id   = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True)

    def __init__(self, name, fullname, password):
        self.name = name

    def __repr__(self):
       return "<User('%s')>" % (self.name)

def main():
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess    = Session()
    for i in sess.query(User).all():
        logging.debug(i)
        logging.debug(i.name)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info('hello')
    main()
