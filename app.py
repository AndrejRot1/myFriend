from flask import Flask, render_template, request, jsonify
import openai

api_key = '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'

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual API key
openai.api_key = api_key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']

    # Using the OpenAI Python library to send a prompt to ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
        max_tokens=100
    )

    # Extracting the AI's response from the completion
    ai_response = response['choices'][0]['message']['content']

    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(debug=True)
