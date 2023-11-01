import requests

class APITester:
    """
    APITester es una herramienta para probar APIs.
    Puede utilizarse para realizar solicitudes GET a una API y personalizar los parámetros y encabezados.
    """

    def __init__(self):
        """
        Inicializa una instancia de APITester.
        """
        self.api_url = ""
        self.params = {}
        self.headers = {}
        self.data = {}

    def set_api_url(self, url):
        """
        Establece la URL de la API que se va a probar.

        :param url: La URL de la API.
        :type url: str
        """
        self.api_url = url

    def add_param(self, key, value):
        """
        Agrega un parámetro a la solicitud.

        :param key: El nombre del parámetro.
        :type key: str

        :param value: El valor del parámetro.
        :type value: str
        """
        self.params[key] = value

    def add_header(self, key, value):
        """
        Agrega un encabezado a la solicitud.

        :param key: El nombre del encabezado.
        :type key: str

        :param value: El valor del encabezado.
        :type value: str
        """
        self.headers[key] = value

    def add_data(self, key, value):
        """
        Agrega un dato a la solicitud (por ejemplo, en una solicitud POST o PUT).

        :param key: El nombre del dato.
        :type key: str

        :param value: El valor del dato.
        :type value: str
        """
        self.data[key] = value

    def make_get_request(self):
        """
        Realiza una solicitud GET a la API con los parámetros y encabezados configurados.

        Imprime la respuesta en la consola.
        """
        try:
            # Realiza una solicitud GET a la API con parámetros y encabezados opcionales
            response = requests.get(self.api_url, params=self.params, headers=self.headers)

            if response.status_code == 200:
                print("Solicitud exitosa")
                print("Contenido de la respuesta:")
                print(response.text)

                # Si la API devuelve datos en formato JSON, puedes analizarlos
                try:
                    data = response.json()
                    print("Datos recibidos:")
                    print(data)
                except ValueError:
                    pass  # La respuesta no es JSON

                # Si deseas guardar la respuesta en un archivo
                with open('respuesta_api.json', 'w') as file:
                    file.write(response.text)
                    print("Respuesta guardada en 'respuesta_api.json'")

            else:
                print(f"Error en la solicitud: Código de respuesta {response.status_code}")

        except requests.exceptions.ConnectionError as e:
            print("Error de conexión:", e)
        except requests.exceptions.Timeout as e:
            print("Tiempo de espera agotado:", e)
        except requests.exceptions.RequestException as e:
            print("Error en la solicitud:", e)

    def send_put_request(self):
        """
        Realiza una solicitud PUT a la API con los parámetros, encabezados y datos configurados.

        Imprime la respuesta en la consola.
        """
        try:
            response = requests.put(self.api_url, json=self.data, headers=self.headers)

            if response.status_code == 200:
                print("Solicitud exitosa")
                print("Contenido de la respuesta:")
                print(response.text)

                # Si la API devuelve datos en formato JSON, puedes analizarlos
                try:
                    data = response.json()
                    print("Datos recibidos:")
                    print(data)
                except ValueError:
                    pass  # La respuesta no es JSON

                # Si deseas guardar la respuesta en un archivo
                with open('respuesta_api.json', 'w') as file:
                    file.write(response.text)
                    print("Respuesta guardada en 'respuesta_api.json'")

            else:
                print(f"Error en la solicitud: Código de respuesta {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")

    def send_post_request(self):
        """
        Realiza una solicitud POST a la API con los parámetros, encabezados y datos configurados.

        Imprime la respuesta en la consola.
        """
        try:
            response = requests.post(self.api_url, json=self.data, headers=self.headers)

            if response.status_code == 200:
                print("Solicitud exitosa")
                print("Contenido de la respuesta:")
                print(response.text)

                # Si la API devuelve datos en formato JSON, puedes analizarlos
                try:
                    data = response.json()
                    print("Datos recibidos:")
                    print(data)
                except ValueError:
                    pass  # La respuesta no es JSON

                # Si deseas guardar la respuesta en un archivo
                with open('respuesta_api.json', 'w') as file:
                    file.write(response.text)
                    print("Respuesta guardada en 'respuesta_api.json'")

            else:
                print(f"Error en la solicitud: Código de respuesta {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")

if __name__ == "__main__":
    print("Bienvenido al API Tester")
    url = input("Ingresa la URL de la API que deseas probar: ")

    tester = APITester()
    tester.set_api_url(url)

    request_type = input("Selecciona el tipo de solicitud (GET, POST, PUT, DELETE): ").upper()

    if request_type not in ("GET", "POST", "PUT", "DELETE"):
        print("Tipo de solicitud no válido.")
    else:
        while True:
            param_name = input("Ingrese el nombre del parámetro (o escriba 'terminar' para finalizar): ")
            if param_name.lower() == 'terminar':
                break
            param_value = input(f"Ingrese el valor para '{param_name}': ")
            tester.add_param(param_name, param_value)

        while True:
            header_name = input("Ingrese el nombre del encabezado (o escriba 'terminar' para finalizar): ")
            if header_name.lower() == 'terminar':
                break
            header_value = input(f"Ingrese el valor para '{header_name}': ")
            tester.add_header(header_name, header_value)

        if request_type in ("POST", "PUT"):
            while True:
                data_name = input("Ingrese el nombre del campo de datos (o escriba 'terminar' para finalizar): ")
                if data_name.lower() == 'terminar':
                    break
                data_value = input(f"Ingrese el valor para '{data_name}': ")
                tester.add_data(data_name, data_value)

        if request_type == "GET":
            tester.make_get_request()
        elif request_type == "POST":
            tester.send_post_request()
        elif request_type == "PUT":
            tester.send_put_request()
        else:
            print("Tipo de solicitud no válido.")