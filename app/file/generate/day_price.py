import tushare as ts
import pandas as pd
import datetime as dt
import app.file.write_file_os as wfo


def to_date(date_str):
    return dt.datetime.strptime(str(date_str), "%Y-%m-%d")


def from_date(date):
    return date.strftime("%Y-%m-%d")


def get_file_name(code):
    path = wfo.get_day_path(code)
    return path + code


def write_day_price(code):
    df = ts.get_k_data(code)
    file_name = get_file_name(code)
    df.to_csv(file_name, sep=',', header=True, index=False)


def get_code_day(code, day):
    file = get_file_name(code)
    df = pd.read_csv(file)
    return df[df.get('date') == day]


def get_day_close_price(code, day):
    df = get_code_day(code, day)
    return df.close.values[0]


def get_day_open_price(code, day):
    df = get_code_day(code, day)
    return df.open.values[0]


def get_code_change_day(code, day):
    file = get_file_name(code)
    df = pd.read_csv(file)
    close = df[df.get('date') == day].close.values[0]
    print(close)
    yesterday_index = df[df.date == day].index.values[0] - 1
    yesterday_close = df[df.index == yesterday_index].close.values[0]
    print(yesterday_close)
    return ((close - yesterday_close) * 100 / yesterday_close).round(2)


if __name__ == '__main__':
    write_day_price('300715')
    a = get_code_change_day('300715', '2018-04-26')
    print(a)
