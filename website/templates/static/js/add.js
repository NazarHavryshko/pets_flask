const radioContainers = document.querySelectorAll('.radio__btn__div');

radioContainers.forEach(container => {
  const radioInput = container.querySelector('input[type="radio"]');
  
  radioInput.addEventListener('change', () => {
    if (radioInput.checked) {
      radioContainers.forEach(c => c.classList.remove('active'));
      container.classList.add('active');
    }
  });
});



const nextButtonSell = document.getElementById('nextBtn');
const personalDetailsStepSell = document.querySelector('.personal__details__step__sell');
const personalDetailsStepLostFound = document.querySelector('.personal__details__lost__found');
const addPetMainFormSell = document.querySelector('.add__pet__main__form');

nextButtonSell.addEventListener('click', () => {
    const radioSell = document.querySelector('input[type="radio"][value="sell"]');
    if (radioSell.checked) {
        document.location.assign("/sell");
    }

    const radioLostFound = document.querySelector('input[type="radio"][value="lost_found"]');
    if (radioLostFound.checked) {
        document.location.assign("/lost_found");
    }

    const radioLostInGoodHands = document.querySelector('input[type="radio"][value="in_good_hands"]');
    if (radioLostInGoodHands.checked) {
        document.location.assign("/in_good_hands");
    }

    const radioLostYourPet = document.querySelector('input[type="radio"][value="your_pet"]');
    if (radioLostYourPet.checked) {
        document.location.assign("/your_pet");
    }
});
