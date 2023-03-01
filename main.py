import requests
import json

def get_heroes_list(needed_heroes):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url=url)
    heroes = response.json()
    stats_dict = {}
    int_points = []
    for row in heroes:
        if row['name'] in needed_heroes:
            int_points.append(row['powerstats']['intelligence'])
            if row['powerstats']['intelligence'] not in stats_dict:
                stats_dict.setdefault(row['powerstats']['intelligence'], [row['name']])
            else:
                stats_dict[row['powerstats']['intelligence']].append(row['name'])

    smart_hero = ''.join(stats_dict[max(int_points)])
    return print(f'Самый умный герой с интелектом {max(int_points)} - {smart_hero}')


if __name__ == "__main__":
    get_heroes_list(['Hulk', 'Captain America', 'Thanos'])