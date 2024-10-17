def hello():
    _must_be_private()
    print('Hello from module B > submodule A')


# pour signifier qu'un élément devrait PRIVÉ,
# on le préfixe par `_`
# ATTENTION la fonction n'est pas vraiment privée (!?!) :
# elle reste accessible dans main
def _must_be_private():
    print('I really want to be private') # NON !