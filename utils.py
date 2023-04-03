# -*- coding: utf-8 -*-

from app import app
import os

FEATURE_FLAG_FILE = os.getenv('FEATURE_FLAG_FILE', default=app.config.get('FEATURE_FLAG_FILE'))

def read_feature_flag():
    try:
        with open(FEATURE_FLAG_FILE, 'r') as f:
            line = f.readline()
            if 'ALL' not in line and 'country=' in line:
                return line.split('=')[1].strip()
    except IOError as e:
        return None

    return None