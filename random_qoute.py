import requests
import json



def random_qoute() -> str:
    """gets a random qoute"""
    res = requests.get("https://type.fit/api/quotes")
    res = json.loads(res.text)
    return res


def write_in_txt(output_filename: str = "qoutes") -> None:
    res = random_qoute()
    with open(f"{output_filename}.txt", "a") as f:
        for index, q in enumerate(res):
            f.write(f'{res[index]["text"]}\n')
