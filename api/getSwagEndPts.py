import json

def list_endpoints(openapi_file):
    """
    Lists all endpoints and their HTTP methods from an OpenAPI JSON file.

    Args:
        openapi_file (str): Path to the OpenAPI JSON file.
    """
    try:
        with open(openapi_file, 'r', encoding='utf-8') as f:
            api_spec = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return
    except FileNotFoundError:
        print(f"File not found: {openapi_file}")
        return

    # Ensure 'paths' is in the API specification
    if 'paths' not in api_spec:
        print("No 'paths' section found in the OpenAPI specification.")
        return

    paths = api_spec['paths']

    # print("List of Endpoints and Supported HTTP Methods:")
    for path, methods in paths.items():
        for method in methods.keys():
            # Filter out non-standard HTTP methods if necessary
            method_upper = method.upper()
            print(f"{method_upper} {path}")

if __name__ == "__main__":
    # Replace 'openapi.json' with the path to your OpenAPI JSON file
    openapi_file_path = '/home/bikeride/dockerK8s/VAmPI/openapi_specs/openapi3.yml'
    list_endpoints(openapi_file_path)
