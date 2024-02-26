""" L'ojectif c'est de lire/écire un nombre scientifique depuis un JSon
	Le format décimal n'est pas facile à lire par l'humain: '1000000000'

	Copilot : Lors de l'écriture les nombres sont convertis en notation décimale ...
 	Si vous voulez écrire un nombre en notation scientifique dans un fichier JSON à l’aide de Python,
 	vous pouvez le faire en le stockant comme une chaîne de caractères.

	L'utilisateur doit pouvoir écrire le nombre de façon scientifique dans le JSon soit en str soit en float
	Copilot propose de faire .replace(".", ",")  à chaque fois mais moi je mets toujours un '.' à la place de la ','

	write_json_file filter to have reading string in JSon
"""
import json
from collections.abc import Mapping, Sequence

file_json_name = 'json-test.json'

data = None

# ----------------------------------------------------------------------------
# That's just horrible !!!
# https://stackoverflow.com/questions/50700585/write-json-float-in-scientific-notation
# d'après les commentaires en plus ça ne fonctionne pas
#
class ScientificNotationEncoder(json.JSONEncoder):
    def iterencode(self, o, _one_shot=False):
        if isinstance(o, float):
            return "{:e}".format(o)
        elif isinstance(o, Mapping):
            return "{{{}}}".format(', '.join('"{}" : {}'.format(str(ok), self.iterencode(ov))
                                             for ok, ov in o.items()))
        elif isinstance(o, Sequence) and not isinstance(o, str):
            return "[{}]".format(', '.join(map(self.iterencode, o)))
        return ', '.join(super().iterencode(o, _one_shot))

# ----------------------------------------------------------------------------

def _filter_read_list( item_list ):
	for item in item_list:
		if isinstance(item["nombre_scientifique"], str):
			# Convert string to number
			item["nombre_scientifique"] = float( item["nombre_scientifique"] )
    
def read_json_file():
	try:
		with open( file_json_name, 'r' ) as file_json:
			data_json = json.load( file_json )
		# filter nombre_scientifique
		_filter_read_list( data_json )
		return data_json
	except FileNotFoundError:
		return None
	except json.JSONDecodeError:
		return None

def _filter_write_list( item_list ):
	# filter nombre_scientifique avant d'écrire
	for item in item_list:
		if abs( item["nombre_scientifique"] ) > 1e+6 > isinstance(item["nombre_scientifique"], (int, float)):
			# Convert number into string
			item["nombre_scientifique"] = "{:.2e}".format(item["nombre_scientifique"])
   
def write_json_file( item_list ):
	_filter_write_list( item_list )
	try:
		with open( file_json_name, 'w' ) as file_json:
			json.dump( item_list, file_json, indent=4 )  # tabulation identation is 4
	except FileNotFoundError:
		return None
	except json.JSONDecodeError:
		return None  

# There must be an Item with "NAME"
def get_item_by_name( name, list_item ):
	for item in list_item:
		if item['NAME'] == name:
			return item
	return None

# ----------------------------------------------------------------------------

# Read Json File 
#
data = read_json_file()

# Display value in json file
#
my_item1 = get_item_by_name('Item1', data)

if my_item1 is None:
    print('NO DATA')
    exit()

# Get ns1
#
ns1 = my_item1['nombre_scientifique']

ns1_formated = "{:.2e}".format(ns1)

print(ns1) # lecture du JSon : les nombres sont automatiquement convertis en notation décimale standard.
print( f"nombre_scientifique: {ns1_formated}" )

# 1230000.0
# nombre_scientifique: 1.23e+06

# Get ns2
#
my_item2 = get_item_by_name('Item2', data)
ns2 = my_item2['nombre_scientifique']
print(ns2)

# set new value
ns2 = 0.56E+06 # et là je ne modifie pas data
print(ns2)

# je reprends ns2 du fichier JSon
ns2 = my_item2['nombre_scientifique']

# make calculation
add = ns1 + ns2

print( f"add: {add}" )

# Get AddItem to save result
#
item_added = get_item_by_name('AddItem', data)

item_added['nombre_scientifique'] = add

# Finaly write the result
#
write_json_file( data )


