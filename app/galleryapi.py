# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
SuisenGalleryApi V0.1
@author: marunowork
"""

import os
import sys
import time
import json
from datetime import datetime, date, time, timedelta
from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
from subprocess import check_output
from jsonp_flask import jsonp
from app.constants import *

## setting 
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS( app, resources = { r"/api" : {"origins" : "*" } } )

def bstr( b_param, s_true, s_false):
    b_str = s_false
    if b_param :
        b_str = s_true
    return ( b_str )

def get_app_path():
    return ( str( check_output(["which", "instagram-scraper"]), 'utf-8' ).strip() )

def del_json_file( f_prm ):
    if os.path.isfile( JSON_FILE_NAME ) and len( f_prm ) > 0 :
        os.remove( JSON_FILE_NAME )
    return ( bstr( os.path.isfile( JSON_FILE_NAME ), "1", "" ) )
        

def get_url_req_param( prm_name, prm_def ):
    if request.args.get(prm_name) is not None :
        prm = str( request.args.get( prm_name ) )
        ret = prm if len( prm ) > 0 else prm_def
        return ( ret )
    else :
        return ( prm_def )

def get_file_dt():
    if not os.path.isfile( JSON_FILE_NAME ) :
        return ( datetime(UPDATE_MAX_YYYY \
                , UPDATE_MAX_MM, UPDATE_MAX_DD) )
    else :
        p = os.stat( JSON_FILE_NAME )
        return ( datetime.fromtimestamp( p.st_ctime ) )

def get_datetime_with_delta( dt, days_delta ):
    return ( dt + timedelta( days = days_delta ) )

def chk_json_file():
    dt_lim = get_datetime_with_delta( datetime.now() \
                , EXPIRE_DAYS ).strftime( '%Y%m%d' )
    dt_jsn = get_file_dt().strftime( '%Y%m%d' )
    return ( dt_jsn < dt_lim )
 
def run_proc_cmd():
    cmd = get_app_path()
    cmd += " --tag "
    cmd += TAGNAME
    cmd += " --quiet " if IS_QUIET_MODE else ""
    cmd += " --maximum "
    cmd += get_url_req_param( 'maxnum', str( LIST_MAXNUM ) )
    cmd += " --media-metadata -t none"
    res = subprocess.run( cmd, shell = True )
    return (res)

def load_json_file():
    f = open(JSON_FILE_NAME, 'r')
    json_data = json.loads( f.read() )
    return (json_data)


@app.route('/api',methods=['GET'])
@jsonp
def api():
    if len( get_url_req_param( 'force', "" ) ) > 0 :
        del_json_file( get_url_req_param( 'force', "" ) )
    if chk_json_file() == False :
        if run_proc_cmd().returncode != 0 :
            print( '外部プログラムの実行に失敗しました ', file = sys.stderr )
            sys.exit(1)
    return jsonify( ResultSet = load_json_file() ) 


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000)
