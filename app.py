import os

from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():

    return """

<center> 

    <img src="https://te.legra.ph/file/9a365462d71dbb0042c6e.jpg" style="border-radius: 12px;"/> 

</center> 

<style>

    body { 

        background: antiquewhite;

    }

</style>"""

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8080))

    app.run(host='0.0.0.0', port=port)
