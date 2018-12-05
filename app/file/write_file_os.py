import datetime as dt
import os


def make_dir_today(name=''):
    file_path = get_path_name() + name
    exists = os.path.exists(file_path)
    if exists:
        return file_path
    else:
        os.makedirs(file_path)
        return file_path


def get_path_name():
    return '/Users/liushike/kstocks/data/' + dt.datetime.now().strftime("%Y-%m-%d") + '/'


def get_basic_path():
    return '/Users/liushike/kstocks/data/basic/'


def get_day_path(code):
    path = '/Users/liushike/kstocks/data/codes/' + code
    exists = os.path.exists(path)
    if not exists:
        os.makedirs(path)
    return path


def mk_basic_path():
    path = get_basic_path()
    exists = os.path.exists(path)
    if exists:
        return path
    else:
        os.makedirs(path)
        return path
