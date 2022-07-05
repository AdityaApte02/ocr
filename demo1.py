from flask import Flask as fl
from flask import render_template,url_for
from PIL import Image
from flask import request,redirect
from werkzeug.utils import secure_filename
import logging
import cv2
import pytesseract
import numpy
import base64
from text2image_tess import *

app=fl(__name__)

@app.route('/hello/')
def hello_world():
    return "<h1>Hello</h1>"


@app.route('/')
def home():
    return render_template('index.html', title="Home")

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    app.logger.info("Testing logging information before if")
    if request.method=='POST':
        app.logger.info("Testing logging information after if")
       
        filestr=request.files['image']
        app.logger.info(filestr)
        filestr.save("./static/images/"+secure_filename(filestr.filename))
        # pic=Image.open("./static/images/"+secure_filename(filestr.filename))
        # app.logger.info(type(pic))
    
       
        text=get_bounds("./static/images/"+secure_filename(filestr.filename))
        app.logger.info(text)

        img2=get_boxes("./static/images/"+secure_filename(filestr.filename))
        pic=Image.fromarray(img2)
        # pic.show()
        pic.save('./static/images/new'+secure_filename(filestr.filename))
        im='./static/images/new'+secure_filename(filestr.filename)
        # im=pic.open('./static/images/new.jpg')
       
      
            
       
     
    # return redirect(url_for('mainpage.html'))
    return render_template('mainpage.html', img=im, text=text)





if __name__=="__main__":
    app.run(debug=True)
