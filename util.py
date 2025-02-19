from typing import List, Union, Dict
import datetime
import json

def get_list_of_chanels() -> List[str]:
    
    with open('chanels.txt', 'r') as f:
        chanels = f.readlines()

    chanels = [c.strip() for c in chanels]
    return chanels

def get_prefix_for_chanels() -> Dict[str, str]:
    
    with open('chanels_prefixes.json', 'r') as f:
        d = json.load(f)
        
    if isinstance(d, dict):
        return d
    
    return {}

def is_today(dt: Union[str, datetime.datetime]) -> bool:
    today = datetime.datetime.today().date()
    
    if isinstance(dt, str):
        if datetime.datetime.fromisoformat(dt).date() == today:
            return True
        
    elif isinstance(dt, datetime.datetime):
        if dt.date() == today:
            return True
        
    return False

def get_config():
    with open('config.json', 'r') as f:
        d = json.load(f)
    return d
