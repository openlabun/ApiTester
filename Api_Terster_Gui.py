import tkinter as tk
import requests

class APITesterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("API Tester")

        self.api_url_label = tk.Label(root, text="URL de la API:")
        self.api_url_label.pack()
        self.api_url_entry = tk.Entry(root)
        self.api_url_entry.pack()

        self.params_label = tk.Label(root, text="Parámetros (nombre:valor):")
        self.params_label.pack()
        self.params_entry = tk.Entry(root)
        self.params_entry.pack()

        self.headers_label = tk.Label(root, text="Encabezados (nombre:valor):")
        self.headers_label.pack()
        self.headers_entry = tk.Entry(root)
        self.headers_entry.pack()

        self.data_label = tk.Label(root, text="Datos (nombre:valor):")
        self.data_label.pack()
        self.data_entry = tk.Entry(root)
        self.data_entry.pack()

        self.method_label = tk.Label(root, text="Método:")
        self.method_label.pack()

        self.method_var = tk.StringVar()
        self.method_var.set("GET")

        self.get_radio = tk.Radiobutton(root, text="GET", variable=self.method_var, value="GET")
        self.get_radio.pack()

        self.post_radio = tk.Radiobutton(root, text="POST", variable=self.method_var, value="POST")
        self.post_radio.pack()

        self.put_radio = tk.Radiobutton(root, text="PUT", variable=self.method_var, value="PUT")
        self.put_radio.pack()

        self.delete_radio = tk.Radiobutton(root, text="DELETE", variable=self.method_var, value="DELETE")
        self.delete_radio.pack()

        self.submit_button = tk.Button(root, text="Enviar Solicitud", command=self.send_request)
        self.submit_button.pack()

        self.response_label = tk.Label(root, text="Respuesta:")
        self.response_label.pack()
        self.response_text = tk.Text(root, height=10, width=40)
        self.response_text.pack()

    def send_request(self):
        api_url = self.api_url_entry.get()
        method = self.method_var.get()
        params = self.params_entry.get()
        headers = self.headers_entry.get()
        data = self.data_entry.get()

        params_dict = {}
        headers_dict = {}
        data_dict = {}

        for param in params.split("\n"):
            if param.strip():
                key, value = param.split(":")
                params_dict[key.strip()] = value.strip()

        for header in headers.split("\n"):
            if header.strip():
                key, value = header.split(":")
                headers_dict[key.strip()] = value.strip()

        for item in data.split("\n"):
            if item.strip():
                key, value = item.split(":")
                data_dict[key.strip()] = value.strip()

        try:
            if method == "GET":
                response = requests.get(api_url, params=params_dict, headers=headers_dict)
            elif method == "POST":
                response = requests.post(api_url, json=data_dict, headers=headers_dict)
            elif method == "PUT":
                response = requests.put(api_url, json=data_dict, headers=headers_dict)
            elif method == "DELETE":
                response = requests.delete(api_url, params=params_dict, headers=headers_dict)
            else:
                self.response_text.delete(1.0, tk.END)
                self.response_text.insert(tk.END, "Método no válido")
                return

            self.response_text.delete(1.0, tk.END)
            self.response_text.insert(tk.END, response.text)

        except requests.exceptions.RequestException as e:
            self.response_text.delete(1.0, tk.END)
            self.response_text.insert(tk.END, f"Error en la solicitud: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = APITesterGUI(root)
    root.mainloop()