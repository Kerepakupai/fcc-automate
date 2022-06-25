import pandas as pd
import camelot

def read_table_from_html():
    simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
    table = simpsons[1]
    print(table)


def read_table_from_csv():
    # reading 1 csv file from the website
    df_laliga21 = pd.read_csv('https://football-data.co.uk/mmz4281/2122/SP1.csv')
    df_laliga21.rename(
        columns={'FTHG': 'home_goals', 'FTAG': 'away_goals'}, 
        inplace=True
    )
    print(df_laliga21)


def read_table_from_pdf():
    tables = camelot.read_pdf('foo.pdf', pages='1', flavor='lattice')
    print(tables)

    tables.export('foo.csv', f='csv', compress=True)
    tables[0].to_csv('foo.csv')
    print(tables[0].df)  # to a df


if __name__ == '__main__':
    read_table_from_pdf()
