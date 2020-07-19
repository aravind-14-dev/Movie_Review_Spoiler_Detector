import numpy as np
from flask import Flask, request, jsonify
import joblib
from text_proc import text_process

app = Flask(__name__)

model = joblib.load(open('NB1.joblib','rb'))
#model_clf = model['pipeline_clf']

@app.route('/api',methods=['POST'])  #route /api paths to predict fn , POST - predict handles post requests
def predict():
    data = request.get_json(force=True)  #access json from incoming requests
    prediction = model.predict(data["x"])
    output_text = "Text:" + str(data["x"])
    output = ["Spoiler" if i else "No Spoiler" for i in prediction]
    #output = "Class: " + str(prediction)


    return jsonify(output_text,output)  # return json respons

if __name__ == '__main__':
    app.run(port=8080,debug=True)