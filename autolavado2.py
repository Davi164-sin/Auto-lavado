from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return"""
     ```
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Planilla de Autolavado</title>
  <style>
    table {
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 10px;
    }
  </style>
</head>
<body>
  <h1>Planilla de Autolavado</h1>
  <form id="formulario">
    <label for="placa">Placa del vehículo:</label>
    <input type="text" id="placa" name="placa"><br><br>
    <label for="tipo_lavado">Tipo de lavado:</label>
    <select id="tipo_lavado" name="tipo_lavado">
      <option value="Basico">Básico</option>
      <option value="Completo">Completo</option>
      <option value="Premium">Premium</option>
    </select><br><br>
    <label for="fecha">Fecha:</label>
    <input type="date" id="fecha" name="fecha"><br><br>
    <button id="guardar">Guardar</button>
  </form>
  <h2>Lavadas registradas</h2>
  <table id="tabla_lavadas">
    <thead>
      <tr>
        <th>Placa</th>
        <th>Tipo de lavado</th>
        <th>Fecha</th>
      </tr>
    </thead>
    <tbody id="tbody_lavadas">
    </tbody>
  </table>
  <h2>Lavadas acumuladas por vehículo</h2>
  <table id="tabla_acumuladas">
    <thead>
      <tr>
        <th>Placa</th>
        <th>Cantidad de lavadas</th>
        <th>Lavador</th>
        <th>Lavadero</th>
      </tr>
    </thead>
    <tbody id="tbody_acumuladas">
    </tbody>
  </table>
  <h2>Ganancias</h2>
  <p>Lavador: <span id="ganancias_lavador">0</span></p>
  <p>Lavadero: <span id="ganancias_lavadero">0</span></p>

  <script>
    let lavadas = [];
    let acumuladas = {};
    const precioLavado = 10;

    document.getElementById('guardar').addEventListener('click', (e) => {
      e.preventDefault();
      const placa = document.getElementById('placa').value;
      const tipo_lavado = document.getElementById('tipo_lavado').value;
      const fecha = document.getElementById('fecha').value;

      lavadas.push({ placa, tipo_lavado, fecha });

      if (acumuladas[placa]) {
        acumuladas[placa]++;
      } else {
        acumuladas[placa] = 1;
      }

      actualizarTablas();
    });

    function actualizarTablas() {
      const tbodyLavadas = document.getElementById('tbody_lavadas');
      const tbodyAcumuladas = document.getElementById('tbody_acumuladas');

      tbodyLavadas.innerHTML = '';
      tbodyAcumuladas.innerHTML = '';

      lavadas.forEach((lavada) => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td>${lavada.placa}</td>
          <td>${lavada.tipo_lavado}</td>
          <td>${lavada.fecha}</td>
        `;
        tbodyLavadas.appendChild(row);
      });

      let totalLavador = 0;
      let totalLavadero = 0;

      Object.keys(acumuladas).forEach((placa) => {
        const cantidadLavadas = acumuladas[placa];
        const lavador = Math.floor(cantidadLavadas / 2);
        const lavadero = cantidadLavadas - lavador;

        totalLavador += lavador * precioLavado;
        totalLavadero += lavadero * precioLavado;

        const row = document.createElement('tr');
        row.innerHTML = `
          <td>${placa}</td>
          <td>${cantidadLavadas}</td>
          <td>${lavador}</td>
          <td>${lavadero}</td>
        `;
        tbodyAcumuladas.appendChild(row);
      });

      document.getElementById('ganancias_lavador').textContent = totalLavador;
      document.getElementById('ganancias_lavadero').textContent = totalLavadero;
    }
  </script

     """
if __name__ == "__main__":
    app.run(port=5003)
