from flask import Flask, jsonify, render_template, request
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/system_data')
def system_data():
    try:
        cpu = psutil.cpu_percent(interval=0.5)
        memory = psutil.virtual_memory().percent
        network = psutil.net_io_counters()
        disk = psutil.disk_usage('/').percent
        process_count = len(psutil.pids())

        processes = []
        for p in psutil.process_iter(['pid', 'name']):
            try:
                processes.append(p.info)
            except psutil.NoSuchProcess:
                continue

        processes = sorted(processes, key=lambda x: x['pid'], reverse=True)[:10]

        return jsonify({
            'cpu': cpu,
            'memory': memory,
            'network_sent': network.bytes_sent,
            'network_recv': network.bytes_recv,
            'disk': disk,
            'process_count': process_count,
            'processes': processes
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/kill_process', methods=['POST'])
def kill_process():
    pid = request.json.get('pid')
    try:
        if not psutil.pid_exists(pid):
            return jsonify({'success': False, 'error': 'Process not found.'})
        p = psutil.Process(pid)
        p.terminate()
        p.wait(timeout=3)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
