import pandas as pd
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Load your Excel file
# Ensure your Excel has a column exactly named "Name"
df = pd.read_excel('party.xlsx')

@app.route('/')
def index():
    # Convert Excel data to a list of dictionaries for the website
    people = df.to_dict(orient='records')
    return render_template('index.html', people=people)

if __name__ == "__main__":
    app.run()