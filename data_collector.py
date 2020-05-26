# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:37:54 2020

@author: mende
"""

import json
import boto3
import os
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
sys.path.append('/tmp')
import yfinance as yf

def lambda_handler(event, context):
    
    # initialize boto3 client
    fh = boto3.client("firehose", "us-east-2")
    
    #leverage the power of yfinance.history
    stock_symbol = ['FB','SHOP','BYND','NFLX','PINS','SQ','TTD','OKTA','SNAP','DDOG']
    data = yf.Tickers(stock_symbol)
    history = data.history(start="2020-05-14", end="2020-05-15",interval="1m",group_by = 'tickers')

    req = []

    for stock in stock_symbol:
        for index, value in history[stock].iterrows():
            dataf = {'high':value['High'],'low':value['Low'],'ts':index.strftime('%Y-%m-%d %H:%M:%S'),'name':stock}
            
            #convert it into JSON
            as_jsonstr = json.dumps(dataf)
            
            # this actually pushed to our firehose datastream
            # we must "encode" in order to convert it into the
            # bytes datatype as all of AWS libs operate over
            # bytes not strings
            fh.put_record(
            DeliveryStreamName="STA9760-delivery-yfinance-stream", 
            Record={"Data": as_jsonstr.encode('utf-8')})
            
            req.append(dataf)

    # return
    return {
        'statusCode': 200,
        'body': json.dumps(f'Done! Recorded: {as_jsonstr}')
    }