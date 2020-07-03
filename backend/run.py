from flask import Flask, request, render_template
import numpy as np
import cv2
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    return render_template('upload.html')

@app.route('/view', methods=['POST','GET'])
def upload_image():
    f = request.files['file'].read()
    npim = np.fromstring(f,np.uint8)
    img = cv2.imdecode(npim,cv2.IMREAD_COLOR)
    # print(img)
    # cv2.imshow("",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # np.reshape(npim,(280,280))
    # rows = 0
    # cols = 0
    # for i in npim:
        # rows+=1
    # for i in npim[0:1,]:
        # cols+=1
    # print(npim[0:1,])
    # print(rows,cols)

    return render_template('viewimage.html')
	# if 'file' not in request.files:
	# 	flash('No file part')
	# 	return redirect(request.url)
	# file = request.files['file']
	# if file.filename == '':
	# 	flash('No image selected for uploading')
	# 	return redirect(request.url)
	# if file and allowed_file(file.filename):
	# 	filename = secure_filename(file.filename)
	# 	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	# 	#print('upload_image filename: ' + filename)
	# 	flash('Image successfully uploaded and displayed')
	# 	return render_template('upload.html', filename=filename)
	# else:
	# 	flash('Allowed image types are -> png, jpg, jpeg, gif')
	# 	return redirect(request.url)

app.run()