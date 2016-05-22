import requests as rq
import webbrowser
import urllib.parse as urlparse
import vk
import vk_api

# id of vk.com application, that has access to audio
APP_ID = '5474337'
# chars to exclude from filename
FORBIDDEN_CHARS = '/\\\?%*:|"<>!'

access_token = user_id = ""
vkapi = ""

def get_auth_params():
    auth_url = ("https://oauth.vk.com/authorize?client_id={app_id}"
        "&scope=wall,audio&redirect_uri=http://oauth.vk.com/blank.html"
        "&display=page&response_type=token".format(app_id=APP_ID))
    webbrowser.open_new_tab(auth_url)
    redirected_url = input("Paste here url you were redirected:\n")
    aup = urlparse.parse_qs(redirected_url)
    aup['access_token'] = aup.pop(
        'https://oauth.vk.com/blank.html#access_token')
    return aup['access_token'][0], aup['user_id'][0]

def auth_to_vk():
    global vkapi, access_token, user_id
    access_token, user_id = get_auth_params()
    session = vk.Session(access_token=access_token)
    vkapi = vk.API(session = session)


def uploadSongs(path="music/"):

    auth_to_vk()
    upload_url = vkapi.audio.getUploadServer(access_token=access_token)['upload_url']
    files = {
            'access_token':access_token,
             'file': open('music/1SecondVideo.mp3', 'rb')}
    r = rq.post(upload_url, files = files)
    j = r.json()
    print(j)
    print(vkapi.audio.save(server=j['server'], audio=j['audio'], hash=j['hash'],
                           title="asd", artist="as", audio_hash="123", gid=0, access_token=access_token))

if (__name__ == "__main__"):
    uploadSongs()

