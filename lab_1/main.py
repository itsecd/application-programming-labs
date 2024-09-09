import argparse
import re

number_regex = r"(?:(?:\+?[7])|(?:\b[8])) ?(\d{3}) ?\d{3}-?\d{2}-?\d{2}"

def _parse_arguments() -> list:
     parser = argparse.ArgumentParser(
        prog="main.py",
        description="Returns most count number codes",
        epilog="o:" 
    )
    parser.add_argument("filename", type=str, help="Path to file.")
    
    return parser.parse_args()

def get_codes(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        c = re.compile(number_regex)

        while ( line := file.readline() ):
            if line.startswith("Номер"):
                yield c.search(line).group(1)
                
def get_common_codes():


def get_common_codes(filename: str):
    """
    Open and read target file. Find strings starts with number phone field and uses regexp to find phone codes.

    Patameters:
    filename (str): path to target file.

    Returns:
    Generator[int]
    """
    matches = dict()

    with open(filename, "r", encoding="utf-8") as file:
        c = re.compile(number_regex)

        while ( line := file.readline() ):
            if line.startswith("Номер"):
                code = c.search(line).group(1)

                if code in matches: matches[code] += 1
                else: matches[code] = 1

    max_match = max(matches.values())

    for code, match in matches.items():
        if match == max_match: yield code


def main():
    args = _parse_arguments()
    
    try:
        print("Codes:", end=" ")
        for code in get_common_codes(args.filename): print(code, end=" ")
    except FileNotFoundError:
        print("Incorrect object or path to file!")
    except Exception as e:
        print("Something wrong ;/ => {e.text}")
        

if __name__ == "__main__":
   main()

   
