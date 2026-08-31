import requests
from config import API_BASE_URL, API_TIMEOUT

class APIClient:
    def __init__(self, base_url=API_BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None
    
    def set_token(self, token):
        """Establece el token de autenticación"""
        self.token = token
        self.session.headers.update({'Authorization': f'Bearer {token}'})
    
    def get(self, endpoint, params=None):
        """Realiza una petición GET"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.get(url, params=params, timeout=API_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error en GET {url}: {e}")
            return None
    
    def post(self, endpoint, data=None):
        """Realiza una petición POST"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.post(url, json=data, timeout=API_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error en POST {url}: {e}")
            return None
    
    def put(self, endpoint, data=None):
        """Realiza una petición PUT"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.put(url, json=data, timeout=API_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error en PUT {url}: {e}")
            return None
    
    def delete(self, endpoint):
        """Realiza una petición DELETE"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.delete(url, timeout=API_TIMEOUT)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error en DELETE {url}: {e}")
            return False
