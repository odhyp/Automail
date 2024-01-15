from pathlib import Path


def get_root_path():
    """Get project root path
    """
    current_path = Path().absolute()
    root_path = Path(current_path)
    return root_path


def get_data_path():
    """Get data path
    """
    root_path = get_root_path()
    data_path = Path(root_path, 'data')
    return data_path


def get_input_path(file_name: str):
    """Get input file path. Current input directory is in data
    """
    data_path = get_data_path()
    input_path = Path(data_path, file_name)
    return input_path
