from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
# from flask_user import UserMixin (if doing auth)
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()

class ModelABC(object):
    """ Abstract Base class so everything has pk, is stamped, and serialize-able """

    id = db.Column(db.Integer, primary_key=True) # 1st int PK = autoincrement in SQLalc.
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    #def __repr__(self):
    #    return str(self.id)

    # Useful iff plan to provide an API
    def serialize(self):
        """ Basic, but enough for now """
        return {c: str(getattr(self, c)) for c in inspect(self).attrs.keys()}

    def commit(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            db.session.rollback()
            raise Exception("Failed creating record '"+name+"', already exists?")

    @staticmethod
    def serialize_list(l):
        """ Static method, read-only, no instance, no class... """
        return [m.serialize() for m in l]

class Product(ModelABC, db.Model):
    """ w/ SKU (currently 1 char, but standards dictate upto 16 reasonably) """

    sku = db.Column(db.String(16), nullable=False, unique=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    price = db.Column(db.Float(), nullable=False, server_default='0.0')

    @classmethod
    def create(cls, sku, name, description, price):
        # Caller will handle exception if applicable
        return Product(sku=sku,name=name,description=description,price=price).commit()

class Offer(ModelABC, db.Model):
    """ Currently single product quantity based """

    # one to one, though arguably one to many if future offers span products?
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    price = db.Column(db.Float(), nullable=False, server_default='0.0')
    quantity = db.Column(db.Integer, nullable=False, server_default='1')
    enabled = db.Column(db.Boolean(), nullable=False, server_default='1')

    @classmethod
    def create(cls, product_id, price, quantity, enabled=True):
        return Offer(product_id=product_id, price=price, quantity=quantity, enabled=enabled).commit()

