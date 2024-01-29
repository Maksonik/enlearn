// Функция для отображение списка слов для поисковой строки
const searchWord = (wordListUrl, wordDetailUrl, search) => {
    search.addEventListener('input', async (e) => {
        //получить подстроку
        let text = search.value
        
        //отправить запрос на сервер
        let options = {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
            },
        };
        let response = await fetch(`${wordListUrl}?text=${encodeURIComponent(text)}`, options)
        let data = await response.json()
        let word_tips = document.querySelector('.word_tips')

        //вывести 10 слов
        if (data.words != ''){
            word_tips.style.display = 'block'
            word_tips.innerHTML = ''
            for (let word of data.words.slice(0,10)) {
                let div = document.createElement('div')
                div.textContent = `${word.name} - ${word.short_description}`
                //добавить событие перехода на слово
                div.addEventListener('click', (e) => {
                    window.location.href = wordDetailUrl +'?word=' + encodeURIComponent(word.name)
                })
                word_tips.append(div)
        }} else {
            word_tips.style.display = 'none'
            word_tips.innerHTML = ''
        }
    })
    
    //Скрыть лист после нажатия
    search.addEventListener('blur', (e) => {
        let word_tips = document.querySelector('.word_tips')
        setTimeout(() => {
            word_tips.style.display = 'none';
        }, 200)
    })
}
