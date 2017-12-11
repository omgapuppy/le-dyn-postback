#!/usr/bin/env python

from logentries import LogentriesHandler
import logging
from flask import Flask, jsonify, request
import os

listener = Flask(__name__)

# Configure the port your postback URL will listen on
PORT = 5000
# Note - LOGENTRIES_TOKEN is provided via env variable

log = logging.getLogger('logentries')
log.setLevel(logging.INFO)
dyn = LogentriesHandler(os.environ["LOGENTRIES_TOKEN"])
log.addHandler(dyn)
# Enter the following for the bounce postback URL:
# SCRIPT_HOST_IP:PORT/bounce?e=@email&r=@bouncerule&t=@bouncetype&dc=@diagnostic&s=@status
@listener.route('/bounce', methods=['GET'])
def bounce():
    e = request.args.get('e')
    r = request.args.get('r')
    t = request.args.get('t')
    dc = request.args.get('dc')
    s = request.args.get('s')
    log.info("BOUNCE email='{}' rule='{}' type='{}' diagnostic='{}'\
    status='{}'".format(e, r, t, dc, s))
    return jsonify(result={"status": 200})

# Enter the following for the complaint postback URL:
# SCRIPT_HOST_IP:PORT/complaint?e=@email
@listener.route('/complaint', methods=['GET'])
def complaint():
    e = request.args.get('e')
    log.info("COMPLAINT email='{}'".format(e))
    return jsonify(result={"status": 200})


if __name__ == '__main__':
    listener.run(host='0.0.0.0',
                 port=PORT,
                 debug=False)
