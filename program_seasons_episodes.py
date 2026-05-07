import requests

search_slug = "wie-is-de-mol"

payload = {
    'seriesSlug': search_slug,
    'tab': 'afleveringen'
}


program_data = requests.get(f"https://npo.nl/start/_next/data/x86HHiBzF_QycknSQpn-M/serie/{search_slug}/afleveringen.json", params=payload).json()['pageProps']['dehydratedState']['queries'][3]['state']['data']

for program_seasons in program_data:

    program_season_label = program_seasons['label']
    print(program_season_label)

    program_season_guid = program_seasons['guid']
    print(program_season_guid)

