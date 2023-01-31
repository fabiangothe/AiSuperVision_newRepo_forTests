"""Sphinx configuration file."""
import os
import sys

# add example module to the python path
# ist in GitHub im original so drin, aber geht auch ohne, warum???
#sys.path.insert(0, os.path.dirname(__file__))

#die folgenden Zeilen waren nur zum Ausprobieren
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
#sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath('.')), 'example'))
#sys.path.insert(0, os.path.dirname(os.path.abspath("../")))
#sys.path.insert(0, os.path.join(os.path.abspath("../"), 'example'))



extensions = ['sphinx_sqlalchemy', 'sphinxcontrib.sadisp', 'sphinx.ext.inheritance_diagram', 'sqlalchemyviz', 'graphviz']

html_theme = "furo"

#following is added for sphinxcontrib-sadisplay according to: https://github.com/sphinx-contrib/sadisplay
plantuml = 'java -jar plantuml.jar'.split()
graphviz = 'dot -Tpng'.split()
sadisplay_default_render = 'plantuml'


