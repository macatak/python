# takes a Swagger/OpenAPI spec and generate a wordlist
# of all the available endpoint
# useful for kiterunner, feroxbuster, etc.

import json
import yaml
import os

def load_openapi_spec(openapi_file):
    """
    Loads an OpenAPI specification from a JSON or YAML file.

    Args:
        openapi_file (str): Path to the OpenAPI file.

    Returns:
        dict: The OpenAPI specification as a dictionary.
    """
    _, ext = os.path.splitext(openapi_file)
    try:
        with open(openapi_file, 'r', encoding='utf-8') as f:
            if ext.lower() in ['.yaml', '.yml']:
                return yaml.safe_load(f)
            elif ext.lower() == '.json':
                return json.load(f)
            else:
                print("Unsupported file extension. Please provide a JSON or YAML file.")
                return None
    except Exception as e:
        print(f"Error loading OpenAPI specification: {e}")
        return None

def list_endpoints(openapi_file, output_file='vampiWordLst.kite'):
    """
    Lists all endpoints and their HTTP methods from an OpenAPI file and saves them to a file.

    Args:
        openapi_file (str): Path to the OpenAPI JSON or YAML file.
        output_file (str): Path to the output file where endpoints will be saved.
    """
    api_spec = load_openapi_spec(openapi_file)
    if not api_spec or 'paths' not in api_spec:
        print("Invalid OpenAPI specification.")
        return

    paths = api_spec['paths']

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for path, methods in paths.items():
                for method in methods.keys():
                    method_upper = method.upper()
                    f.write(f"{method_upper} {path}\n")
        print(f"Endpoints have been saved to '{output_file}'.")
    except Exception as e:
        print(f"Error writing to output file '{output_file}': {e}")

if __name__ == "__main__":
    # Replace with the path to your OpenAPI JSON or YAML file
    openapi_file_path = '/home/bikeride/dockerK8s/VAmPI/openapi_specs/openapi3.yml'  # or 'openapi.json'
    list_endpoints(openapi_file_path)
