"""Github-API operations module"""
import json
from datetime import datetime, timedelta
import requests
import config as cfg

def get_repo_info():
    """
    Gets the repo commits quantity and last commit info
    """
    response = requests.get(cfg.repo_url)
    info = json.loads(response.text)
    commit_info = info[0]['commit']['author']
    name = commit_info['name']
    local_date = datetime.strptime(commit_info['date'], '%Y-%m-%dT%H:%M:%SZ') + timedelta(cfg.gmt)
    date = local_date.strftime(cfg.datetime_format)
    return 'Total commits: %s. Last commit by %s (%s)' % (len(info), name, date)
