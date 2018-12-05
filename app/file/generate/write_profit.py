import os

import pandas as pd
import tushare as ts

import app.file.generate.write_basic as wb
import app.file.write_file_os as wfo
import app.file.generate.write_classified as wc
import app.file.generate.today_all_file as taf


##高送转##

def mk_profit_path():
    path = wfo.get_basic_path() + "profit/"
    exists = os.path.exists(path)
    if exists:
        return path
    else:
        os.makedirs(path)
        return path


def __get_path(name):
    return mk_profit_path() + name


def get_profit_path():
    return __get_path('profit.csv')


def get_high_profit_path():
    return __get_path('high_profit.csv')


def get_mid_profit_path():
    return __get_path('mid_profit.csv')


def get_low_profit_path():
    return __get_path('low_profit.csv')


def get_later_profit_path():
    return __get_path('later_profit.csv')


def write_profit():
    top = wb.get_basic_stock().index.size
    df = ts.profit_data(top=top)
    path = get_profit_path()
    df.to_csv(path, index=False)


def __add_row(df, from_index):
    wc.add_classified_all_row(df, from_index)
    taf.add_nmc_row(df, from_index)
    wb.add_outstanding_row(df, from_index)
    wb.add_later_row(df, from_index)


def write_high_profit():
    path = get_profit_path()
    df = pd.read_csv(path)
    df = df[df.shares >= 10]
    path = get_high_profit_path()
    __add_row(df, 2)
    df.to_csv(path, index=False)


def write_mid_profit():
    path = get_profit_path()
    df = pd.read_csv(path)
    df = df[df.shares >= 5]
    df = df[df.shares < 10]
    path = get_mid_profit_path()
    __add_row(df, 2)
    df.to_csv(path, index=False)


def write_low_profit():
    path = get_profit_path()
    df = pd.read_csv(path)
    df = df[df.shares > 0]
    df = df[df.shares < 5]
    path = get_low_profit_path()
    __add_row(df, 2)
    df.to_csv(path, index=False)


def write_later_profit():
    path = get_profit_path()
    df = pd.read_csv(path)
    df = df[df.shares > 0]
    df = df[df.shares < 5]
    path = get_low_profit_path()
    __add_row(df, 2)
    df.to_csv(path, index=False)


def update_profit():
    mk_profit_path()
    write_profit()
    write_high_profit()
    write_mid_profit()
    write_low_profit()
