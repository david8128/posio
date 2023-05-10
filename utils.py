# -*- coding: utf-8 -*-

from app import app
import os
from flagsmith import Flagsmith
import json

def read_feature_flag():
    flagsmith = Flagsmith(environment_key="jTG9o3HTR97xSnvmRBuP4m") # The method below triggers a network request 
    flags = flagsmith.get_environment_flags() # Check for a feature 
    is_enabled = flags.is_feature_enabled("country_flag") # Or, use the value of a feature 
    if is_enabled:
        return flags.get_feature_value("country_flag")

    return None
