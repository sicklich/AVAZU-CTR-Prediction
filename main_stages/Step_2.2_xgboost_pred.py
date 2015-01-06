# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 14:46:43 2015

@author: ivan
"""
from datetime import datetime
from csv import DictReader
import pandas as pd

xgboost_file = 'xgboost/pred.txt'
pred = pd.read_csv(xgboost_file,index_col = False, header = None)
pred.head()

submit_file = 'xgboost/submission.csv'
submit = pd.read_csv(submit_file)

submit['click'] = pred

submit.to_csv('xgboost/submit_xgboost.csv',index=False)