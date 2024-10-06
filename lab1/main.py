import argparse
import re



def read_file(file: str) -> list[str]:
    """
    get data from the file.
    
    Parameters:
    file: str - name of file.

    Returns:
    All data from file in list[str]
    """
    try:
        text_stream = open(file, 'r', encoding="UTF-8")
        data = text_stream.readlines()
        text_stream.close()
        return data

    except:
        print("Error open file")


def arg_parcer() -> str:
    """
    File name parcer.
    
    Returns:
    name of file (from command line) in str
    """
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('file_name', type=str,
                            help='file for work')
        args = parser.parse_args()
        return args.file_name
    except:
        print("Error parse arg")


def processing_file(data: list(str)) -> str:
    """
    Processing of file:
    
    data: list(str) - info from read file

    Returns:
    The most popular name from file in str
    """
    try:
        text_pattern = r'Имя: '
        all_names = []
        names = []

        for i in range(0, len(data)):
            if re.search(text_pattern, data[i]):
                name = re.split(text_pattern, data[i])
                name = re.split(r'\n', name[1])
                all_names.append(name[0])

        for i in range(0, len(all_names)):
            if all_names[i] not in names:
                names.append(all_names[i])

        max_count = -1
        popular_name = -1

        for i in range(0, len(names)):
            count = 0
            for j in range(0, len(all_names)):
                if re.fullmatch(names[i], all_names[j]):
                    count += 1
            if count > max_count:
                max_count = count
                popular_name = i

        return names[popular_name]
    except:
        print('Error of processing file')


def main():
    file_name = arg_parcer()
    data = read_file(file_name)
    answer = processing_file(data)
    print("The most popular name:", answer) #ответ: Светлана


if __name__ == "__main__":
    main()
