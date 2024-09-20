import argparse
import re

def _parse_arguments() -> list:
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Returns most count number codes",
        epilog="o:" 
    )
    parser.add_argument("filename", type=str, help="Path to file.")

    return parser.parse_args()

def get_codes(filename: str) -> dict:
    """
    Get codes from the target file.

    Parameters:
    filename (str): name of target file.

    Returns
    dict: dict contains numbers and it count with format code:count
    """
    number_regex = r"(?:(?:\+?[7])|(?:\b[8])) ?(\d{3}) ?\d{3}-?\d{2}-?\d{2}"
    codes = dict()

    with open(filename, "r", encoding="utf-8") as file:
        c = re.compile(number_regex)

        while ( line := file.readline() ):
            if line.startswith("Номер"):
                code = c.search(line).group(1)

                if code in codes: codes[code] += 1
                else: codes[code] = 1
    
    return codes

def get_max_codes(codes: dict) -> filter:
    """
    Filter dict and returns most count codes.

    Parameters:
    codes (dict): Dict of all numbers.

    Returns
    filter: result that contains max codes
    """
    max_code = max(codes.values())
    return filter(lambda key: codes[key] == max_code, codes)

def main():
    args = _parse_arguments()
    
    try:
        codes = get_codes(args.filename)
        max_codes = get_max_codes(codes)
    except FileNotFoundError:
        print("Incorrect object or path to file!")
    except Exception as e:
        print(f"Something wrong ;/ => {e}")
    
    print("Max Codes:")
    for code in max_codes:
        print(code, end=" ")
            

if __name__ == "__main__":
   main()
