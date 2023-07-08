import re


def main(input_string):
    p = r"\(\s*opt\s+array\(\s*((?:\w+\s*\.\s*)*\w+)\s*\)\s*\|\>\s*(\w+)\s*\)"
    matches = re.findall(p, input_string)
    result = [
        (
            option,
            [v.replace(" ", "").replace("\n", "") for v in values.split(".")]
        ) for values, option in matches
    ]
    return result
