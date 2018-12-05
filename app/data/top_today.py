import pandas as pd


def st(df):
    return (df.name.str.contains('ST')) & (not_0(df))


# st
def st_is_top(df):
    top = (df.settlement + (df.settlement * 0.05).round(2)).round(2)
    return (top == df.trade) & (st(df))


def st_is_one_top(df):
    return st_is_top(df) & one(df)


def st_is_not_one_top(df):
    return st_is_top(df) & not_one(df)


def st_had_top(df):
    top = (df.settlement + (df.settlement * 0.05).round(2)).round(2)
    return (top == df.high) & (top != df.trade) & (st(df))


# 跌停
def st_is_down(df):
    down = (df.settlement - (df.settlement * 0.05).round(2)).round(2)
    return (down == df.trade) & (st(df))


def st_is_one_down(df):
    return st_is_down(df) & one(df)


def st_is_not_one_down(df):
    return st_is_down(df) & not_one(df)


def st_had_down(df):
    down = (df.settlement - (df.settlement * 0.05).round(2)).round(2)
    return (down == df.low) & (down != df.trade) & (st(df))


# normal
# 涨停
def normal_is_top(df):
    top = (df.settlement + (df.settlement * 0.1).round(2)).round(2)
    return (top == df.trade) & (not_0(df))


# 一字
def normal_is_one_top(df):
    return normal_is_top(df) & one(df)


# 自然
def normal_not_one_top(df):
    return normal_is_top(df) & not_one(df)


# 触及涨停，烂板
def normal_had_top(df):
    top = (df.settlement + (df.settlement * 0.1).round(2)).round(2)
    return (top == df.high) & (top != df.trade) & (not_0(df))


# 跌停
def normal_is_down(df):
    down = (df.settlement - (df.settlement * 0.1).round(2)).round(2)
    return (down == df.trade) & (not_0(df))


def normal_is_one_down(df):
    return normal_is_down(df) & one(df)


def normal_not_one_down(df):
    return normal_is_down(df) & not_one(df)


def normal_had_down(df):
    down = (df.settlement - (df.settlement * 0.1).round(2)).round(2)
    return (down == df.low) & (down != df.trade) & (not_0(df))


# 判断
def one(df):
    return df.high == df.low


def not_one(df):
    return df.low != df.high


def not_0(df):
    return df.settlement != 0


# all return df
# 涨停
def is_top(df):
    return df[normal_is_top(df) | st_is_top(df)]


# 一字
def is_one_top(df):
    return df[normal_is_one_top(df) | st_is_one_top(df)]


# 换手
def not_one_top(df):
    return df[normal_not_one_top(df) | st_is_not_one_top(df)]


# 炸板
def had_top(df):
    return df[normal_had_top(df) | st_had_top(df)]


# 上涨百分比
def raise_percent(df, percent):
    return df[df.changepercent >= percent]


# 跌停
def is_down(df):
    return df[normal_is_down(df) | st_is_down(df)]


def is_one_down(df):
    return df[normal_is_one_down(df) | st_is_not_one_down(df)]


def not_one_down(df):
    return df[normal_not_one_down(df) | st_is_not_one_down(df)]


def had_down(df):
    return df[normal_had_down(df) | st_had_down(df)]


def reduce_percent(df, percent):
    return df[df.changepercent <= percent]


def separate_type(df):
    one_word_up = df[is_one_top(df)]
    one_word_down = df[is_one_down(df)]
    stop = df[df.changepercent == 0 & one(df)]
    top_up = df[not_one_top(df)]
    top_down = df[not_one_down(df)]
    top_ed = df[had_top(df) & not_one(df)]
    down_ed = df[had_down(df) & not_one(df)]
    data = {"one_word_up": one_word_up, "one_word_down": one_word_down, "stop": stop, "top_up": top_up,
            "top_down": top_down, "top_ed": top_ed, "down_ed": down_ed}
    return pd.Panel(data)

# df = ts.get_today_all()
# pd = separate_type(df)
# print(pd)
