from uuid import uuid4

import requests

from module import Fwibble


def random() -> str:
    return str(uuid4())


def random2() -> str:
    return Fwibble().random()


def cat_fact() -> str:
    response = requests.get("https://catfact.ninja/fact")
    return response.json()["fact"]
