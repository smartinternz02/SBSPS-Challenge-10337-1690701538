from flask import Flask, render_template, request, session,flash
import requests
import ibm_db


app = Flask(__name__)
app.secret_key ='a'

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=9938aec0-8105-433e-8bf9-0fbb7e483086.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32459;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hzk47323;PWD=jhJ8WCScbq7hOY1J",'','')
print(conn)
print("connection successful...")
# =============================================================================
# url = "https://electric-vehicle-charging-stations.p.rapidapi.com/getByCordsAdv"
# querystring = {"lat":"40.733154296875","lng":"-73.99571228027344","radius":"10","page":"1","per_page":"10","access_param":"public","ev_connector_type_param":"J1772","ev_network_param":"Tesla,Tesla Destination","owner_type_param":"all"}
# headers = {
#  	"X-RapidAPI-Key": "05e6b8edccmsh7ef028db4983267p1abf89jsnc05651039ac0",
#  	"X-RapidAPI-Host": "electric-vehicle-charging-stations.p.rapidapi.com"
# }
# response = requests.get(url, headers=headers, params=querystring)
# print(response.json())
# =============================================================================
def insertdb(conn,stationName,streetAddress,city,state,zip,country,latitude,longitude):
    sql= "INSERT into charge VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(stationName,streetAddress,city,state,zip,country,latitude,longitude)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))

def insertdb(conn,connector,name,timeslot,phonenumber,cost,chargestationname,address):
    sql= "INSERT into slot VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(conn,connector,name,timeslot,phonenumber,cost,chargestationname,address)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))

@app.route('/')
def index():
    return render_template('userprofile.html')

@app.route('/home')
def home():
    return render_template('userprofile.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/upload')
def upload():
    return render_template('registration.html')

@app.route('/slot')
def slot():
    return render_template('slot.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/confirm')
def confirm():
    return render_template('confirm.html')

@app.route('/nearchargestation')
def nearchargestation():
    return render_template('chargestationform.html')

@app.route('/getlocation')
def getlocation():
    return render_template('getloaction.html')

@app.route('/bike')
def bike():
    return render_template('bike.html')

@app.route('/search', methods=['POST'])
def search():
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    radius = request.form['radius']

    # You can now use these values to make the API request

    response_data = {
        'latitude': latitude,
        'longitude': longitude,
        'radius': radius
    }
    url = "https://vehicle-charging-stations.p.rapidapi.com/poi/"


    querystring = {"longitude":longitude,"latitude":latitude,"distance":radius}
    headers = {
	"X-RapidAPI-Key": "4d2d2cbbdamsh2eca708138973fcp19c2b6jsnd6dda6eafa0a",
	"X-RapidAPI-Host": "vehicle-charging-stations.p.rapidapi.com"
}


    response = requests.get(url, headers=headers, params=querystring)
    data1=response.json()
    
    return render_template('index.html', data=data1)
     
@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == "POST":
        stationName= request.form['stationName']
        streetAddress= request.form['streetAddress']
        city = request.form['city']
        state = request.form['state']
        zip = request.form['zip']
        country = request.form['country']
        latitude = request.form['latitude']
        longitude = request.form['longitude']        
        #inp=[name,email,contact,address,role,branch,password]
        insertdb(conn,stationName,streetAddress,city,state,zip,country,latitude,longitude)
        return render_template('registration.html')
@app.route('/slot1', methods=['POST','GET'])
def slot1():
    if request.method == "POST":
        connector= request.form['connector']
        name= request.form['name']
        timeslot= request.form['timeslot']
        phonenumber= request.form['phonenumber']
        cost= request.form['cost']
        chargestationname= request.form['chargestationname']    
        address= request.form['address']
        #inp=[name,email,contact,address,role,branch,password]
        insertdb2(conn,connector,name,timeslot,phonenumber,cost,chargestationname,address)
        return render_template('slot.html')

if __name__ == '__main__':
    app.run(debug=True)
