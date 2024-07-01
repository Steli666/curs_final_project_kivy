import requests
from kivy.storage.jsonstore import JsonStore

token_store = JsonStore('package.json')

def logout(instance):
    url = "http://127.0.0.1:8000/api/logout"
    try:
        headers = {'content-type': 'application/json',
                   "authorization": token_store.get("vars")["token"]
                   }
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            token_store.put("vars", token="")
            instance.update_right_action_items()
        else:
            print("Failed to fetch sessions. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred while fetching sessions:", str(e))