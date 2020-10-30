from requests import get
def download_avatar(user, filename):
    githuburl = 'https://api.github.com/users/' + user
    get_githuburl = get(githuburl)
    json_data = get_githuburl.json()
    response = get(json_data['avatar_url'])
    if response.status_code == 200:
        with open(filename, 'wb') as image:
            image.write(response.content)