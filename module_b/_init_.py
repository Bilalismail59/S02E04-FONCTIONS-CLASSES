# sert de chef d'orchestre pour lister les sous-modules
# et « aplatir » les namespaces (éviter `mod.sub.subsub`)

# on peut importer tout le sous-module et/ou une fonction précise

from .submodule_a import * # j'importe tout
from .submodule_b import hello as hello_b # chemin relatif