# Text File Viewer

This Flask application allows users to view the contents of text files in HTML format. It provides a single GET route where users can specify the file name and optional start and end line numbers as URL parameters. The application handles errors gracefully and displays error pages with exception details when necessary.

## Usage

1. Clone the repository.
2. Install the dependencies listed in `requirements.txt`.
3. Run the Flask application using `python app.py`.
4. Open a web browser and navigate to `http://localhost:5000/`.
5. Specify the file name and optional start and end line numbers in the URL parameters to view the file content.

## Features

- Renders text files in HTML format.
- Supports specifying start and end line numbers to view a specific portion of the file.
- Utilizes Material-UI for styling the HTML content.
- Gracefully handles errors and displays error pages with exception details.
