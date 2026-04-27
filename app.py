from flask import Flask, render_template, request
import requests
import random


app = Flask(__name__)

## URLS can basically be changed to everything you want. Did these one because my layout has trending and new programs. But you can have programs from an category displayed as well.
trending_programs_url = "https://npo.nl/start/api/domain/recommendation-collection?collectionId=trending-anonymous-v0&collectionIndex=1&collectionType=SERIES&includePremiumContent=true&layoutType=RECOMMENDATION&partyId=1%3Amjue2oeb%3A16f959774071426fb880d64700be8000"

new_programs_url = "https://npo.nl/start/api/domain/recommendation-collection?collectionId=recent-free-v0&collectionIndex=4&collectionType=SERIES&includePremiumContent=true&layoutType=RECOMMENDATION&partyId=1%3Amjue2oeb%3A16f959774071426fb880d64700be8000"


@app.route('/')
def index():
    i = 0
    post_data = {"items": {"trending_programs": {"image": [],
                                                 "text_image": [],
                                                 "slug": []},
                           "new_programs": {"image": [],
                                            "text_image": [],
                                            "slug": []}}}

    trending_programs_data = requests.get(trending_programs_url).json()
    new_programs_data = requests.get(new_programs_url).json()

    while i < 2:
        random_trending_program = random.choice(trending_programs_data["items"])

        try:
            post_data["items"]["trending_programs"]["text_image"].append(random_trending_program["images"][1]['url'])
            post_data["items"]["trending_programs"]["slug"].append(random_trending_program["slug"])
            post_data["items"]["trending_programs"]["image"].append(random_trending_program["images"][0]['url'])
        except:
            i = -1

        i += 1
    i = 0

    while i < 3:
        random_new_programs = random.choice(new_programs_data["items"])
        try:
            post_data["items"]["new_programs"]["text_image"].append(random_new_programs["images"][1]['url'])
            post_data["items"]["new_programs"]["slug"].append(random_new_programs["slug"])
            post_data["items"]["new_programs"]["image"].append(random_new_programs["images"][0]['url'])
        except:
            i = -1

        i += 1

    return render_template("index.html", post_data=post_data)


@app.route('/search_results', methods=['POST'])
def search_results():
    if request.method == 'POST':

        search_term = request.form['search-term']

        payload = {"searchQuery": search_term,
                   "searchType": "series",
                   "subscriptionType": "anonymous",
                   "includePremiumContent": "true"}

        search_results_api = requests.get("https://npo.nl/start/api/domain/search-collection-items", params=payload).json()[
            'items'][:16]

        post_data = {"items": {"image_url": [],
                               "title_image": [],
                               "series_slug": []}}


        len_list = len(search_results_api)

        for i in range(len(search_results_api)):
            image_url = None
            image_text_url = None


            for image in search_results_api[i]['images']:
                if image['role'] == "title":
                    image_text_url = image['url']
                    post_data['items']['title_image'].append(image_text_url)

            if not image_text_url:
                len_list -= 1
                continue


            for image in search_results_api[i]['images']:
                if image['role'] == "collection_item":
                    image_url = image['url']
                    post_data['items']['image_url'].append(image_url)

            if not image_url:
                for image in search_results_api[i]['images']:
                    if image['role'] == "default":
                        image_url = image['url']
                        post_data['items']['image_url'].append(image_url)

            post_data['items']['series_slug'].append(search_results_api[i]['slug'])

        print(post_data)
        return render_template("search_results.html", post_data=post_data, len=len_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
