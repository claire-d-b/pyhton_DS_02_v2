from pandas import DataFrame, set_option
import torch
from torch.utils.data import Dataset


def display(df: DataFrame, num_rows: int, num_cols: int) -> None:
    try:
        isinstance(df, DataFrame)
        size = (num_rows, num_cols)

        df_truncated = df.truncate(before=0, after=1)

        print("Loading dataset of dimensions ", size)

        # Print the truncated DataFrame without indices and headers and show specific columns
        print(df_truncated.to_string(index=False, header=False,
                columns=[0,1,2,3,4,5,num_cols-6, num_cols-5,num_cols-4,num_cols-3,num_cols-2,num_cols-1], max_cols=11))

    except Exception as e:
        raise AssertionError(f"Error: {e}")


def load(path: str) -> Dataset:
    """Function that opens a file and display inner data in the shape of a datatable"""
    num_rows, num_cols = 0, 0
    try:
        # Ici open est un gestionnaire de contexte qui retourne un object-fichier
        with open(path, 'r') as file:
            nlist = []
            # What is a BOM? The Byte Order Mark is a sequence of bytes at the beginning of a text file
            # that signals the encoding used for the file.
            # Purpose: The BOM helps systems distinguish between different encodings.
            # In UTF-8, it’s not required, but some editors (especially on Windows) may include it by default.
            # Practical Consideration: When processing files in Python (or other programming languages),
            # you might encounter \ufeff at the start of your text, so it's important to be aware of it
            # and remove it when necessary.
            nlist.append(file.readline().strip().lstrip('\ufeff').split(','))
            # readline: returns next line from the object file
            # strip: removes spaces at the beginning and end
            # lstrip: '\ufeff' is a special character used in text files to indicate the encoding,
            # by default remove spaces from the left, is specified remove specified characters
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
