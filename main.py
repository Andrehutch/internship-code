#run command
#gcloud app deploy --project=powerful-bounty-401013 --version 1

import os
from flask import Flask, request, render_template
from google.cloud import firestore

app = Flask(__name__)

# Initialize Firestore client
db = firestore.Client()

# Create a business cards collection
business_cards = db.collection('business_cards')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Add the business card to the collection
        business_cards.add({'name': name, 'email': email})

    # Retrieve and display all business cards
    cards = business_cards.stream()
    return render_template('index.html', cards=cards)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
