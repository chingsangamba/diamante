from flask import Flask,render_template,request
#from werkzeug import secure_filename
import os
app = Flask(__name__)
@app.route('/admin')
def admin():
    #go
    return render_template('admin.html')
@app.route('/')
def mains():
    return render_template('main.html')
'''@app.route('/<str:TITLE>')
def routess():
    return render_template(TITLE+'.html',title=TITLE)'''
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      g = request.form.get('title')
      folder_path = os.path.join(app.root_path, 'contents')
      folder_paths = os.path.join(folder_path, g)

      os.makedirs(folder_paths, exist_ok=True)
      #os.system('cd contents/'+g)
      f = request.files['file']
      sv = os.path.join(folder_paths, f.filename)
      
      f.save(sv)#issue is here
      j = request.form.get('email')
      op = request.form.get('description')
      with open(os.path.join(folder_paths, 'data.txt'),'a') as a:
        a.write('email:'+j+'\n description: '+op)
        a.close()

      return 'file uploaded successfully'
if __name__ == '__main__':
    app.run()