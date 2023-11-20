from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import numpy as np
import laspy
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('Please select a file before submitting.')
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        flash('Please select a file before submitting.')
        return redirect(url_for('index'))

    if file:
        xyz_data = np.genfromtxt(file, delimiter=" ")

        las_file_path = "./DownlodedFiles/output.las"  # Set the path where you want to save the LAS file
        out_file = laspy.file.File(las_file_path, mode="w", header=laspy.header.Header())

        out_file.header.scale = [0.001, 0.001, 0.001]
        out_file.header.offset = [0, 0, 0]
        out_file.header.x_scale_factor = 0.001
        out_file.header.y_scale_factor = 0.001
        out_file.header.z_scale_factor = 0.001

        out_file.x = xyz_data[:, 0]
        out_file.y = xyz_data[:, 1]
        out_file.z = xyz_data[:, 2]

        out_file.close()

        return send_file(las_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
