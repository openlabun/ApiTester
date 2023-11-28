<template>
  <div class="card text-center m-3">
    <v-responsive class="mx-auto" max-width="344">
      <!-- Select para los métodos -->
      <select v-model="selectedMethod">
        <option value="GET">GET</option>
        <option value="PUT">PUT</option>
        <option value="POST">POST</option>
        <option value="DELETE">DELETE</option>
      </select>
      <!-- Input para la URL -->
      <input :value="url" @input="updateUrl" placeholder="https://example.com" />
      
      <!-- Pestañas para Query Params y Request Body -->
      <div>
        <button @click="activeTab = 'queryParams'">Query Params</button>
        <button @click="activeTab = 'requestBody'">Body</button>
      </div>

      <!-- Contenido de la pestaña activa -->
      <div v-if="activeTab === 'queryParams'">
        <!-- Input para los parámetros de consulta -->
        <input :value="queryParams" @input="updateQueryParams" placeholder="param1=value1&param2=value2" />
      </div>
      <div v-if="activeTab === 'requestBody'">
        <!-- Textarea para el cuerpo de la solicitud -->
        <textarea :value="requestBody" @input="updateRequestBody" placeholder="Request Body"></textarea>
      </div>

      <!-- Botón para enviar -->
      <button @click="request" :disabled="isRequesting">Send</button>
      <!-- Resultado de la solicitud -->
      <pre v-if="totalVuePackages">Respond: <br>{{ JSON.stringify(totalVuePackages, null, 2) }}</pre>
      <pre v-else class="placeholder">Respond Body</pre>
    </v-responsive>

  </div>
</template>


<script>
export default {
  name: "http-request",
  data() {
    return {
      url: "", // Para almacenar la URL
      queryParams: "", // Para almacenar los parámetros de consulta
      requestBody: "", // Para almacenar el cuerpo de la solicitud
      selectedMethod: "GET", // Para almacenar el método seleccionado
      totalVuePackages: null,
      activeTab: "queryParams", // Inicialmente mostrar la pestaña de Query Params
      isRequesting: false,
    };
  },

  
  methods: {
    updateUrl(event) {
      this.url = event.target.value;
    },
    updateQueryParams(event) {
      this.queryParams = event.target.value;
    },
    updateRequestBody(event) {
      this.requestBody = event.target.value;
    },
    request() {
      this.isRequesting = true;
      // Construir la URL con los parámetros de consulta solo si los parámetros están vacíos
      const urlWithParams = this.queryParams ? `${this.url}?${this.queryParams}` : this.url;
      fetch(urlWithParams, {
        method: this.selectedMethod,
        body: this.selectedMethod === "GET" ? undefined : this.requestBody, // No incluir body en solicitudes GET
      })


      //Manejo de errores
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => (this.totalVuePackages = data))
    .catch((error) => {
      console.error("There was an error!", error);
      // Mostrar mensaje de error al usuario
      alert("Hubo un error en la solicitud. Por favor, verifica la URL y los parámetros.");
    })
        .finally(() => {
          this.isRequesting = false; // Deshabilitar el indicador de solicitud al finalizar
        });
    },
  },
};
</script>