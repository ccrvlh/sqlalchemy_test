import sqlalchemy as db
from sqlalchemy.orm import relationship

from app.engine import Base, BaseMixin


class User(BaseMixin, Base):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}  # type: ignore

class Tenant(BaseMixin, Base):
    __tablename__ = "tenant"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class AccountClassification(BaseMixin, Base):
    __tablename__ = "acc_class"
    id = db.Column(db.Integer, db.Identity(start=1000, cycle=True), primary_key=True)
    classification = db.Column(db.String, unique=True)
    is_balance_sheet = db.Column(db.Boolean)
    children = relationship("AccountType", backref="classification", lazy="noload")


class AccountType(BaseMixin, Base):
    __tablename__ = "acc_type"
    id = db.Column(db.Integer, db.Identity(start=1000, cycle=True), primary_key=True)
    title = db.Column(db.String, unique=True)
    parent = db.Column(db.String, db.ForeignKey("acc_class.classification"))
    children = relationship("AccountSubType", lazy="noload")


class AccountSubType(BaseMixin, Base):
    __tablename__ = "acc_subtype"
    id = db.Column(db.Integer, db.Identity(start=1000, cycle=True), primary_key=True)
    subtype = db.Column(db.String, unique=True)
    parent = db.Column(db.String, db.ForeignKey("acc_type.title"))

