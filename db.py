import json

def connect(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}
    
def content(conn, name=None, value=None):
    conn[name] = value
    return conn

def save(conn, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(conn, f, ensure_ascii=False, indent=2)

