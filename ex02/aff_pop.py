from matplotlib.pyplot import figure, plot, yticks, title, xlabel, ylabel
from matplotlib.pyplot import legend, show, tight_layout
from pandas import DataFrame
from load_csv import load


def convert_to_int(value):
    """ Convert a string with a suffix like 'M' (million) or 'K' (thousand) \
    to an integer. """
    if not value:
        return 0
    if isinstance(value, int):
        return value

    value = value.strip().upper()
    if value.endswith('M'):
        return int(float(value[:-1]) * 1_000_000)
    elif value.endswith('K'):
        return int(float(value[:-1]) * 1_000)
    elif value.endswith('B'):
        return int(float(value[:-1]) * 1_000_000_000)
    else:
        return int(value)


def get_line(df: DataFrame, keyword: str):

    try:
        assert isinstance(df, DataFrame), "Error"
        """ Search for a keyword in the entire DataFrame """
        nlist = df.iloc[0].tolist()
        ret = []

        for item in nlist:
            ret.append(str(item).strip())

        data = df[df.map(lambda x: keyword.lower() in
                         str(x).lower()).any(axis=1)]

        width, height = data.shape

        vlist = []
        klist = []

        row_data = data.iloc[0]

        keys = row_data.index
        klist = keys.tolist()

        for y in range(height):
            for x in range(width):
                vlist.append(data.iloc[x].iloc[y])

        x = klist
        y = vlist

        nklist = []
        klist = klist[1:len(klist)]
        for k in klist:
            nklist.append(int(k))

        nvlist = []
        vlist = vlist[1:len(vlist)]
        for v in vlist:
            nvlist.append(convert_to_int(v))

        return (nklist, nvlist)

    except AssertionError as e:
        print(f"An unexpected error occurred: {e}")


def display_graph(x1: list, y1: list, x2: list, y2: list,
                  kword1: str, kword2: str) -> None:
    figure(figsize=(8, 5))
    plot(x1, y1, label=kword1)
    plot(x2, y2, label=kword2)
    title('Population Total')
    xlabel('Year')
    ylabel('Population')

    yticks([20000000, 40000000, 60000000], ['20M', '40M', '60M'])
    legend(loc='lower right')
    tight_layout()
    show()


def main():

    try:
        x1, y1 = get_line(load("src/population_total.csv"), "France")
        x2, y2 = get_line(load("src/population_total.csv"), "Belgium")
        display_graph(x1, y1, x2, y2, "France", "Belgium")
        x2, y2 = get_line(load("src/wrong_file.csv"), "France")
        display_graph(x1, y1, x2, y2, "France", "Belgium")
    except TypeError as e:
        print(f"TypeError: {e}")


if __name__ == "__main__":
    main()
