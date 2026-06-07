import os
from typing import List

import yaml

languages = {}
languages_present = {}


def get_string(lang: str):
    return languages[lang]


try:
    languages["en"] = yaml.safe_load(
        open("./strings/langs/en.yml", encoding="utf8")
    )

    if not languages["en"]:
        languages["en"] = {}

    languages_present["en"] = languages["en"].get(
        "name",
        "English",
    )

except Exception as e:
    print(f"Error loading en.yml: {e}")
    exit(1)


for filename in os.listdir("./strings/langs/"):
    if not filename.endswith(".yml"):
        continue

    language_name = filename[:-4]

    if language_name == "en":
        continue

    try:
        with open(
            f"./strings/langs/{filename}",
            encoding="utf8",
        ) as file:
            data = yaml.safe_load(file)

        if not data:
            data = {}

        languages[language_name] = data

        for item in languages["en"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["en"][item]

        languages_present[language_name] = (
            languages[language_name].get(
                "name",
                language_name.upper(),
            )
        )

        print(f"Loaded language: {language_name}")

    except Exception as e:
        print(
            f"Language file error in {filename}: {e}"
        )

        languages[language_name] = dict(
            languages["en"]
        )

        languages_present[language_name] = (
            language_name.upper()
        )

print(
    f"Successfully loaded {len(languages)} language files."
)
