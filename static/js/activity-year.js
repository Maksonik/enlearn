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


function generateYearCalendar(year, activity) {
    const svgElement = document.querySelector('svg');
    svgElement.innerHTML = ''; // Очищаем содержимое SVG

    const svgNS = "http://www.w3.org/2000/svg";
    const svgCode = document.createElementNS(svgNS, 'g');

    const monthWidth = 75;
    const dayWidth = 10;
    const dayHeight = 10;
    const monthSpacing = 0;

    let xStart = 20;
    let yStart = 120;

    for (let month = 0; month < 12; month++) {
        const days = daysInMonth(month, year);
        const firstDayOfWeek = getFirstDayOfWeek(month, year);
        const weeks = Math.ceil((days + firstDayOfWeek) / 7);

        const monthGroup = document.createElementNS(svgNS, 'g');
        monthGroup.setAttribute('class', `month ${month + 1}`);
        monthGroup.setAttribute('transform', `translate(${xStart},${yStart})`);
        monthGroup.innerHTML = `<text x="40" y="-12" class="month" text-anchor="middle">${getMonthName(month, year)}</text>`;

        for (let dayOfWeek = 0; dayOfWeek < 7; dayOfWeek++) {
            for (let week = 0; week < weeks; week++) {
                const day = week * 7 + dayOfWeek - firstDayOfWeek + 1;

                if (day > 0 && day <= days) {
                    const value = getValueForDay(`${year}-${(month + 1).toString().padStart(2, '0')}-${day}`, activity);
                    const color = getColorForValue(value);
                    const rect = document.createElementNS(svgNS, 'rect');
                    rect.setAttribute('x', `${week * (dayWidth + 3)}`);
                    rect.setAttribute('y', `${dayOfWeek * (dayHeight + 3)}`);
                    rect.setAttribute('width', `${dayWidth}`);
                    rect.setAttribute('height', `${dayHeight}`);
                    rect.setAttribute('rx', '2');
                    rect.setAttribute('ry', '2');
                    rect.setAttribute('class', 'day');
                    rect.setAttribute('fill', color);
                    monthGroup.appendChild(rect);
                }
            }
        }

        svgCode.appendChild(monthGroup);
        xStart += monthWidth + monthSpacing;
    }

    svgElement.appendChild(svgCode);
}



