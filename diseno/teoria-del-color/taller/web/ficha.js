const elemento = id => document.getElementById(id);
const referencia = elemento('referencia');
const registrar = elemento('registrar');
let animales = 50;

elemento('modo').addEventListener('change', event => {
  document.documentElement.style.colorScheme = event.target.value;
});

function actualizarBoton() {
  registrar.disabled = animales === 0 || referencia.value.trim() === '';
}

referencia.addEventListener('input', actualizarBoton);
elemento('salida').addEventListener('submit', event => {
  event.preventDefault();
  if (animales === 0 || !referencia.value.trim()) return;

  animales--;
  const fila = elemento('filas').insertRow(0);
  for (const valor of [referencia.value.trim(), 'Salida de 1', animales + ' de 50']) {
    fila.insertCell().textContent = valor;
  }
  elemento('ocupacion').textContent = animales + ' de 50 animales';
  elemento('estado').classList.remove('aviso');
  elemento('estado').textContent = animales === 0 ? 'Corral vacío' : 'Hay espacio disponible';
  elemento('confirmacion').textContent = 'Salida registrada. Quedan ' + animales + ' animales.';
  referencia.value = '';
  actualizarBoton();
  referencia.focus();
});

function mostrarHistorial(visible) {
  elemento('historial').hidden = !visible;
  elemento('ficha').hidden = visible;
  elemento('confirmacion').textContent = '';
  elemento(visible ? 'titulo-historial' : 'titulo-ficha').focus();
}
elemento('ver-historial').addEventListener('click', () => mostrarHistorial(true));
elemento('volver').addEventListener('click', () => mostrarHistorial(false));
