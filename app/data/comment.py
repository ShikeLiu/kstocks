import pandas as pd


def get_comment(source_file):
    df = pd.read_csv(source_file)
    return df.get('code', 'comment')


if __name__ == '__main__':
    print(get_comment('/Users/liushike/Documents/mid.csv'))
