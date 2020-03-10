from application import db, login_manager
from flask_login import UserMixin

class menu(db.Model):
    DishID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100), nullable=False, unique=True)
    Type = db.Column(db.String(50), nullable=False, unique=True)
    Price = db.Column(db.Integer, nullable=False, unique=True)
    Typedish = db.relationship('Typedish')

    def __repr__(self):
         return ''.join([
             'DishID: ', self.DishID, '\r\n',
             'Description: ', self.Title, '\r\n', self.Type, '\r\n', self.Price,'\r\n'
    ])

@login_manager.user_loader
def load_user(MemberID):
    return Member.query.get(int(MemberID))

class member(db.Model, UserMixin):
    MemberID = db.Column(db.Integer, primary_key=True)
    FullName = db.Column(db.String(30), nullable=False)
    HouseNo = db.Column(db.String(30), nullable=False)
    Street = db.Column(db.String(30), nullable=False)
    Postcode = db.Column(db.String(30), nullable=False)
    EmailAddress = db.Column(db.String(150), nullable=False, unique=True)
    Password = db.Column(db.String(500), nullable=False)
    Purchase = db.relationship('Typedish')

def __repr__(self):
   return ''.join([
            'User ID: ', self.user_id, '\r\n',
        ])

class Typedish(db.Model):
    MemberlID = db.Column(db.Integer, primary_key=True)
    VegetarianID = db.Column(db.Intreger, db.ForeignKey('menu.DishID'), primary_key=True, nullable=False)
    HotID = db.Column(db.String(3), nullable=False)

    def __repr__(self):
         return ''.join([
             'User ID: ', self.user_id, '\r\n',
    ])
