from app import db
import datetime


class StockMarketDay(db.Model):
    __tablename__ = 'STOCKS_MARKET_DAY'
    StockId = db.Column(db.Integer, primary_key=True)
    StartTime = db.Column(db.TIMESTAMP, default=datetime.datetime.now())
    type = db.Column(db.VARCHAR)
    activity = db.Column(db.INT)
    price_1 = db.Column(db.VARCHAR)

    def __init__(self, stock_id, start_time, stock_type, activity):
        self.StockId = stock_id
        self.StartTime = start_time
        self.type = stock_type
        self.activity = activity

    def __repr__(self):
        return '<stock %r>' % self.StockId


if __name__ == '__main__':
    # stock = StockMarketDay(type='top', StockId='15000', price_1='20', activity=1)
    # stock.price_1 = '20.97'
    # # stock.type = 'top'
    # # stock.activity = 11
    # # stock.price_1(20)
    # # stock.StockId(300000)
    # # print(stock.type)
    # db.session.add(stock)
    #
    # db.session.commit()

    stock = StockMarketDay.query.all()
    for s in stock:
        db.session.delete(s)
    db.session.commit()

    # s = StockMarketDay(100, datetime.datetime.now(), 'top', 1)
    # s1 = StockMarketDay(1001, datetime.datetime.now(), 'top', 1)
    # s1.price_1 = '20.94'
    # ss = [s, s1]
    # db.session.add_all(ss)
    # db.session.commit()
