import datetime as dt

import pandas as pd
import tushare as ts

import app.file.write_file_os as wfo


def get_basic_stock_path(check):
    if check:
        return wfo.mk_basic_path() + 'basic_stock.csv'
    else:
        return wfo.get_basic_path() + 'basic_stock.csv'


def write_basic_stock():
    df = pd.DataFrame(ts.get_stock_basics())
    path = get_basic_stock_path(True)
    df.to_csv(path)
    df = get_basic_stock()
    __add_later_row(df, 2)
    df.to_csv(path)


def get_basic_stock():
    path = get_basic_stock_path(False)
    return pd.read_csv(path)


def is_later(code, day=365):
    try:
        df = get_basic_stock()
        date_str = df[df.code == code].timeToMarket.values[0]
        date = dt.datetime.strptime(str(date_str), "%Y%m%d")
        return dt.datetime.now() - date < dt.timedelta(days=day)
    except ValueError:
        return 0
    except IndexError:
        return 1


def __add_later_row(df, index):
    df.insert(index, 'later', df.get('code').apply(lambda x: is_later(x)))


def _get_later(code):
    try:
        df = get_basic_stock()
        return df[df.code == code].later.values[0]
    except IndexError:
        return 2


def add_later_row(df, index):
    df.insert(index, 'later', df.get('code').apply(lambda x: _get_later(x)))


def get_outstanding(code):
    df = get_basic_stock()
    return df[df.code == code].outstanding.values[0]


def add_outstanding_row(df, index):
    df.insert(index, 'outstanding', df.get('code').apply(lambda x: get_outstanding(x)))



# print(_get_later(300742))

# write_basic_stock()

# write_basic_stock()

#
# print(is_later(3511))
# print(is_later(300705))
