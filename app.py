from flask import Flask
from flask import request
from flask import render_template
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless=new")

cam1 = webdriver.Chrome(options=options)
cam2 = webdriver.Chrome(options=options)
cam3 = webdriver.Chrome(options=options)
cam4 = webdriver.Chrome(options=options)

#Live Gets
cam1.get("http://admin:abcd1234@10.0.1.11/rmt.html")
cam2.get("http://admin:abcd1234@10.0.1.12/rmt.html")
cam3.get("http://admin:abcd1234@10.0.1.13/rmt.html")
cam4.get("http://admin:abcd1234@10.0.1.14/rmt.html")

#Test Gets
# cam1.get("http://127.0.0.1:3000")
# cam2.get("http://127.0.0.1:3000")
# cam3.get("http://127.0.0.1:3000")
# cam4.get("http://127.0.0.1:3000")

try:
    element1 = WebDriverWait(cam1, 10).until(EC.presence_of_all_elements_located())
    element2 = WebDriverWait(cam2, 10).until(EC.presence_of_all_elements_located())
    element3 = WebDriverWait(cam3, 10).until(EC.presence_of_all_elements_located())
    element4 = WebDriverWait(cam4, 10).until(EC.presence_of_all_elements_located())
except:
    print("brokey")

cam1_iris = int(cam1.execute_script("return IrisValue;"))
cam2_iris = int(cam2.execute_script("return IrisValue;"))
cam3_iris = int(cam3.execute_script("return IrisValue;"))
cam4_iris = int(cam4.execute_script("return IrisValue;"))

#print(cam1_iris, cam2_iris, cam3_iris ,cam4_iris)

app = Flask(__name__)

irisValues = [1.9, 2.0, 2.2, 2.4, 2.6, 2.8, 3.1, 3.4, 3.7, 4, 4.4, 4.8, 5.2, 5.6, 6.2, 6.8, 7.3, 8, 8.7, 9.6, 10, 11, 12, 14, 15, 16, 65535]

@app.route("/")
def index():
    return render_template('index.html', cam1_iris=cam1_iris, cam2_iris=cam2_iris, cam3_iris=cam3_iris, cam4_iris=cam4_iris)

@app.route("/cam1/<value>")
def cam1update(value):
    global cam1_iris 
    cam1_iris = int(value)
    print(value)
    script = f"""
            IrisValue = {irisValues[int(value)]};
            IrisCtrl.SetValue();
    """
    cam1.execute_script(script)
    return value

@app.route("/cam2/<value>")
def cam2update(value):
    global cam2_iris 
    cam2_iris = int(value)
    print(value)
    script = f"""
            IrisValue = {irisValues[int(value)]};
            IrisCtrl.SetValue();
    """
    cam2.execute_script(script)
    return value

@app.route("/cam3/<value>")
def cam3update(value):
    global cam3_iris 
    cam3_iris = int(value)
    print(value)
    script = f"""
            IrisValue = {irisValues[int(value)]};
            IrisCtrl.SetValue();
    """
    cam3.execute_script(script)
    return value

@app.route("/cam4/<value>")
def cam4update(value):
    global cam4_iris 
    cam4_iris = int(value)
    print(value)
    script = f"""
            IrisValue = {irisValues[int(value)]};
            IrisCtrl.SetValue();
    """
    cam4.execute_script(script)
    return value

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)