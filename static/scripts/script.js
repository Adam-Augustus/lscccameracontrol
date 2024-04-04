window.addEventListener("DOMContentLoaded", (event) => {
const cam1_value = document.querySelector('#cam1_value');
const cam2_value = document.querySelector('#cam2_value');
const cam3_value = document.querySelector('#cam3_value');
const cam4_value = document.querySelector('#cam4_value');

const cam1_slider = document.querySelector('#cam1_iris');
const cam2_slider = document.querySelector('#cam2_iris');
const cam3_slider = document.querySelector('#cam3_iris');
const cam4_slider = document.querySelector('#cam4_iris');

const irisValues = [1.9, 2.0, 2.2, 2.4, 2.6, 2.8, 3.1, 3.4, 3.7, 4,   4.4, 4.8, 5.2, 5.6, 6.2, 6.8, 7.3, 8,   8.7, 9.6, 10,  11,  12,  14,  15,  16,  65535];

cam1_slider.addEventListener('input', () => {
    cam1_value.innerHTML = String(irisValues[cam1_slider.value]);
    fetch(`/cam1/${cam1_slider.value}`).then((response) => console.log(response));
});

cam2_slider.addEventListener('input', () => {
    cam2_value.innerHTML = String(irisValues[cam2_slider.value]);
    fetch(`/cam2/${cam2_slider.value}`).then((response) => console.log(response));
});

cam3_slider.addEventListener('input', () => {
    cam3_value.innerHTML = String(irisValues[cam3_slider.value]);
    fetch(`/cam3/${cam3_slider.value}`).then((response) => console.log(response));
});

cam4_slider.addEventListener('input', () => {
    cam4_value.innerHTML = String(irisValues[cam4_slider.value]);
    fetch(`/cam4/${cam4_slider.value}`).then((response) => console.log(response));
});
});