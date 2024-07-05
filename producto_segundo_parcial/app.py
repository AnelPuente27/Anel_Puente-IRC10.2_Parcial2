from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    playbooks = os.listdir('playbooks')
    return render_template('index.html', playbooks=playbooks)

@app.route('/run_playbook', methods=['POST'])
def run_playbook():
    if request.method == 'POST':
        playbook = request.form.get('playbook')
        if playbook:
            playbook_path = os.path.join('playbooks', playbook)
            if os.path.exists(playbook_path):
                try:
                    result = subprocess.run(['ansible-playbook', playbook_path], capture_output=True, text=True)
                    return render_template('output.html', output=result.stdout)
                except Exception as e:
                    return render_template('output.html', output=str(e))
    return "No playbook specified or playbook does not exist."

if __name__ == '__main__':
    app.run(debug=True)
