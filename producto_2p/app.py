from flask import Flask, render_template, request
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == 'POST':
        # Ejecuta un comando ad hoc de Ansible para obtener el inventario
        result = subprocess.run(['ansible-inventory', '--inventory', 'inventory.ini', '--list'], capture_output=True, text=True)
        inventory_json = json.loads(result.stdout)
        return render_template('inventory.html', inventory=inventory_json)
    return render_template('inventory.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
