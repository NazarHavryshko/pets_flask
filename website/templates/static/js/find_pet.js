document.addEventListener('DOMContentLoaded', () => {
    const filterBtn = document.getElementById('filterBtn');
    const selectContainer = document.querySelector('.select-container');
    // const applyFiltersBtn = document.getElementById('applyFilters');
    // const ageSelect = document.getElementById('ageSelect');
    // const genderSelect = document.getElementById('genderSelect');
    // Додайте інші селекти якщо потрібно
    
    filterBtn.addEventListener('click', () => {
        selectContainer.style.display = selectContainer.style.display === 'none' ? 'flex' : 'none';
        filterBtn.classList.toggle('active');
    });
    
    // applyFiltersBtn.addEventListener('click', () => {
    //     const selectedAge = ageSelect.value;
    //     const selectedGender = genderSelect.value;
    //     // Отримання інших обраних параметрів
        
    //     // Відправити запит на бекенд і обробити результат
    //     sendBackendRequest(selectedAge, selectedGender);
    // });
    
    // function sendBackendRequest(age, gender) {
    //     // Ваш код для відправки запиту на бекенд з урахуванням параметрів
    //     // Тут можна використовувати Fetch API або інші методи
        
    //     // Після отримання відповіді виконати подальші дії
    // }
});

const checkboxes = document.querySelectorAll('.checkbox__style');

checkboxes.forEach(checkbox => {
    const label = checkbox.nextElementSibling;

    checkbox.addEventListener('change', () => {
        const customCheckbox = label.querySelector('.custom__checkbox');
        
        if (checkbox.checked) {
            customCheckbox.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M17 9L9.99998 16L6.99994 13M8 20H16C18.2091 20 20 18.2091 20 16V8C20 5.79086 18.2091 4 16 4H8C5.79086 4 4 5.79086 4 8V16C4 18.2091 5.79086 20 8 20Z" stroke="#54ADFF" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>';
        } else {
            customCheckbox.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M4 8C4 5.79086 5.79086 4 8 4H16C18.2091 4 20 5.79086 20 8V16C20 18.2091 18.2091 20 16 20H8C5.79086 20 4 18.2091 4 16V8Z" stroke="#54ADFF" stroke-width="1.5" stroke-linejoin="round"/></svg>';
        }
    });
});


const filterTitle = document.querySelector('.age__filter__title');
const filterOpenIcon = document.querySelector('.age__filter__open');
const filterCloseIcon = document.querySelector('.age__filter__close');
const ageCheckbox = document.querySelector('.age__checkbox');

filterTitle.addEventListener('click', () => {
    ageCheckbox.style.display = ageCheckbox.style.display === 'none' ? 'block' : 'none';
    filterOpenIcon.style.display = ageCheckbox.style.display === 'none' ? 'block' : 'none';
    filterCloseIcon.style.display = ageCheckbox.style.display === 'none' ? 'none' : 'block';
});

const genderFilterTitle = document.querySelector('.gender__filter__title');
const genderFilterOpenIcon = document.querySelector('.gender__filter__open');
const genderFilterCloseIcon = document.querySelector('.gender__filter__close');
const genderCheckbox = document.querySelector('.gender__checkbox');

genderFilterTitle.addEventListener('click', () => {
    genderCheckbox.style.display = genderCheckbox.style.display === 'none' ? 'block' : 'none';
    genderFilterOpenIcon.style.display = genderCheckbox.style.display === 'none' ? 'block' : 'none';
    genderFilterCloseIcon.style.display = genderCheckbox.style.display === 'none' ? 'none' : 'block';
});
