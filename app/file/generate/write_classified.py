import os

import pandas as pd
import tushare as ts

import app.file.write_file_os as wfo


def mk_classified_path():
    path = wfo.get_basic_path() + "classified/"
    exists = os.path.exists(path)
    if exists:
        return path
    else:
        os.makedirs(path)
        return path


def __get_path(name):
    return mk_classified_path() + name


def get_industry_classified_path():
    return __get_path('industry_classified.csv')


def get_concept_classified_path():
    return __get_path('concept_classified.csv')


def get_area_classified_path():
    return __get_path('area_classified.csv')


def write_industry_classified():
    df = ts.get_industry_classified()
    path = get_industry_classified_path()
    df.to_csv(path, index=False)


def write_concept_classified():
    df = ts.get_concept_classified()
    path = get_concept_classified_path()
    df.to_csv(path, index=False)


def write_area_classified():
    df = ts.get_area_classified()
    path = get_area_classified_path()
    df.to_csv(path, index=False)


def get_industry_classified(code):
    df = pd.read_csv(get_industry_classified_path())
    return df[df.code == code].c_name.values


def get_concept_classified(code):
    df = pd.read_csv(get_concept_classified_path())
    return df[df.code == code].c_name.values


def get_area_classified(code):
    df = pd.read_csv(get_area_classified_path())
    return df[df.code == code].area.values


def add_industry_row(df, index):
    df.insert(index, 'industry', df.get('code').apply(lambda x: get_industry_classified(x)))


def add_concept_row(df, index):
    df.insert(index, 'concept', df.get('code').apply(lambda x: get_concept_classified(x)))


def add_area_row(df, index):
    df.insert(index, 'area', df.get('code').apply(lambda x: get_area_classified(x)))


def add_classified_all_row(df, from_index):
    add_area_row(df, from_index)
    add_concept_row(df, from_index)
    add_industry_row(df, from_index)


def update():
    mk_classified_path()
    write_industry_classified()
    write_concept_classified()
    write_area_classified()


# update()
