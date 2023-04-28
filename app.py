from flask import Flask, request, render_template, flash, get_flashed_messages
from utils.openaiapi import OpenAI
import os

app = Flask(__name__)
app.secret_key = b'_5#y26r"4K9z\n\xec]/'
ai = OpenAI()
from utils.generator import IncidentGenerator
incidents = IncidentGenerator()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/import_syslog', methods=['GET', 'POST'])
def import_syslog():
    if request.method == 'GET' and request.args.get('start'):
        start = int(request.args.get('start'))
        end = int(request.args.get('end'))
        prompt = incidents.generateIncidentsPrompt(incidents.generateNumberIncidents(start, end))
        analysis = ai.analyze(prompt)
        result = analysis.choices[0].text
        return render_template('import_syslog.html', incidents=enumerate(incidents.incidents), result=result)
    if request.method == 'POST' and request.files['file']:
        file = request.files['file']
        incident_list = []
        for line in file.readlines():
            incident_list.append(line.decode())
        incidents.loadIncidents(incident_list)
        return render_template('import_syslog.html', incidents=enumerate(incidents.incidents))
    return render_template('import_syslog.html', incidents=enumerate(incidents.incidents))

if __name__ == '__main__':
    app.run(host="0.0.0.0")