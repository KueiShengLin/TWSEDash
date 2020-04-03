from flask import Flask
from plot import dash_generate

server = Flask(__name__)
dash = dash_generate(server)

@server.route("/dash")
def dash_app():
    return  dash
    
if __name__ == "__main__":
    server.run(host="127.0.0.1", port="8050", debug=True)