from API import db

class INSS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sal_min = db.Column(db.Numeric(10,2), nullable=False)
    sal_max = db.Column(db.Numeric(10,2), nullable=False)
    aliquota = db.Column(db.Integer, default=0)
    deducao = db.Column(db.Numeric(10,2), nullable=False)
    
    def __repr__(self):
        return '%r' % self.id

class IPR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sal_min = db.Column(db.Numeric(10,2), nullable=False)
    sal_max = db.Column(db.Numeric(10,2), nullable=False)
    aliquota = db.Column(db.Integer, default=0)
    deducao = db.Column(db.Numeric(10,2), nullable=False)
    
    def __repr__(self):
        return '%r' % self.id
    
db.create_all()