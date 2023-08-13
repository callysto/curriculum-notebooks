def get_pokemon_data():
    import requests
    import pandas as pd
    r = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000')
    df = pd.DataFrame(r.json()['results'])

    abilities = []
    base_experience = []
    forms = []
    #game_indices = []
    height = []
    held_items = []
    id = []
    is_default = []
    location_area_encounters = []
    moves = []
    #name = []
    order = []
    species = []
    sprites = []
    stats = []
    types = []
    weight = []
    for i in range(len(df)):
        print(df['name'][i])
        try:
            r = requests.get(df['url'][i])
            abilities.append(r.json()['abilities'])
            base_experience.append(r.json()['base_experience'])
            forms.append(r.json()['forms'])
            #game_indices.append(r.json()['game_indices'])
            height.append(r.json()['height'])
            held_items.append(r.json()['held_items'])
            id.append(r.json()['id'])
            is_default.append(r.json()['is_default'])
            location_area_encounters.append(r.json()['location_area_encounters'])
            moves.append(r.json()['moves'])
            #name.append(r.json()['name'])
            order.append(r.json()['order'])
            species.append(r.json()['species'])
            sprites.append(r.json()['sprites'])
            stats.append(r.json()['stats'])
            types.append(r.json()['types'])
            weight.append(r.json()['weight'])
        except:
            abilities.append(None)
            base_experience.append(None)
            forms.append(None)
            #game_indices.append(None)
            height.append(None)
            held_items.append(None)
            id.append(None)
            is_default.append(None)
            location_area_encounters.append(None)
            moves.append(None)
            #name.append(None)
            order.append(None)
            species.append(None)
            sprites.append(None)
            stats.append(None)
            types.append(None)
            weight.append(None)
    df['id'] = id
    df['height'] = height
    df['weight'] = weight
    df['base_experience'] = base_experience
    df['abilities'] = abilities
    df['forms'] = forms
    df['species'] = species
    df['is_default'] = is_default
    #df['game_indices'] = game_indices
    #df['held_items'] = held_items
    df['location_area_encounters'] = location_area_encounters
    #df['moves'] = moves
    #df['name'] = name
    df['order'] = order
    #df['sprites'] = sprites
    df['stats'] = stats
    df['types'] = types
    df = df.drop('url', axis=1) # drop url column

    # split the stats column into multiple columns
    df_stats = pd.DataFrame(df['stats'].tolist())
    df_stats.columns = ['hp','attack','defense','special-attack','special-defense','speed']
    for column in df_stats.columns:
        df_stats[column] = df_stats[column].apply(lambda x: x['base_stat'] if x is not None else None)
    # join with the main dataframe
    df = df.join(df_stats)
    df = df.drop('stats', axis=1)
    df = df.drop('location_area_encounters', axis=1)

    # split the abilities to three columns
    abilities_lists = [[],[],[]]
    for i in range(len(df)):
        for n in range(3):
            try:
                ability = df['abilities'][i][n]['ability']['name']
            except:
                ability = None
            abilities_lists[n].append(ability)
    df['ability1'] = abilities_lists[0]
    df['ability2'] = abilities_lists[1]
    df['ability3'] = abilities_lists[2]
    df = df.drop('abilities', axis=1)

    # species column is a dictionary, so we need to extract the name
    df['species'] = df['species'].apply(lambda x: x['name'] if x is not None else None)

    # convert the forms column to a string
    df['forms'] = df['forms'].apply(lambda x: x[0]['name'] if x is not None else None)

    # split the types to two columns
    types_lists = [[],[]]
    for i in range(len(df)):
        for n in range(2):
            try:
                type = df['types'][i][n]['type']['name']
            except:
                type = None
            types_lists[n].append(type)
    df['type1'] = types_lists[0]
    df['type2'] = types_lists[1]
    df = df.drop('types', axis=1)

    # convert the moves column to a stringified list
    #df['moves'] = df['moves'].apply(lambda x: [move['move']['name'] for move in x] if x is not None else None)

    # reorder the columns
    df = df[['id','name','base_experience','height','weight','speed','hp','attack','defense','special-attack','special-defense','forms','species','is_default','order','type1','type2','ability1','ability2','ability3']]

    # write the dataframe to a csv file
    df.to_csv('pokemon.csv', index=False)

    # return the dataframe
    return df