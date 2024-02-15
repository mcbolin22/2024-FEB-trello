from init import db, ma
from marshmallow import fields

class Card(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    date = db.Column(db.Date) # date the card was created
    status = db.Column(db.String)
    priority = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # uses __tablename__ users.id

    user = db.relationship('User', back_populates='cards') # Uses class of user.py 

    class CardSchema(ma.Schema):

        user = fields.Nested('UserSchema', only = ['name', 'email'])
        class Meta:

            fields = ('id', 'title', 'description', 'date', 'status', 'priority', 'user')

    card_schema = CardSchema()
    cards_schema = CardSchema(many=True)