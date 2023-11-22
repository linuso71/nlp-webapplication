import paralleldots
paralleldots.set_api_key('SFarLEyAecqCzn4eNqvbJwbrLKRugtqkTRpnsABxjOY')
def ner(text):
    ner = paralleldots.ner(text)
    return ner