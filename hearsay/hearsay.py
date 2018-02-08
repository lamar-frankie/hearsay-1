from giphypop import translate

def get_cat_gif():
    """Return Cat Gif URL"""
    cat_gif = translate('cat')
    return cat_gif

def get_cat_fact():
    """Retuns Cat Fact JSON"""
    cat_request = requests.get('https://catfact.ninja/fact')
    return r.text

if __name__ == '__main__':
    cat_gif = get_cat_gif()
    cat_fact = get_cat_fact()
    print(cat_gif)
    print(fact_fact)
