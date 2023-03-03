import requests
import json

def get_heroes_list(needed_heroes):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url=url)
    heroes = response.json()
    stats_dict = {}
    int_points = []
    for pers in heroes:
        if pers['name'] in needed_heroes:
            int_points.append(pers['powerstats']['intelligence'])
            if pers['powerstats']['intelligence'] not in stats_dict:
                stats_dict.setdefault(pers['powerstats']['intelligence'], [pers['name']])
            else:
                stats_dict[pers['powerstats']['intelligence']].append(pers['name'])

    smart_hero = ','.join(stats_dict[max(int_points)])
    return print(f'Самый умный герой {smart_hero}, его интеллект {max(int_points)}')


if __name__ == "__main__":
    get_heroes_list(['Hulk', 'Captain America', 'Thanos'])
