from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#engine = create_engine('sqlite:///db/odin.db', echo = False) 
engine = create_engine('postgresql://kvdrcziuilhlad:406563816a6f61cdc320ec01e8c1e23b852d6f49f2d7e112551fc461e1f6c564@ec2-184-73-25-2.compute-1.amazonaws.com:5432/d7pkbp026e5o8h', echo = False) 

Session = sessionmaker(bind = engine)

Base = declarative_base()
