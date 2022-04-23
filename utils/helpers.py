from utils.consts import CITY_FILE_PATH, APP_DESC_PATH
import os


def read_file() -> str:
    path = os.path.join(os.getcwd(), CITY_FILE_PATH)
    with open(path, 'r') as f:
        return f.read()


def write_to_file(value: str) -> None:
    path = os.path.join(os.getcwd(), CITY_FILE_PATH)
    with open(path, 'w') as f:
        f.write(value)


def read_app_description() -> None:
    path = os.path.join(os.getcwd(), APP_DESC_PATH)
    with open(path, 'r') as f:
        return f.read()


def temp_from_kelvin_to_celcius(temp: str) -> str:
    temp_k = float(temp)
    temp_c = round(temp_k - 273.15, 2)
    return str(temp_c)


def convert_wind_speed(wind_speed: float) -> float:
    return round(wind_speed/1000*3600, 2)
