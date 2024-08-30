
'''
simple webhook reciever that responds to POST requests
used as an OpenSearch/Elasticsearch alerting endpoint
runs on http://127.0.0.1:5000
better to run from terminal and not IDE
'''
from flask import Flask,request,json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method=='GET':
        return('<form action="/test" method="post"><input type="submit" value="Send" /></form>')

    elif request.method=='POST':
        return "OK this is a post method"
    else:
        return("ok")

if __name__ == '__main__':
    app.run(debug=True)        