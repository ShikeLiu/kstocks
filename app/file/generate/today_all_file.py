import pandas as pd
import tushare as ts
import os

import app.data.top_today as tt
import app.file.write_file_os as wfo
import app.file.generate.write_classified as wc
import app.file.generate.write_basic as wb


def get_file_name(directory, name):
    return wfo.make_dir_today(directory) + name


def get_gen_file_name(name):
    return get_file_name('generated/', name)


def get_root_file_name():
    return get_file_name('source/', 'today_all.csv')


def write_today_all():
    today_all = ts.get_today_all()
    df = pd.DataFrame(today_all)
    file_name = get_root_file_name()
    df.to_csv(file_name, sep=',', header=True, index=False)
    return file_name


def read_today_all():
    file_name = get_root_file_name()
    return pd.read_csv(file_name)


def __add_row(df, from_index):
    wc.add_classified_all_row(df, from_index)
    wb.add_later_row(df, from_index)


# def get_concept_classified_file_name():
#     return get_file_name('source/', 'concept_classified.csv')
#
#
# def write_concept_classified():
#     df = ts.get_concept_classified()
#     file_name = get_concept_classified_file_name()
#     df.to_csv(file_name, sep=',', header=True, index=False)
#     return file_name
#
#
# def read_concept_classified():
#     file_name = get_concept_classified_file_name()
#     return pd.read_csv(file_name)


def write_one_top(df):
    file_name = get_gen_file_name('one_top.csv')
    pd.DataFrame(tt.is_one_top(df)).to_csv(file_name, sep=',', header=True, index=False)
    return file_name


def write_normal_top(df):
    file_name = get_gen_file_name('normal_top.csv')
    pd.DataFrame(tt.not_one_top(df)).to_csv(file_name, sep=',', header=True, index=False)
    return file_name


def write_raise(df):
    file_name = get_gen_file_name('had_top.csv')
    pd.DataFrame(tt.had_top(df)).to_csv(file_name, sep=',', header=True, index=False)
    return file_name


def write_had_top(df):
    file_name = get_gen_file_name('raise_1.05.csv')
    pd.DataFrame(tt.raise_percent(df, 1.05)).to_csv(file_name, sep=',', header=True, index=False)
    return file_name


def write_one_down(df):
    file_name = get_gen_file_name('one_down.csv')
    pd.DataFrame(tt.is_one_down(df)).to_csv(file_name, sep=',', header=True, index=False)
    return file_name


def write_normal_down(df):
    file_name = get_gen_file_name('normal_down.csv')
    pd.DataFrame(tt.not_one_down(df)).to_csv(file_name, sep=',', header=True, index=False)
    return file_name


def write_had_down(df):
    file_name = get_gen_file_name('had_down.csv')
    pd.DataFrame(tt.had_down(df)).to_csv(file_name, sep=',', header=True, index=False)
    return file_name


def write_reduce(df):
    file_name = get_gen_file_name('reduce_0.95.csv')
    pd.DataFrame(tt.raise_percent(df, 0.95)).to_csv(file_name, sep=',', header=True, index=False)
    return file_name


def read(file_name):
    path = get_gen_file_name(file_name)
    return pd.read_csv(path)


#获取流通市值
def get_nmc(code):
    df = read_today_all()
    return df[df.code == code].nmc.values[0]


def add_nmc_row(df, index):
    df.insert(index, 'nmc', df.get('code').apply(lambda x: get_nmc(x)))


def do_all():
    exists = os.path.exists(get_root_file_name())
    if not exists:
        write_today_all()
    df = read_today_all()
    new = df[['changepercent', 'trade', 'open', 'high', 'low', 'settlement',
              'volume', 'turnoverratio', 'amount', 'per', 'pb', 'mktcap', 'nmc']].astype(float).round(2)
    df = pd.concat([df[['code', 'name']], new], axis=1)
    __add_row(df, 2)
    write_one_top(df)
    write_normal_top(df)
    write_had_top(df)
    write_raise(df)
    write_one_down(df)
    write_normal_down(df)
    write_had_down(df)
    write_reduce(df)


if __name__ == '__main__':
    do_all()

# print(write_today_all())
#
# print('---------')
#
# print(read_today_all())
