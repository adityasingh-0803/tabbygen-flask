from flask import Flask, render_template, request

app = Flask(__name__)

def generate_feedback(transcript, role):
    dummy_feedbacks = {
        'PM': '''
🔹 Role: Prime Minister (PM)

✅ Strengths:
- Clear framing of the motion with a compelling opening.
- Presented a strong model with logical steps.

📉 Areas to Improve:
- Arguments lacked comparative weight.
- Rebuttals were not preemptively addressed.

🔚 Overall Score: 7.8/10
''',
        'LO': '''
🔹 Role: Leader of Opposition (LO)

✅ Strengths:
- Strong signposting and structure.
- Engaged well with the government’s case.

📉 Areas to Improve:
- Introduction lacked thematic clarity.
- Rebuttals repeated without new logic.

🔚 Overall Score: 7.6/10
''',
        'MG': '''
🔹 Role: Member of Government (MG)

✅ Strengths:
- Excellent extension with clear separation from PM.
- New arguments were relevant and analytical.

📉 Areas to Improve:
- Could have engaged more with LO’s framing.

🔚 Overall Score: 8.2/10
''',
        'MO': '''
🔹 Role: Member of Opposition (MO)

✅ Strengths:
- Strong contextual analysis of government case.
- Clear and methodical structure.

📉 Areas to Improve:
- Missed opportunity to undercut the extension logic.

🔚 Overall Score: 7.9/10
'''
    }
    return dummy_feedbacks.get(role, "No feedback available for the selected role.")

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
