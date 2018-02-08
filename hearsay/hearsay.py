from giphypop import translate
import requests

def get_cat_gif():
    """Return Cat Gif URL"""
    cat_gif = translate('cat')
    return cat_gif

def get_cat_fact():
    """Retuns Cat Fact JSON"""
    cat_request = requests.get('https://catfact.ninja/fact')
    return cat_request.text

if __name__ == '__main__':
    gif = get_cat_gif()
    fact = get_cat_fact()
    print(gif)
    print(fact)
