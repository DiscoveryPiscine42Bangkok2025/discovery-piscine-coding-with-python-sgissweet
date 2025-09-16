#!/usr/bin/env python3

def famous_births(h_figure):
    sorted_h_figure = { key: val for key, val in sorted(h_figure.items(), key=lambda item: item[1]["date_of_birth"])}
    for key, val in sorted_h_figure.items():
        name = val["name"]
        date = val["date_of_birth"]
        print(f"{name} is a great scientist born in {date}")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" },
}

famous_births(women_scientists)