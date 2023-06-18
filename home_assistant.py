import requests

url = 'http://homeassistant.local:8123'
unlock_url = f'{url}/api/services/lock/unlock'

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmMzU3ODhiY2RhYWY0NWMyODBjNzQ1MGUwNmFjZTYxNyIsImlhdCI6MTY4NTEwNjYxOSwiZXhwIjoyMDAwNDY2NjE5fQ.5uRTGoFe7IR4AFOBOJTQr4fS_pccXgW7Yis3xrdq74Y'

headers = {'Authorization': f'Bearer {token}'}


def unlock():
    requests.post(unlock_url, headers=headers, json={'entity_id': 'lock.smartlock'})
