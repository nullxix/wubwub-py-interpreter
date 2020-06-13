from funky_tables import core as core_table
import core_actions

tables = {
    "temp" : {
        "keys":[],
        "values":[]
    },
    "user": {
        "keys": ["woof"],
        "values": [["bark", "bark"]],
    },
    "core" : {
        "keys":[],
        "values":[]
    },
}

def check_table(table_name, token):
    """chckes 
    """
    table = tables[table_name]
    for key in table:
        for i in range(0, len(table['keys'])):
            if(table['keys'][i] == token):
                return table['values'][i]
    return False

def check_token(token):
    """ finds first function that matches token
        if no function found, return none
    """
    
    #check temporary functions
    res = check_table("temp", token)
    if(res):
        return {"func": res, "table": "temp"}
    
    #check user (program) defined functions
    res = check_table("user", token)
    if(res):
        return {"func": res, "table": "user"}
    
    # finally, check core
    res = check_table("core", token)
    if(res):
        return {"func": res["func"], "runtime": res["runtime"], "table": "core"}

    # if function isn't found
    return {"func": False, "table": False}

def add_token(key: str, func: str = "bark", table: str = "user"):
    tables[table]['keys'].append(key)
    tables[table]['values'].append(func)

def kill_token(key: str, table: str = 'user'):
    # find that token!
    _i = tables[table]['keys'].index(key)

    # kill it and its little function too
    tables[table]['keys'].pop(_i)
    tables[table]['values'].pop(_i)



# 
# 
#  INIT
# 

## we need to import all the core functions
## and add them to the functions table

# build core tables from core tables
_core_keys = []
_core_values = []

for val in core_table:
    _core_keys.append(val['key'])
    _core_values.append({
        'func': val['func'],
        'runtime' : val['runtime']
    })

# add it to core tables
tables["core"]["keys"] += _core_keys
tables["core"]["values"] += _core_values