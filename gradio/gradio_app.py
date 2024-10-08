import gradio as gr
import requests
import os

hate_speech_predict_api = os.getenv(
    "HATE_SPEECH_PREDICT_API",
    "https://hatespeech-flask.azurewebsites.net/predict",
)


# Define the function to send text to the MLflow model API and get the
# prediction
def predict_hate_speech(text):
    # Adjust the URL if your API is hosted elsewhere
    url = hate_speech_predict_api
    data = {"inputs": text}
    headers = headers = {
        "Content-type": "application/json",
        "Accept": "application/json",
    }
    print(data)
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        return f"{prediction}"
    else:
        return f"Error: {response.text}"


# Create the Gradio interface
iface = gr.Interface(
    fn=predict_hate_speech,
    inputs=gr.Textbox(lines=5, label="Enter Text"),
    outputs="text",
    title="Hate Speech Detection",
    description="Enter text and click submit to classify \
        it as hate speech or not.",
)

# Launch the Gradio app
if __name__ == "__main__":
    iface.launch()
