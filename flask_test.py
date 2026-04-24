from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():

    payload = {"searchQuery": "de mol",
                "searchType": "series",
                "subscriptionType": "anonymous",
                "includePremiumContent": "true"}

    search_results_api = requests.get("https://npo.nl/start/api/domain/search-collection-items", params=payload).json()['items'][:10]


    post_data = {"items": {"image_url": [],
                        "title": [],
                        "series_slug": []}
                        }



    for i in range(len(search_results_api)):
        image_url = None

        post_data['items']['title'].append(search_results_api[i]['title'])
        post_data['items']['series_slug'].append(search_results_api[i]['slug'])

        for image in search_results_api[i]['images']:
            if image['role'] == "collection_item":
                image_url = image['url']
                post_data['items']['image_url'].append(image_url)
                
        if not image_url:
            for image in search_results_api[i]['images']:
                if image['role'] == "default":
                    image_url = image['url']
                    post_data['items']['image_url'].append(image_url)


    return render_template("index.html", len=len(search_results_api), npo_data=post_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)