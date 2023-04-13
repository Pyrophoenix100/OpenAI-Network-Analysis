from flask import Flask, request, render_template, flash, get_flashed_messages
from utils.openaiapi import OpenAI
import os

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4K9z\n\xec]/'
ai = OpenAI()
from utils.generator import IncidentGenerator
incidents = IncidentGenerator()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/import_syslog', methods=['GET', 'POST'])
def import_syslog():
    if request.method == 'POST' and request.files['file']:
        file = request.files['file']
        incident_list = []
        for line in file.readlines():
            incident_list.append(line.decode())
        incidents.loadIncidents(incident_list)
        return render_template('import_syslog.html', success=True, incidents=enumerate(incidents.incidents))
    else:
        flash("No file supplied", "error")
        return render_template('index.html')

@app.route('/analyze_incident', methods=['GET', 'POST'])
def analyze_incident():
    if request.method == 'POST':
        start = int(request.form['start'])
        end = int(request.form['end'])
        prompt = incidents.generateIncidentsPrompt(incidents.generateNumberIncidents(start, end))
        analysis = ai.analyze(prompt)
        result = analysis.choices[0].text
        return render_template('analyze_incident.html', result=result)
    else:
        return render_template('index.html', flashes=get_flashed_messages())


@app.route('/gpt_options', methods=['GET', 'POST'])
def gpt_options():
    if request.method == 'POST':
        option = request.form['option']
        if option == '1': # Context Prompt
            new_prompt = request.form['new_prompt']
            if new_prompt:
                ai.context_prompt = new_prompt
        elif option == '2': # Max Tokens
            new_tokens = request.form['new_tokens']
            if new_tokens:
                ai.max_generation = int(new_tokens)
        elif option == '3': # Change Model
            new_model = request.form['new_model']
            if new_model:
                ai.model = int(new_model)
        return render_template('gpt_options.html', success=True, ai=ai)
    else:
        return render_template('gpt_options.html', ai=ai)

if __name__ == '__main__':
    app.run(debug=True)