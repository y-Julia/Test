import requests

# Replace with your personal access token
access_token = "access_token"

# Replace with your username
username = 'username'

# Set up proxy information
proxy_host = 'http://XXX.XX.X'
proxy_port = 'XXXX'
proxies = {
    'http': f'{proxy_host}:{proxy_port}',
    'https': f'{proxy_host}:{proxy_port}'
}

# Get a list of all repositories owned by the user
url = f'https://api.github.com/users/{username}/repos'
headers = {'Authorization': f'token {access_token}'}
response = requests.get(url, headers=headers, proxies=proxies)
# Delete each repository
for repo in response.json():
    url = f'https://api.github.com/repos/{username}/{repo["name"]}'
    response = requests.delete(url, headers=headers, proxies=proxies)
    # print(response)
    if response.status_code == 204:
        print(f'{repo["name"]} deleted successfully')
    else:
        print(f'Error deleting {repo["name"]}: {response.status_code}')
