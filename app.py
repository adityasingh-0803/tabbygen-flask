from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy feedback generator
def generate_feedback(transcript, role):
    return f"[Demo] Feedback for {role}:\nGreat use of structure and tone. Improve clarity in your second argument. Try summarizing stronger."

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
