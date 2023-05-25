import WebSocket from 'ws';

const socket = new WebSocket('ws://localhost:8765');

socket.onopen = function(e) {
  console.log('Conexión establecida ...');
  socket.send("Hola servidor!");
  
};

socket.onmessage = function(event) {
  console.log('Mensaje recibido: %s', event.data);
};

socket.onclose = function(event) {
  if (event.wasClean) {
    console.log('Conexión cerrada limpiamente, código=%s motivo=%s', event.code, event.reason);
  } else {
    // ej. El proceso del servidor se detuvo o la red está caída
    // event.code es usualmente 1006 en este caso
    console.log('La conexión se cayó!');
  }
};

socket.onerror = function(error) {
  console.log('%s', error);
};