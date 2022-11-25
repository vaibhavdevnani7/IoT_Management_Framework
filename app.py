from flask import Flask, request, jsonify
import who_is_on_my_wifi as wiom
import time

app = Flask(__name__)
time_last = time.time()
@app.route('/listdevices')
def find_devices():
    WHO = wiom.who()
    devices = []
    for j in range(0, len(WHO)):
        if 'ESP_DEVICE' in WHO[j][5]:
            devices.append(WHO)
    return jsonify(devices)

@app.route('/<device>/uploadbin', methods=["POST"])
def uploadbin(device):
    # code to encode the file and send i to device for flashing
    return (str(request.data) + "succesfully uploaded and flashed")

@app.route('/<device>/variable/<method>', methods=["POST"])
def devicevars(device, method):
    if method=='list':
        variables = {}
        # code to get variables from device here
        variables = {'Var1':55,'TestVar2':5}
        return jsonify(variables)
    elif method == 'get':
        variables = {}
        # code to get variables from device here
        variables = {'Var1':55,'TestVar2':5}
        args = request.args
        name = args.get('variable')
        return jsonify(variables[name])

@app.route('/<device>/config/<method>', methods=["POST"])
def configvars(device, method):
    if method=='list':
        configvars={}
        # code to get config variables from device here
        configvars = {'config1':100,'Testconfig':1}
        return jsonify(configvars)
    elif method == 'change':
        args = request.args
        name = args.get('config')
        change  = request.data
        # code to request device to change config
        return (str(name) + 'changed to' + str(change))
        
@app.route('/<device>/healthstatus', methods=["POST"])
def health_status(device):
    devicehealth = {}
    # code to detch device health
    devicehealth = {'voltage': '3.89', 'current': '120', 'temp': '38'}
    return jsonify(devicehealth)

@app.route('/<device>/files/<method>', methods=["POST"])
def device_files(device, method):
    if method=='list':
        files = []
        # code to fetch file list from device
        files = ['config1.json', 'a.bmp']
        return jsonify(files)
    elif method == 'get':
        args = request.args
        name = args.get('filename')
        # code to fetch filedata from device
        return (name)
    elif method == 'upload':
        # code to upload filedata from device
        return (str(request.data) + 'File has been uploaded to device')


@app.route('/<device>/serialout', methods=["GET"])
def serial_out(device):
    serialout = []
    #code to get serial out from device
    serialout = ['Serial out testing', 'Line 2']
    time_last = time.time()
    return jsonify('Serial output till ' + str(round(time_last)) +"  "+ str(serialout))

app.run()