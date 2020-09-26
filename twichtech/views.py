from django.http import HttpResponse
import requests

def home(request):

    print(' ')
    print(' ')

    # Obtener  client-id y authorization creando Aplicación en https://dev.twitch.tv/console/apps
    # Luego hacer un POST como el siguiente para tener el TOKEN:
    # POST https://id.twitch.tv/oauth2/token?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&grant_type=client_credentials
    headers = {
        'client-id': 'CLIENT_ID',
        'Authorization': 'Bearer TOKEN_OBTENIDO',
    }

    # game_id = 509670 es la categoría: Ciencia y Tecnología
    params = (
        ('game_id', '509670'),
        ('language', 'es'),
    )

    response = requests.get('https://api.twitch.tv/helix/streams', headers=headers, params=params)

    streams = response.json()

    html = "<html><body><title>Twitch Tech</title>"
    html = html + "<h3>Vivos en Español de Ciencia y Tecnología en Twitch: </h3>"

    for stream in streams['data']:
        char = '🔴'
        if stream['title'][0] == char:
            title = stream['title'][1:]
        else:
            title = stream['title']
        
        html = html + "<span> 🔴 " + title + "</span> <br />"
        print(stream['user_name'] + ' ' + stream['title'])

    html = html + "</body></html>"

    #dump = json.dumps(streams)

    #return HttpResponse(html, content_type='application/json')
    return HttpResponse(html)