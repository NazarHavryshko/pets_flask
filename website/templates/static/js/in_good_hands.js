const inputFile = document.getElementById('pet__photo');
const selectedImage = document.getElementById('selectedImage');
const svgIcon = document.querySelector('.photo__pet__svg');

inputFile.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            selectedImage.src = e.target.result;
            selectedImage.classList.remove('pet__photo__input')
            svgIcon.style.display = 'none'; // Приховати svg
        };
        reader.readAsDataURL(file);
    }
});

const radioContainersGenderFL = document.querySelectorAll('.gender');

radioContainersGenderFL.forEach(container => {
  const radioInput = container.querySelector('input[type="radio"]');
  
  radioInput.addEventListener('change', () => {
    if (radioInput.checked) {
      radioContainersGenderFL.forEach(c => c.classList.remove('active'));
      container.classList.add('active');
    }
  });
});


const nextBtnPersonalDetails = document.getElementById('nextBtnPersonalDetails');
const personalDetailsStep = document.querySelector('.personal__details__step');
const moreInfoStep = document.querySelector('.more__info__step');

nextBtnPersonalDetails.addEventListener('click', function() {
    const inputFields = document.querySelectorAll('.personal__details__step input[required]');
    let allFieldsFilled = true;

    inputFields.forEach(field => {
        if (field.value.trim() === '') {
            allFieldsFilled = false;
            field.classList.add('error');
        } else {
            field.classList.remove('error');
        }
    });

    if (!allFieldsFilled) {
        alert('Please fill in all required fields.');
    } else {
      personalDetailsStep.classList.add('not__active__el');
      moreInfoStep.classList.remove('not__active__el');
    }
});

const backBtnMI = document.getElementById('cancelBntMI');
const personalDetailsStep2 = document.querySelector('.personal__details__step');
const moreInfoStep2 = document.querySelector('.more__info__step');

backBtnMI.addEventListener('click', () => {
    moreInfoStep2.classList.add('not__active__el');
    personalDetailsStep2.classList.remove('not__active__el');
});