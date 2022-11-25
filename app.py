from flask import Flask
from insurance.logger import logging

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    logging.info('Logging module testing.')
    return "Flask Testing"

if __name__ == '__main__':
    app.run(debug=True)