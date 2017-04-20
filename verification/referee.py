from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee

from tests import TESTS

cover = """def cover(func, data):
    return list(func(data))
"""

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cover_code={
            'python-27': cover,
            'python-3': cover
        },
        function_name={
            "python": "checkio",
            "js": "nonUniqueElements"
        }
    ).on_ready)
