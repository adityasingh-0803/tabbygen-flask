from flask import Flask, render_template, request
import ollama  # Replace with openai if using GPT API

app = Flask(__name__)

def generate_feedback(transcript, role):
    prompt = f"You are a debate coach. Give personalized feedback to a {role} speaker based on this speech:\n{transcript}\nFocus on logic, clarity, and persuasiveness."
    response = ollama.chat(model='mistral', messages=[
        {"role": "user", "content": prompt}
    ])
    return response['message']['content']

@app.route('/', methods=['GET', 'POST'])
def feedback_view():
    feedback = None
    if request.method == 'POST':
        transcript = request.form.get('transcript')
        role = request.form.get('role')
        feedback = generate_feedback(transcript, role)
    return render_template('upload_transcript.html', feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
