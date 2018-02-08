from giphypop import translate
from hearsay import hearsay

def get_cat_gif():
    cat_gif = translate('cat')
    return cat_gif

def get_cat_fact():
    r = requests.get('https://catfact.ninja/fact')
    return r.text
    
if __name__ == '__main__':
    cat = get_cat_gif()
    fact = get_cat_fact()
    print(cat)
    print(fact)
