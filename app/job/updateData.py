import app.file.generate.today_all_file as taf
import app.file.generate.write_basic as wb
import app.file.generate.write_classified as wc
import app.file.generate.write_profit as wp
import tushare as ts
import app.data.top_today as tt
import app.model as model
import datetime
import app.enum.market_type as m_type

if __name__ == '__main__':
    today_all = ts.get_today_all()
    #
    # wb.write_basic_stock()
    # wc.update()
    # taf.do_all()
    # wp.update_profit()

    # write db
    # 一字涨停
    one_top = tt.is_one_top(today_all)
    one_top_list = []
    for row in one_top.rows:
        stock = model.StockMarketDay(row['code'], datetime.datetime.now(), m_type.MarketType.one_top.name, 1)
        one_top_list.append(stock)
    print(one_top_list)
