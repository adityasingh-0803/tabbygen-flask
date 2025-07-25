from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy API for feedback (replace with actual model later)
def generate_feedback(transcript, role):
    return f"This is dummy feedback for a {role} based on the transcript:\n\n{transcript[:200]}..."

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
