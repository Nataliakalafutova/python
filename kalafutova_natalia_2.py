import json
movies = []

# Otevření souboru pro čtení
with open("netflix_titles.tsv", encoding="utf-8") as file:
    for line in file:
        # Rozdělení na dvě položky v seznamu
        line = line.strip().split('\t')
        movies.append(line)
        movies = sorted(movies)
print(movies)

PRIMARYTITLE = line[2]
DIRECTOR = line[15]
CAST = line[16]
GENRES = line[8]
STARTYEAR = line[5]


movie_info = {
            'title': PRIMARYTITLE,
            'directors': DIRECTOR,
            'cast': CAST,
            'genres': GENRES,
            'decade': STARTYEAR
        }

movies.append(movie_info)

with open('movies.json', mode='w', encoding='utf-8') as json_file:
    json.dump(movies, json_file, ensure_ascii=False, indent=4)

print("Data boli prevedene do 'movies.json'.")