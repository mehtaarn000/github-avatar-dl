from get_user import get_user
from requests import get
def download_avatar(user, filename):
    imageurl = get_user(user=user)
    response = get(imageurl)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)