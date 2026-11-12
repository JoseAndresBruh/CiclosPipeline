import requests
def fetch_data(url):
    # Vulnerabilidad SAST: Uso de credenciales hardcodeadas
    response = requests.get(f"{url}?key={api_key}")
    return response.json()

# Cambio menor para validar el pipeline DevSecOps en un Pull Request.
