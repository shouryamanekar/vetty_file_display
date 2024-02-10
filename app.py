from flask import Flask, render_template, request
import os
import chardet

app = Flask(__name__)

# Define the directory where files are stored
files_dir = os.path.join(os.path.dirname(__file__), 'files')

@app.route('/')
def display_file():
    # Get filename from URL parameter, default to 'file1.txt'
    filename = request.args.get('filename', 'file1.txt')

    # Get start and end line numbers from URL parameters
    start_line = request.args.get('start_line', type=int)
    end_line = request.args.get('end_line', type=int)

    try:
        # Construct the full file path
        filepath = os.path.join(files_dir, filename)

        # Open the file in binary mode to ensure correct reading
        with open(filepath, 'rb') as f:
            # Read the raw data from the file
            raw_data = f.read()

            # Detect the encoding of the raw data
            encoding = chardet.detect(raw_data)['encoding']

            # Decode the raw data using the detected encoding
            content = raw_data.decode(encoding)

        # Split the content into lines
        lines = content.split('\n')

        # Filter lines based on start and end line numbers
        if start_line is not None and end_line is not None:
            lines = lines[start_line-1:end_line]
        elif start_line is not None:
            lines = lines[start_line-1:]
        elif end_line is not None:
            lines = lines[:end_line]

        # Join the lines back into a single string
        content = '\n'.join(lines)

        # Render the file content in the template
        return render_template('file_display.html', content=content)
    
    except Exception as e:
        # Render error page if an exception occurs
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
