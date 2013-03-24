import os
from flask import Flask
from flask import request
from flask import render_template
import json
from jsonstore.store import EntryManager
import datetime

em = EntryManager('index.db')


app = Flask(__name__)

@app.route("/")
def hello():
    r = request.values.to_dict()
    #jstime = datetime.datetime.fromtimestamp(int(r["rt.end"])/1000).isoformat()
    #r.update({"jstime": jstime})
    rj = json.dumps(r)
    em.create(r)
    data = em.search()
    return "okay"

@app.route("/chart")
def chart():
    data = em.search()
    return render_template('chart.html',data = data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
