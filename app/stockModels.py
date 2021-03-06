from .apps import db

class StockBasicInfo(db.Model):
    __tablename__ = 'sa_stockbasicinfo'
    id = db.Column(db.INTEGER, primary_key=True)
    code = db.Column(db.String(6))
    name = db.Column(db.String(6))
    price = db.Column(db.String(6))
    pe = db.Column(db.String(6))
    pb = db.Column(db.String(6))
    bankuai = db.Column(db.String(20))
    enable = db.Column(db.INTEGER)
    relatedStock = db.Column(db.String)


class StockDetail(db.Model):
    __tablename__ = 'sa_stockdetail'
    id = db.Column(db.INTEGER, primary_key=True)
    code = db.Column(db.String(6))
    name = db.Column(db.String(6))
    content = db.Column(db.String)
    title = db.Column(db.String)
    seq = db.Column(db.String)


class MeiTanExtend(db.Model):
    __tablename__ = 'sa_maitan_extend'
    id = db.Column(db.INTEGER, primary_key=True)
    code = db.Column(db.String(6))
    chanliang = db.Column(db.INTEGER)
    channeng = db.Column(db.INTEGER)
    beizhu = db.Column(db.String)


class DazongUrls(db.Model):
    __tablename__ = 'sa_dazong_urls'
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.INTEGER)
    url = db.Column(db.INTEGER)
    enable = db.Column(db.INTEGER)
    remarks = db.Column(db.String)

class Article(db.Model):
    __tablename__ = 'sa_bankuai_article'
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    relatedStocks = db.Column(db.String)
    bankuai = db.Column(db.String)
    remarks = db.Column(db.String)