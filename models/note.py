from datetime import date
from . import Base, engine
import sqlalchemy as sa


class Note(Base):
    __tablename__ = 'Note'

    id = sa.Column(sa.Integer(), primary_key=True)
    user = sa.Column(sa.String(80), nullable=False)
    title = sa.Column(sa.String(64), nullable=False)
    body = sa.Column(sa.String(350), nullable=False)
    date = sa.Column(sa.Date(), default=date.today())

    def __str__(self):
        return self.name
