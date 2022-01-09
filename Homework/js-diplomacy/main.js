'use strict';
function changeColor(){
    const redWords = document.querySelectorAll('.color-change');

    for (const word of redWords) {
        word.classList.add('red');
    }
}
// Event handler
document.querySelector('.color-change-button').addEventListener('click', changeColor);

function formValidate (evt) {
    evt.preventDefault();

    const formData = document.querySelector('input[name="number"]');
    const userNum = Number(formData.value); // typecast to num

    if (userNum >= 10 || !userNum ) {
        formFeedback.innerText = 'Please enter a smaller number';
    } else {
        formFeedback.innerText = 'You are good to go!';
    }
}

// event handler
document.querySelector('.number-form').addEventListener('submit', formValidate);
