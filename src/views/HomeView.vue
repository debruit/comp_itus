<template>
  <div class="background">
    <div class="visor">
      <b-form @reset="onReset">
        <b-form-group id="input-group-1" label="Campaña" label-for="input-1">
          <b-form-select
            id="input-1"
            v-model="actual_campaign"
            :options="campaigns"
            required
          ></b-form-select>
        </b-form-group>

        <b-form-group label="Archivo" v-slot="{ ariaDescribedby }">
          <div id="preview">
            <b-form-radio
              v-model="tipo_archivo"
              :aria-describedby="ariaDescribedby"
              value="predefinido"
              >Archivo predefinido</b-form-radio
            >

            <img v-if="url" :src="url" />
            <b-link @click="openFile"> {{ filename }}</b-link>
          </div>

          <b-form-radio
            v-model="tipo_archivo"
            :aria-describedby="ariaDescribedby"
            value="local"
            >Seleccionar archivo</b-form-radio
          >
          <div v-if="archivoLocal">
            <input type="file" id="file-small" @change="createURL" />
            <div id="preview">
              <img v-if="url" :src="url" />
              <b-link @click="openFile"> {{ filename }}</b-link>
            </div>
          </div>
        </b-form-group>

        <b-form-group label="Medio de envío" v-slot="{ ariaDescribedby }">
          <b-form-radio
            v-model="tipo_envio"
            :aria-describedby="ariaDescribedby"
            value="email"
            >Email</b-form-radio
          >
          <b-form-radio
            v-model="tipo_envio"
            :aria-describedby="ariaDescribedby"
            value="whatsapp"
            >WhatsApp</b-form-radio
          >
          <b-form-radio
            v-model="tipo_envio"
            :aria-describedby="ariaDescribedby"
            value="sms"
            >SMS</b-form-radio
          >
          <div v-if="tipo_envio">
            <div v-if="tipo_envio === 'email'">
              <b-form-input
                v-model="email_destino"
                type="email"
                placeholder="Ingrese el email del destinatario"
                required
              ></b-form-input>
              <b-form-textarea
                v-model="mensaje_envio"
                placeholder="Enter something..."
                rows="3"
                max-rows="6"
              ></b-form-textarea>
            </div>
            <div v-else>
              <b-form-input
                v-model="numero_destino"
                type="number"
                placeholder="Ingrese el número del destinatario"
                required
              ></b-form-input>
              <b-form-textarea
                v-model="mensaje_envio"
                placeholder="Enter something..."
                rows="3"
                max-rows="6"
              ></b-form-textarea>
            </div>
          </div>
        </b-form-group>

        <b-button v-b-modal.confirmacion variant="primary">Enviar</b-button>
        <b-modal id="confirmacion" title="Confirmación del envío">
          <p class="my-4">Esta seguro de hacer el envío?</p>
        </b-modal>
        <b-button type="reset" variant="danger">Cancelar</b-button>
      </b-form>
    </div>
  </div>
</template>

<script>
import { ref, watch } from "vue";
import {
  obtenerCampañas,
  obtenerInfo,
  enviarMensaje,
} from "../services/CampañaService";

export default {
  setup() {
    const campaigns = ref([{ text: "Seleccionar campaña", value: null }]);
    const actual_campaign = ref(""); // Campaña seleccionada

    const tipo_archivo = ref("");
    const tipo_envio = ref("");

    const archivoLocal = ref(false);

    const url = ref("");
    const filename = ref("");

    const email_destino = ref("");  // Email del destinatario
    const numero_destino = ref("");   // Número de destinatario
    const asunto = ref(""); // Asunto del mensaje
    const mensaje_envio = ref(""); // Mensaje a enviar

    obtenerCampañas().then((response) => {
      response.forEach((campaign) => {
        campaigns.value.push({
          text: campaign.nombre,
          value: campaign.id,
        });
      });
    });

    watch(actual_campaign, (id) => {
      if (id) {
        obtenerInfo(id).then((response) => {
          console.log(response);
          asunto.value = response.asunto;
          mensaje_envio.value = response.mensaje;
          url.value = URL.createObjectURL(response.documento);
        });
      }
    });

    watch(tipo_archivo, (value) => {
      if (value === "predefinido") {
        archivoLocal.value = false;
      } else {
        archivoLocal.value = true;
      }
    });

    const createURL = (e) => {
      const file = e.target.files[0];
      filename.value = file.name; // update filename
      url.value = URL.createObjectURL(file); // create URL
      console.log(url.value);
    };

    const openFile = () => {
      window.open(url.value, "_blank").focus();
    };

    const onSubmit = () => {
      alert(JSON.stringify(form.value, null, 2));
    };

    const onReset = () => {
      tipo_envio.value = "";
      tipo_archivo.value = "";
      archivoLocal.value = false;
      url.value = "";
      filename.value = "";
      asunto.value = "";
      mensaje_envio.value = "";
    };

    return {
      campaigns,  // Campañas disponibles
      actual_campaign,  // Campaña seleccionada
      tipo_archivo, // Tipo de archivo a seleccionar
      tipo_envio, // Tipo de envío
      onSubmit, // Evento de envío
      onReset,  // Resetear formulario
      archivoLocal, // Flag para seleccionar archivo local
      url,  // URL del archivo a enviar
      email_destino,  // Email del destinatario
      numero_destino, // Número de destinatario
      asunto, // Asunto del mensaje
      mensaje_envio,    // Mensaje a enviar
      createURL,  // Función para crear URL del archivo a enviar
      filename, // Nombre del archivo a enviar
      openFile, // Función para abrir archivo en nueva ventana
    };
  },
};
</script>

<style>
.background {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-image: url(../assets/itus_back.jpeg);
}
.visor {
  width: 50%;
  max-width: 500px;
  background-color: #fff;
  border-radius: 4px;
  padding: 1rem;
}

#preview {
  display: inline-block;
  justify-content: center;
  align-items: center;
}

#preview img {
  max-width: 100%;
  max-height: 50px;
}
</style>