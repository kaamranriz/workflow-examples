"""
API Client - Code with various issues for review.
"""

import requests
import json
import time

API_KEY = "sk-1234567890abcdef"  # Hardcoded secret!
BASE_URL = "https://api.example.com"

def makeRequest(endpoint, method="GET", data=None):
    url = BASE_URL + endpoint
    headers = {"Authorization": "Bearer " + API_KEY}
    
    try:
        if method == "GET":
            r = requests.get(url, headers=headers)
        elif method == "POST":
            r = requests.post(url, headers=headers, json=data)
        elif method == "PUT":
            r = requests.put(url, headers=headers, json=data)
        elif method == "DELETE":
            r = requests.delete(url, headers=headers)
        else:
            return None
        
        return r.json()
    except:  # Bare except - bad practice
        return None

def fetchUser(userId):
    return makeRequest(f"/users/{userId}")

def fetchUsers(page=1, limit=10):
    return makeRequest(f"/users?page={page}&limit={limit}")

def createUser(data):
    return makeRequest("/users", "POST", data)

def updateUser(userId, data):
    return makeRequest(f"/users/{userId}", "PUT", data)

def deleteUser(userId):
    return makeRequest(f"/users/{userId}", "DELETE")

def bulkFetch(ids):
    results = []
    for id in ids:
        # No rate limiting - could overwhelm API
        # No parallelization - slow for many IDs
        result = fetchUser(id)
        results.append(result)
    return results

def retryRequest(endpoint, maxRetries=3):
    for i in range(maxRetries):
        result = makeRequest(endpoint)
        if result:
            return result
        time.sleep(1)  # Fixed delay - no exponential backoff
    return None

class APIClient:
    def __init__(self, key=None):
        self.key = key or API_KEY  # Falls back to hardcoded key
        self.cache = {}
    
    def get(self, endpoint):
        # Simple cache with no expiration
        if endpoint in self.cache:
            return self.cache[endpoint]
        result = makeRequest(endpoint)
        self.cache[endpoint] = result
        return result
    
    def clearCache(self):
        self.cache = {}
    
    def batchGet(self, endpoints):
        return [self.get(e) for e in endpoints]


