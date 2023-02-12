from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def open_file_dialog():
    return '''
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Calculate">
        </form>
    '''

@app.route('/', methods=['POST'])
def calculate_characters():
    file = request.files['file']
    contents = file.read().decode('utf-8')
    total_characters = len(contents)
    return f'Total characters: {total_characters}'

if __name__ == '__main__':
    app.run()
