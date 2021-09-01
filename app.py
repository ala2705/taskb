from urllib import request
import string
from flask import Flask
from random import choices
from hashids import Hashids
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'this should be a secret random string'
# hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])

#browser by default is get request

from flask import request

from models import Link
@app.route('/show_urls',methods=['GET'])
def showUrls():
    link = Link()
    return link.showUrls()
@app.route('/show_urls_Json',methods=['GET'])
def showUrlsJson():
    link = Link()
    return link.showUrlsJson()

@app.route('/full_url',methods=['GET'])
def check_full_url():
    short_url = request.args.get("url")
    link = Link()
    original_url = link.CheckExsistUrl(short_url)
    return original_url

########################


@app.route('/short_url',methods=['POST'])
def short_url():

    original_url = request.form.get('original_url')

    # characters = string.digits + string.ascii_letters
    # # short_url = ''.join(choices(characters, k=8))
    # short_url = ''.join(choices(characters, k=8))
    # print(characters)
    link = Link()
    short_url = link.ShortenUrl(original_url)

    return short_url




@app.route('/',methods=['GET', 'POST'])
def hello_world():
    # link = Link()
    # url = 'www.facebook.com'
    # link.ShortenUrl(url)
    # print('finished adding')
    # link.showUrls()
    # print(link.CheckExsistUrl('qZVq'))

    return 'Hello World!'

@app.route('/get',methods=['GET'])
def get_hello_world():
    return 'Get Hello World!'



if __name__ == '__main__':
    app.run()
