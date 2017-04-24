from app import app
from flask import redirect, render_template, request, url_for
import csv

# Import previous fish
nibbles = []
with open('./app/data/fish.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        nibbles += row


@app.route('/')
@app.route('/release')
def release():
    return render_template('released.html',
                           nibbles=nibbles)


@app.route('/catch')
@app.route('/catch/')
@app.route('/catch/<path:path>')
@app.route('/catch<path:path>')
def catch(path=''):
    start = request.url.find('/', 9)
    fish = request.url[start + 6:]
    nibbles.append(fish)
    # Save current fish
    with open('./app/data/fish.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([fish])
    return redirect(url_for('release'))


if __name__ == '__main__':
    app.run()
