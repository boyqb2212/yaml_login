#!/usr/bin/env python

import logging
from logging.config import dictConfig
import os
import json
import yaml
# yaml_logging 

path = 'logging.yaml'
if os.path.exists(path):
    with open(path,'r') as f :
        config = yaml.safe_load(f.read())
    dictConfig(config)    
    #dictConfig(config)

logger1 = logging.getLogger("server")
logger2= logging.getLogger("client")



