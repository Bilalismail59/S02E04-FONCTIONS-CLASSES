"""
my_project/
│
├── main.py 
├── module_a.py
└── module_b
    ├── submodule_a.py
    └── submodule_b.py
"""

# importe le module A
import module_a

# importe la fonction `hello` du module A
from module_a import hello


# importe le submodule A du module B
# le `.` nous permet de progreeser entre les dossiers et fichiers
import module_b.submodule_a # chemin absolu
# from module_b.submodule_b import hello # ATTENTION remplace le précédent `hello`
from module_b.submodule_b import hello as hello_b # renomme hello en hello_b


# importe tout le module B (submodule A + submodule B)
import module_b

print('Hello from MAIN')

# appel de `hello` du module A
module_a.hello()
module_a._private_func()

# appel de `hello` du module A (via FROM module IMPORT fonction)
hello()

# appeler `hello` du sous-module A
module_b.submodule_a.hello()
hello_b()

module_b.hello()
module_b.hello_b()

module_b._must_be_private()