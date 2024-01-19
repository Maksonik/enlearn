const drawChartLearnedAll = (static) => {
    const ctx = document.getElementById('ChartLearned2');
    new Chart(ctx, {
      type: 'doughnut',
      data: {
          datasets: [{
            label: 'Статистика',
            data:  Object.values(static).slice(0, Object.values(static).length-1),
            backgroundColor: [
              'rgb(255,102,102)',
              'rgb(255,153,102)',
              'rgb(255,204,102)',
              'rgb(255,255,102)',
              'rgb(204,255,102)',
              'rgb(153,255,102)',
              'rgb(102,255,102)'
            ],
            hoverOffset: 4
          }]
      },
      options: {
        plugins: {
          title: {
            display: true,
            text: 'Статистика слов',
          },
          tooltip: {
            callbacks: {
              label: function(context) {
                let label = Object.keys(static)[context.dataIndex]; // Название текущего элемента
                let value = context.dataset.data[context.dataIndex] || 0; // Значение текущего элемента
                return label + ': ' + value;
              }
            }
          }
        }
      }
    });
  }