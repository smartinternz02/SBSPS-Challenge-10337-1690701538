from flask import Flask, render_template, request, session
import requests

app = Flask(__name__)

@app.route('/')
def search():
    url = "https://api.openchargemap.io/v3/referencedata"
    querystring = {"key":"123"}

    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers, params=querystring)

    data=response.json()
    return data



if __name__ == '__main__':
    app.run(debug=True)
