from flask import render_template, request, jsonify
from app import app, db, utils
from app.models import Website

@app.route('/')
def index():
    websites = Website.query.all()
    return render_template('index.html', websites=websites)

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form['url']
    website = Website.query.filter_by(url=url).first()
    if not website:
        website = Website(url=url)
        db.session.add(website)
    website.last_scan = utils.scan(url)
    db.session.commit()
    return jsonify({'last_scan': website.last_scan.strftime('%Y-%m-%d %H:%M:%S')})
