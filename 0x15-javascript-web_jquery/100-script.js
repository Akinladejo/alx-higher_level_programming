document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('header').style.color = '#FF0000';
    var header = document.querySelector('header');
    header.style.color = 'red';
    console.log(header.textContent);
});
