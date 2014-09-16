from flask import Flask, render_template

import random

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def homepage():
    full_wordlist = []
    # make this configurable
    with open('words_en.csv','r') as f:
        for line in f:
            full_wordlist.append(line)

    # return a random subset of 24 words
    wordlist = random.sample(full_wordlist, 24)
    return render_template('index.html', wordlist = wordlist)


@app.route('/goodbye', methods=['GET'])
def quit():
    return render_template('goodbye.html')

if __name__ == "__main__":
    app.run(debug=True)