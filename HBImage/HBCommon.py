import os
import re
import time

from os.path import isfile, join
from functools import wraps




#Decorator : timeit
def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function \"{func.__name__}\" Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper





def load_file_txt(filepath) -> list:
    with open(filepath) as f:
        return f.read().splitlines()

def is_url(string) -> bool:
    url_regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )
    return re.match(url_regex, string) is not None

def get_file_basename(abs_filepath:str) -> str:
    return os.path.basename(abs_filepath)


def get_file_format(filepath:str) -> str:
    basename = os.path.basename(filepath)
    return os.path.splitext(basename)[1][1:]

def get_file_name_and_format(filename:str) -> list:
    file_basename = os.path.basename(filename)
    file_basename_splited = os.path.splitext(file_basename)
    file_name = file_basename_splited[0]
    file_format = file_basename_splited[1][1:]
    return [file_name, file_format]


def update_dict_only_existing_keys(original:dict, input:dict):
    for key, value in input.items():
        if key in original:
            original[key] = value


def limit_number(x, lower, upper):
    return max(lower, min(x, upper))



def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


def list_folder_files(folder_path:str) -> list:
    """Only return the files' relative path, not include folders.

    Args:
        folder_path (str)

    Returns:
        List[str]: a list of files' path.(relative path)
    """
    files = [f for f in os.listdir(folder_path) if isfile(join(folder_path, f))]
    return sorted(files, key=natural_sort_key)



#"natural_sort_key" 
def natural_sort_key(string):
    """\"Write by ChatGPT\"\n
    How to use:\n
    sorted_strings = sorted(strings, key=natural_sort_key)

    """
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string)]







