from pandas import DataFrame, read_csv, set_option
from matplotlib.pyplot import figure, plot, subplots, title, xlabel, ylabel, legend, savefig, show, tight_layout, scatter
import torch
from torch.utils.data import Dataset

def display(df: DataFrame, num_rows: int, num_cols: int) -> None:
    try:
        isinstance(df, DataFrame)
        # Search for a keyword in the entire DataFrame
        keyword = "France"
        # Position-Based Selection: Unlike .loc, which is label-based, .iloc strictly uses
        # integer positions (starting from 0) to access data.
        # Syntax = df.iloc[row_selection, column_selection]
        # displays the first line
        # nlist = list(df)

        ret = []

        first_line = df.iloc[0]
        print("first line", first_line)

        # for item in nlist:
        #    ret.append(str(item).strip())
        # print("RET", ret)
        # lambda function sets all char to lowercase do we talk about case-insensititvity
        # then it searches for the keyword in all lowercase words
        # axis=1 means "row-wise"
        # Finally, df[...] filters the rows where the condition is True.
        # In other words, it selects the rows where the keyword was found in at least one of the columns.
        data_row = df[df.map(lambda x: keyword.lower() in
                         str(x).lower()).any(axis=1)]

        data_col = df[df.map(lambda x: keyword.lower() in
                         str(x).lower()).any(axis=0)]

        vlist = []
        klist = []

        rows = data_row.values
        cols = data_col.values

        flat_rows = [item for sublist in rows for item in sublist][1:-1]
        flat_cols = [item for sublist in cols for item in sublist][1:-1]
        # flat_example= []
        # for sublist in rows:
        #     for item in sublist:
        #         flat_example.append(item)
        # flat_res = flat_example[1:-1]

        for i, row in enumerate(flat_rows):
            if i != len(flat_rows):
                vlist.insert(i, float(row))
        for i, col in enumerate(flat_cols):
            if i != len(flat_cols):
                klist.insert(i, float(col))

        figure(figsize=(8, 5))
        plot(klist, vlist)
        title('Life Expectancy Years')
        tight_layout()
        savefig('output', dpi=100)

    except AssertionError as e:
        print(f"An unexpected error occurred: {e}")



def load(path: str) -> Dataset:
    """Function that opens a file and display inner data in the shape of a datatable"""
    num_rows, num_cols = 0, 0
    try:
        # Ici open est un gestionnaire de contexte qui retourne un object-fichier
        with open(path, 'r') as file:
            nlist = []
            # Purpose: The BOM helps systems distinguish between different encodings.
            # In UTF-8, it’s not required, but some editors (especially on Windows) may include it by default.
            # Practical Consideration: When processing files in Python (or other programming languages),
            # you might encounter \ufeff at the start of your text, so it's important to be aware of it
            # and remove it when necessary.
            nlist.append(file.readline().strip().lstrip('\ufeff').split(','))
            # readline: returns next line from the object file
            # strip: removes spaces at the beginning and end
            # lstrip: '\ufeff' is a special character used in text files to indicate the encoding.
            # split: generates the list
            j = len(nlist[0])
            i = 0
            for line in file:
                nlist.append(line.strip().split(','))
                i += 1

            df = DataFrame(nlist)

            num_rows = i
            num_cols = j

            ret = display(df, num_rows, num_cols)
            
    except Exception as e:
        raise AssertionError(f"Error: {e}")

    return ret

