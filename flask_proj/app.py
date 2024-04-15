from flask import Flask, render_template, request, jsonify
from abra import run_abra_script
import matplotlib
import os

app = Flask(__name__)
matplotlib.use('Agg')

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'audioFile' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['audioFile']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'File uploaded successfully', 'filename': filename})
    else:
        return jsonify({'error': 'Error uploading file'})

@app.route('/upload_filename', methods=['POST'])
def upload_filename():
    try:
        uploaded_filename = request.json.get('filename')
        if uploaded_filename:
            # Здесь вы можете выполнить дополнительные действия с именем файла
            return jsonify({'message': 'Имя файла успешно получено'})
        else:
            return jsonify({'error': 'Имя файла не было передано'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/run_abra_script', methods=['POST'])
def run_abra_script_route():
    try:
        uploaded_filename = request.json.get('filename')
        if uploaded_filename:
            # Запускаем скрипт Abra
            result = run_abra_script(uploaded_filename)
            print(result)
            # return jsonify({'message': 'Скрипт отработал', 'output': result})

            return jsonify({
                'message': 'Скрипт Abra успешно выполнен',
                'output':
                    {
                        # 'image_path': result['image_path'],  # Передаем путь к изображению
                        'average_tempos': result['average_tempos'],
                        'total_tempo': result['total_tempo'],
                        'average_tempo': result['average_tempo'],
                        'audio_duration': result['audio_duration']
 
                    }
            })
        else:
            return jsonify({'error': 'Имя файла не было передано'})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
