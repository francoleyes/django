import requests

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

    @classmethod
    def is_hot_in_pehuajo(cls):
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}&units=metric"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            temperature = data["main"]["temp"]
            return temperature
        except requests.exceptions.RequestException:
            return False

def validate_discount_code(discount_code, available_discount_codes):
    for available_code in available_discount_codes:
        difference = len(set(discount_code).symmetric_difference(available_code.code))
        if difference < 3:
            return available_code

    return False