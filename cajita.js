function recargar() {
    window.location = "";
  }
  
  var numero = parseInt(prompt("introduce un numero"));
  if (numero < 1 || numero > 10) {
    alert('El número debe estar entre 1 y 10')
    recargar();
  }
  
  window.onload = function () {
    var caja = document.getElementById("micuadro");
    var cajato = caja.getContext("2d");
    var colores = [
      "#ffadad",
      "#ffd6a5",
      "#fdffb6",
      "#caffbf",
      "#9bf6ff",
      "#a0c4ff",
      "#bdb2ff",
      "#ffc6ff",
      "#666666",
      "#000000",
    ];
    var indice = numero - 1;
    cajato.fillStyle = colores[indice];
    cajato.fillRect(100, 100, 50, 50);
  };