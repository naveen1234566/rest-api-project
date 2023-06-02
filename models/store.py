from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic")
    tags = db.relationship("TagModel", back_populates = "store", lazy ="dynamic")
    
    
# class ItemModel(db.Model):
#     __tablename__ = "items"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=False, nullable=False)
#     description = db.Column(db.String)
#     price = db.Column(db.Float(precision=2), unique=False, nullable=False)
#     store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)
#     store = db.relationship("StoreModel", back_populates="items")
#     tags = db.relationship("TagModel", back_populates="items", secondary="items_tags")
    
# class TagModel(db.Model):
#     __tablename__ = "tags"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=False, nullable=False)
#     store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)

#     store = db.relationship("StoreModel", back_populates="tags")
#     items = db.relationship("ItemModel", back_populates="tags", secondary="items_tags")
# class ItemsTags(db.Model):
#     __tablename__ = "items_tags"

#     id = db.Column(db.Integer, primary_key=True)
#     item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
#     tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))