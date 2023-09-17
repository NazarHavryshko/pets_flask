const NameBtn = document.getElementById('name__btn');
const Name = document.getElementById('name');


NameBtn.addEventListener('click', () => {
    Name.disabled = false;
    NameBtn.style.display = 'none';
    document.getElementById('save__btn').style.display = 'block';
});


const EmailBtn = document.getElementById('email__btn');
const Email = document.getElementById('email');


EmailBtn.addEventListener('click', () => {
    Email.disabled = false;
    EmailBtn.style.display = 'none';
    document.getElementById('save__btn').style.display = 'block';
});


const DateBtn = document.getElementById('date__btn');
const Date = document.getElementById('date');


DateBtn.addEventListener('click', () => {
    Date.disabled = false;
    DateBtn.style.display = 'none';
    document.getElementById('save__btn').style.display = 'block';
});


const TelBtn = document.getElementById('tel__btn');
const Tel = document.getElementById('tel');


TelBtn.addEventListener('click', () => {
    Tel.disabled = false;
    TelBtn.style.display = 'none';
    document.getElementById('save__btn').style.display = 'block';
});


const CityBtn = document.getElementById('city__btn');
const City = document.getElementById('city');


CityBtn.addEventListener('click', () => {
    City.disabled = false;
    CityBtn.style.display = 'none';
    document.getElementById('save__btn').style.display = 'block';
});




const inputFile = document.getElementById('new__photo');
const selectedImage = document.getElementById('selectedImage');
const svgIcon = document.querySelector('.user__pet__svg');

inputFile.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            selectedImage.src = e.target.result;
            selectedImage.classList.remove('user__photo__input')
            svgIcon.style.display = 'none'; // Приховати svg
        };
        reader.readAsDataURL(file);
    }
});