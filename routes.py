from flask import Flask, render_template
app = Flask(__name__)

# You'll need to install PyJWT via pip 'pip install PyJWT' or your project packages file

import jwt
import time

METABASE_SITE_URL = "https://partner-cube.metabaseapp.com"
METABASE_SECRET_KEY = "abae64173082e1daac3d0eddf13de9c269d3d829deb9e32503309e75d0c92ea8"



# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    payload = {
        "resource": {"dashboard": 1},
        "params": {
        },
        "exp": round(time.time()) + (60 * 10) # 10 minute expiration
    }
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

    iframe_url = METABASE_SITE_URL + "/embed/dashboard/" + token + "#bordered=true&titled=true"
    return render_template('index.html', iframe_url=iframe_url)

if __name__ == '__main__':
    app.run(debug=True)
