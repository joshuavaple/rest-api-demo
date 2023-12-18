from flask import Flask, request, jsonify
from transformers import pipeline
import traceback
from datetime import datetime

app = Flask(__name__)

# first, we need to set up the endpoint
# POST is used instead of GET because we are sending data to the server, not getting data from the server
@app.route("/predict", methods=["POST"])
# now, we can make a prediction endpoint
def predict_sentence():
    try:
        start = datetime.now()
        # get the sentence from the request body
        sentence = request.json["sentence"]
        # load the model
        app = pipeline(task="text-classification",
                        model="./models/pre_trained/roberta-base-go_emotions",
                        top_k=5)
        prediction = list(app(sentence)[0])
        end = datetime.now()
        time_taken = end - start
        return jsonify({'top_5_predictions': str(prediction),
                        'time_taken_seconds': str(time_taken)})
    except:
        return jsonify({'trace': traceback.format_exc()})

# let's create another route fot the summary endpoint
@app.route("/summarize", methods=["POST"])
def summarize_text():
    try:
        start = datetime.now()
        # get the text from the request body
        text = request.json["text"]
        summarizer = pipeline(task="summarization", 
                              model="./models/pre_trained/t5_small_text_summarization")
        summary = summarizer(text)[0]["summary_text"]
        end = datetime.now()
        time_taken = end - start
        return jsonify({'summary': str(summary),
                        'time_taken_seconds': str(time_taken)})
    except:
        return jsonify({'trace': traceback.format_exc()})

if __name__ == '__main__':
    app.run(debug=True)
