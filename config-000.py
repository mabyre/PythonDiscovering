import os
import debug.func as dbg
import json

def read_configuration( file_name ):
    dbg.print( 'Config file:', os.path.abspath(file_name) )
    try:
        with open( file_name, 'r' ) as fichier:
            configuration = json.load(fichier)
        return configuration
    except FileNotFoundError:
        print("Configuration file \'config.json\' not found.")
        return None
    except json.JSONDecodeError:
        print("ERROR: JSON decoding error in configuration file.")
        return None

def main():
    configuration_file = "config.json" # Config file name
    
    # Reading the configuration
    configuration = read_configuration(configuration_file)
    
    if configuration:
        # Using configuration settings
        parametre1 = configuration.get("parametre1", "valeur_par_defaut_pour_parametre1")
        parametre2 = configuration.get("parametre2", 0)
        parametre3 = configuration.get("parametre3", False)
        parametre_tableau = configuration.get("parametre_tableau", ["valeur1", "valeur2"])
        
        # Your program uses the settings here
        print("Paramètre 1:", parametre1)
        print("Paramètre 2:", parametre2)
        print("Paramètre 3:", parametre3)
        print("Paramètre tableau:", parametre_tableau)
    else:
        # Error
        print("Unable to read configuration. Using default values.")

if __name__ == "__main__":
    main()
