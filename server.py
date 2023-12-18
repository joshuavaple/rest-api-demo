from flask import Flask, request, jsonify
import mlflow

app = Flask(__name__)
summarizer = mlflow.transformers.load_model('azureml://southeastasia.api.azureml.ms/mlflow/v2.0/subscriptions/b10dba21-0331-4510-a7cb-924077c9cb52/resourceGroups/dev-csdw-rg/providers/Microsoft.MachineLearningServices/workspaces/dev-csdw-ml-workspace/experiments/55795ceb-a274-41f1-a25f-dac4ceb8567f/runs/371d5d4d-98bd-4522-8e1a-9d81bae83a8d/artifacts/models/pretrained/t5_small_text_summarization')

@app.route('/summarize', methods=['POST'])
def summarize():
    try: 
        data = request.get_json()
        text = data['text']
        summary = summarizer(text)[0]['summary_text']
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)