import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= "a8c1e456dd204cc69636da61ac31fa12",
        client_secret="34a172d4e54443eaab196e26f9bf687a",
        show_dialog=True,
        cache_path="token.txt",
        username="Minhthaiha", 
    )
)
user_id = sp.current_user()["id"]


