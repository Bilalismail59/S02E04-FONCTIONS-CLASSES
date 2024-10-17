def hello():
    print('Hello from module A')

# pour signifier qu'un élément devrait PRIVÉ,
# on le préfixe par `_`
# ATTENTION la fonction n'est pas vraiment privée (!?!) :
# elle reste accessible dans main
def _private_func():
    print('Am I a private function?') # NON !