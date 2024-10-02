from matplotlib.pyplot import legend, show, tight_layout, subplots
from pandas import DataFrame
from load_csv import load


def get_values(df: DataFrame, keyword: str):

    try:
        assert isinstance(df, DataFrame), "Error"
        """ Search for a keyword in the entire DataFrame """
        nlist = df.iloc[0].tolist()
        ret = []
        for item in nlist:
            ret.append(str(item).strip())

        vlist = []

        row_data = df[keyword]

        data = row_data

        for d in data:
            vlist.append(d)

        return (vlist)
    except AssertionError as e:
        print(f"An unexpected error occurred: {e}")


def display_points(frame_x: DataFrame, frame_y: DataFrame) -> None:

    list_x = get_values(frame_x, '1900')
    list_y = get_values(frame_y, '1900')

    """ Custom positions and labels for the x-axis """
    x_positions = [300, 1000, 10000]
    x_labels = ['300', '1k', '10k']

    fig, ax = subplots()
    ax.scatter(list_y, list_x)

    """ Set the x-axis to logarithmic scale """
    ax.set_xscale('log')

    """ Set custom ticks and labels for the x-axis """
    ax.set_xticks(x_positions)
    ax.set_xticklabels(x_labels)

    """ Customize the plot """
    ax.set_title("1900")
    ax.set_xlabel("Gross Domestic product")
    ax.set_ylabel("Life Expectancy")

    """ Display the plot """
    legend()
    tight_layout()
    show()


def main():
    try:
        frame_x = load("src/life_expectancy_years.csv")
        frame_y = load("src/\
        income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        display_points(frame_x, frame_y)
        frame_y = load("\
        income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        display_points(frame_x, frame_y)
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")


if __name__ == "__main__":
    main()
