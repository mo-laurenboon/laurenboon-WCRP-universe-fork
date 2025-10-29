"""
This scripts uses both pyld and RDFlib to extract tuples from JSON-LD files without the need for framing. It then issues example queries to each method and compares their output.
"""

from pyld import jsonld
import json
from rdflib import Graph
