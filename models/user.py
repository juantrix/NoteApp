from . import Base, engine
import sqlalchemy as sa


class User(Base):
    __tablename__ = 'User'

    id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.String(80), nullable=False)
    email = sa.Column(sa.String(150), nullable=False)
    password = sa.Column(sa.String(64), nullable=False)

    def __str__(self):
        return self.name




