from cmath import e
import imp
from flask import Flask,render_template,url_for,request
from model import getprediction
#from model import getprediction
# config=tf.compat.v1.ConfigProto()
# config.gpu_options.allow_growth = True
# sess = tf.compat.v1.Session(config=config)


# physical_devices = tf.config.list_physical_devices('GPU')
# try :
#     tf.config.experimental.set_memory_growth(physical_devices[0], True)
# except e :
#     print(e)

app=Flask(__name__)


@app.route('/',methods=['GET'])
def hello_world():
    return render_template("home.html")


@app.route('/',methods=['POST'])
def predict() :
    imagefile = request.files['imagefile']
    imagepath = "./static/images/"+imagefile.filename
    imagefile.save(imagepath)

    label = getprediction(imagepath)

    p1 = ('%s (%.2f%%)' % (label[0][0][1], label[0][0][2]*100)).split()
    p2 = ('%s (%.2f%%)' % (label[0][1][1], label[0][1][2]*100)).split()
    p3 = ('%s (%.2f%%)' % (label[0][2][1], label[0][2][2]*100)).split()


    return render_template('home.html', prediction1=p1,prediction2=p2,prediction3=p3, image="."+imagepath)










app.run(port=3000,debug=True)
    
