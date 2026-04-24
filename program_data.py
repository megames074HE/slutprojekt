import requests

search_slug = "wie-is-de-mol"

payload = {
    'seriesSlug': search_slug,
    'tab': 'afleveringen'
}


program_data = requests.get(f"https://npo.nl/start/_next/data/x86HHiBzF_QycknSQpn-M/serie/{search_slug}/afleveringen.json", params=payload).json()

print(program_data)