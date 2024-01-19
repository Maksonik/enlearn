function daysInMonth(month, year) {
    return new Date(year, month + 1, 0).getDate();
}

function getMonthName(month, year) {
    const date = new Date(year, month, 1); // Выберите любой год, например, 2000
    const monthName = date.toLocaleString('default', { month: 'short' });
    return monthName;
  }
  

function getFirstDayOfWeek(month, year) {
    const firstDay = new Date(year, month, 1).getDay();
    return firstDay === 0 ? 6 : firstDay - 1; // Коррекция для начала с понедельника
}

function getColorForValue(value) {
    var whiteColor = [255, 255, 255]; // RGB для белого
    var darkGreenColor = [0, 128, 0]; // RGB для темно-зеленого
    value = value == 0 ? 0 : value + 30

    // Интерполируем цвет между белым и темно-зеленым в зависимости от значения
    var interpolatedColor = whiteColor.map(function (white, index) {
      return white + (darkGreenColor[index] - white) * value / 100;
    });

    return 'rgb(' + interpolatedColor.join(', ') + ')'
  }

function getValueForDay(data, activity) {
    if (data in activity) {
        let value = Object.values(activity[data]).reduce((first, a) => first + a,0)
        return value
    } else {
        return 0
    }
}


function generateYearCalendar(year,activity) {
    const data = activity
    const svgCode = [];
    const monthWidth = 80; // Ширина блока месяца
    const dayWidth = 10;
    const dayHeight = 10;
    const monthSpacing = 0; // Интервал между месяцами

    let xStart = 20;
    let yStart = 120;
    svgCode.push(`<text x="500" y="50" class="year" text-anchor="middle" font-size="25">Активность за ${year} год</text>`)
    for (let month = 0; month < 12; month++) {
        const days = daysInMonth(month, year);
        const firstDayOfWeek = getFirstDayOfWeek(month, year);
        const weeks = Math.ceil((days + firstDayOfWeek) / 7);

        svgCode.push(`<g class="month ${month + 1}" transform="translate(${xStart},${yStart})">`);
        svgCode.push(`<text x="40" y="-12" class="month" text-anchor="middle">${getMonthName(month,year)}</text>`);

        for (let dayOfWeek = 0; dayOfWeek < 7; dayOfWeek++) {
            for (let week = 0; week < weeks; week++) {
                const day = week * 7 + dayOfWeek - firstDayOfWeek + 1;

                if (day > 0 && day <= days) {
                    const value = getValueForDay(`${year}-${(month + 1).toString().padStart(2, '0')}-${day}`,  data);
                    const color = getColorForValue(value);
                    svgCode.push(`<rect x="${week * (dayWidth + 3)}" y="${dayOfWeek * (dayHeight + 3)}" width="${dayWidth}" height="${dayHeight}"  rx="2" ry="2" class="day" fill="${color}"></rect>`);
                }
            }
        }

        svgCode.push('</g>');

        xStart += monthWidth + monthSpacing;
    }

    document.querySelector('svg').innerHTML = svgCode.join('');
}




