from flask import Flask,render_template,request
import MLAppPredict as ml

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html' ,name='anais')

@app.route('/validate',methods=['GET','POST'])
def validate():
   radius=request.form['mean_radius']
   texture=request.form['mean_texture']
   perimeter=request.form['mean_perimeter']
   area=request.form['mean_area']
   smoothness=request.form['mean_smoothness']
   prediction=ml.bcprediction(radius,texture,perimeter,area,smoothness)
   if prediction==0:
       predict='YOU DO NOT HAVE BREAST CANCER'
   else:
       predict='YOU HAVE BREAST CANCER YOU HAVE TO SEEK MEDICAL ATTENTION AS QUICK AS POSSIBLE'     
   
    
   return render_template('validate.html',predicte=predict)
if __name__=="__main__":
    app.run(debug=True)    