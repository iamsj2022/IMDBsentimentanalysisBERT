from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin

from predictionFile import Prediction
from trainMovieRvwSystem import TrainBertModel


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    data = request.json['data']
    try:
        if len(data) == 1:
            data.append("")
            predictorObj = Prediction()
            result = predictorObj.executeProcessing(data)
            result.pop()
            return jsonify({"Results" : str(result)})
        else:
            predictorObj = Prediction()
            result = predictorObj.executeProcessing(data)
            return jsonify({"Results" : str(result)})
    except:
        return {"Results" :"Wrong Data Format Sent"}

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

'''
    # For Prediction of Model
    sentence_list = [
        "That movie was absolutely awful",
        "The acting was a bit lacking",
        "The film was creative and surprising",
        "Absolutely fantastic!"
    ]   
'''


'''
    # For Prediction of Model
    sentence_list = [
        "Goosebumps overloaded!!"
        "A 'mass' movie for low IQ people."
        "Chapter 2 is The Super-Duper Blockbuster Movie of 2022 !!!"
       "Worst South Sequel Ever!!!" 
   ] 
'''