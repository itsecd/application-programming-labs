import argparse

from dataframe import init_df, filter_df, show_s_dist

def _parse_arguments() -> list:
    """
    Function for get arguments from cli.
    Returns:
    list: List of arguments.
    """
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Programm gets path to csv file and output some stats information.",
        epilog="o:" 
    )
    parser.add_argument("csv", type=str, help="Path to csv")

    return parser.parse_args()

def main():
    args = _parse_arguments()

    try:
        df = init_df(args.csv)
    except FileNotFoundError:
        print("Invalid path to file.")
        exit()
    except Exception as e:
        print(f"Some error: {e}")
        print("Please, check path to file or its internals.")
        exit()
        

    print(
        "DataFrame:\n",    
        df,
        "\n"
    )

    print(
        "Statistic information for H, W, CH:\n",
        df.loc[:, ("H", "W", "CH")].describe(),
        "\n"    
    )


    max_height = 800
    max_width = 1000
    print(
        f"Filter Function demonstration (for {max_height=}, {max_width=}):\n",
        filter_df(df, max_height, max_width),
        "\n"
    )

    print(
        "Sorting datafram by S column:\n",
        df.sort_values(by="S"),
        "\n"
    )

    show_s_dist(df)


if __name__ == "__main__":
    main()