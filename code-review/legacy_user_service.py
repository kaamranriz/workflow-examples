"""
User Service - Legacy code that needs review and improvement.
This file intentionally has code quality issues for the AI Code Review workflow.
"""

import hashlib
import re
from datetime import datetime

users = {}  # Global state - bad practice

def createUser(email, pwd, name):
    # No input validation
    # No docstring
    # Poor variable names
    id = len(users) + 1
    h = hashlib.md5(pwd.encode()).hexdigest()  # MD5 is insecure for passwords
    users[id] = {'email': email, 'password': h, 'name': name, 'created': str(datetime.now())}
    return id

def getUser(id):
    if id in users:
        return users[id]
    return None  # No error handling

def updateUser(id, data):
    if id in users:
        for k in data:
            users[id][k] = data[k]  # No validation of what fields can be updated
        return True
    return False

def deleteUser(id):
    if id in users:
        del users[id]
        return True
    return False

def authenticate(email, pwd):
    h = hashlib.md5(pwd.encode()).hexdigest()
    for id, u in users.items():
        if u['email'] == email and u['password'] == h:
            return id
    return None

def validateEmail(e):
    # Oversimplified email validation
    if '@' in e:
        return True
    return False

def getAllUsers():
    # Returns passwords too - security issue!
    return list(users.values())

def searchUsers(q):
    result = []
    for id, u in users.items():
        if q.lower() in u['name'].lower() or q.lower() in u['email'].lower():
            result.append(u)
    return result

def changePassword(id, oldPwd, newPwd):
    if id not in users:
        return False
    h = hashlib.md5(oldPwd.encode()).hexdigest()
    if users[id]['password'] != h:
        return False
    # No password strength validation
    users[id]['password'] = hashlib.md5(newPwd.encode()).hexdigest()
    return True

class UserStats:
    def __init__(self):
        pass
    
    def getStats(self):
        s = {}
        s['total'] = len(users)
        s['emailDomains'] = {}
        for id, u in users.items():
            d = u['email'].split('@')[1] if '@' in u['email'] else 'unknown'
            if d in s['emailDomains']:
                s['emailDomains'][d] += 1
            else:
                s['emailDomains'][d] = 1
        return s


