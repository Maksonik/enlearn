// Функция для отображение списка слов для поисковой строки
const searchWord = (wordListUrl, wordDetailUrl, search) => {
    let debounceTimer;

    search.addEventListener('input', async (e) => {
        // Очистить предыдущий таймер, если он существует
        clearTimeout(debounceTimer);

        // Создать Promise, который резолвится через 300 миллисекунд
        const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

        // Получить введенный текст
        let text = search.value;

        // Установить новый таймер для выполнения запроса через 300 миллисекунд
        debounceTimer = setTimeout(async () => {
            let options = {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                },
            };
            
            let response = await fetch(`${wordListUrl}?text=${encodeURIComponent(text)}`, options);
            let data = await response.json();
            let word_tips = document.querySelector('.word_tips');

            if (data.words !== '') {
                word_tips.style.display = 'block';
                word_tips.innerHTML = '';
                for (let word of data.words.slice(0, 10)) {
                    let div = document.createElement('div');
                    div.textContent = `${word.name} - ${word.short_description}`;
                    div.addEventListener('click', (e) => {
                        window.location.href = wordDetailUrl + '?word=' + encodeURIComponent(word.name);
                    });
                    word_tips.append(div);
                }
            } else {
                word_tips.style.display = 'none';
                word_tips.innerHTML = '';
            }
        }, 300);

        // Дождаться завершения таймера (или предыдущего запроса)
        await delay(300);
    });

    // Скрыть лист после потери фокуса
    search.addEventListener('blur', (e) => {
        let word_tips = document.querySelector('.word_tips');
        setTimeout(() => {
            word_tips.style.display = 'none';
        }, 200);
    });
}
