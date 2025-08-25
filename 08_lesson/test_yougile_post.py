import requests

def test_create_project():
    headers = {
        'Authorization': 'Bearer -vhWR+SnGtkHyd25ESxQLloFcqIr2J8j18mI4tNwmSd8mWHnHpPE90wLGzYlmV09',
        'Content-Type': 'application/json'
    }

    body = {
          "title" : "Учёба3"
    }

    response = requests.post('https://ru.yougile.com/api-v2/projects', headers=headers, json=body)
    print(response.json())