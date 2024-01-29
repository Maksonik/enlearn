const drawChartWeek = (activity) => {
  const ctx = document.getElementById('ChartWeek');
  
  const lastSevenDaysList = getSevenDaysList()
  const label = lastSevenDaysList.map((day) => day.split('-').slice(1).join('-'))
  const activityForDays = lastSevenDaysList.map((day) => activity[day] == undefined ? 0 : activity[day])
  let sumActivityForDays = activityForDays.map((day) => day == 0 ? day : Object.values(day).reduce((first, a) => first + a,0))
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: label,
      datasets: [{
        label: 'Активность за день',
        data: sumActivityForDays,
        fill: false,
        borderColor: 'rgb(0, 0, 0)',
        tension: 0.1
      }]
    },
    options: {
      responsive: true,
      scales: {
        x: {
          grid: {
            display: false 
          }
        },
        y: {
          beginAtZero: true
        }
      },
    }
  });
}

function getSevenDaysList() {
  const today = new Date();
  const sevenDaysList = [];

  for (let i = 6; i >= 0; i--) {
    const day = new Date(today);
    day.setDate(today.getDate() - i);

    const year = day.getFullYear();
    const month = (day.getMonth() + 1).toString().padStart(2, '0'); // добавляем ведущий ноль, если месяц < 10
    const date = day.getDate().toString().padStart(2, '0'); // добавляем ведущий ноль, если день < 10

    const formattedDate = `${year}-${month}-${date}`;
    sevenDaysList.push(formattedDate);
  }

  return sevenDaysList;
}
