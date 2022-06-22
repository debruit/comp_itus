let url = 'http://localhost:3000'

export async function obtenerCampañas() {

    const response = await fetch(url+'/campaigns');
    return await response.json();
}

export async function obtenerInfo(id) {

    const response = await fetch(url+'/campaigns/'+id);
    return await response.json();
}

export async function enviarMensaje(data) {
    const response = await fetch(url+`/api/mensaje`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({archivo: data.archivo, destinatario: data.destinatario, mensaje: data.mensaje})
      })
    return await response.json();
}