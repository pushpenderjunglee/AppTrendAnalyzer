from flask import Flask,request, render_template
app = Flask(__name__)
import play_scraper
import pandas as pd

@app.route("/",methods=['GET'])
def index():
    trending = play_scraper.collection(gl = 'in', collection='NEW_FREE', category='GAME', results=120)
    trending_data=[]
    for item in trending:
       print(item)
       trending_data.append([item['app_id'],item['icon'],item['url'],item['title'],item['developer'],item['score'],item['price']])
    return render_template('index.html',data=trending_data,len=len(trending_data))   


@app.route("/getdata",methods=['POST'])    
def playstore():
    trending_data = []
    trending = play_scraper.collection(gl = 'in', collection=request.form['col'], category=request.form['cat'], results=120)
    for item in trending:
        trending_data.append([item['app_id'],item['icon'],item['url'],item['title'],item['developer'],item['score'],item['price']])
    return render_template('result.html',data=trending_data,len=len(trending_data))   


app.run(debug=True)