from requests import get
def get_user(user):
    url = 'https://api.github.com/users/' + user
    a = get(url)
    b = a.json()
    return b['avatar_url']
