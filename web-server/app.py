# Simple Web-Server

from flask import Flask
import subprocess

app = Flask(__name__)

def workers():

    cmd_ip = 'ifconfig | sed -n 2p | cut -d ":" -f2 | cut -d " " -f1 | tr -d "\n"'
    cmd_hostname = 'hostname | tr -d "\n"'

    ip_addr = str(subprocess.check_output(cmd_ip, shell=True))
    hostname = str(subprocess.check_output(cmd_hostname, shell=True))

    return '''
<html>
<style>
  h1   {color:blue}
  h2   {color:red}
</style>
  <div align="center">
  <head>
    <title>Web-Server Container</title>
  </head>
  <body>
    <h1>Hi, I am a Web Server !!</h1><br><h2>This page is served by a <b>Docker Container</b> </h2><br><h3>IP address = ''' + ip_addr + '''<br>Hostname = ''' + hostname + '''</h3>
    <img src="/static/giphy.gif">
  </body>
  </div>
</html>
'''

@app.route('/')
def root():

    return workers()

@app.route('/contrail')
def contrail():

    return workers()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)
