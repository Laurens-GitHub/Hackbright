function adder(x, y) {
  return x + y;
}

document.querySelector('#calc-form').addEventListener('submit', evt => {
  evt.preventDefault();

  const x = Number(document.querySelector('#x-field').value);
  const y = Number(document.querySelector('#y-field').value);

  document.querySelector('#result').textContent = adder(x, y);
});
