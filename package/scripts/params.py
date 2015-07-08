#!/usr/bin/env python
from resource_management import *

# config object that holds the configurations declared in the config xml file
config = Script.get_config()

# store the log file for the service commands outputs
stack_log = config['configurations']['redis-config']['redis.log']
