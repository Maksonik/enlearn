const drawChartLearned = (static) => {
    const ctx = document.getElementById('ChartLearned');
    data = Object.values(static).at(-2)
    new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: [
            'Первая 1000 слов',
            'Выученые слова',
          ],
          datasets: [{
            label: 'Первая 1000 слов',
            data: [1000-data, data],
            backgroundColor: [
              'rgb(255,102,102)',
              'rgb(102,255,102)'
            ],
            hoverOffset: 4
          }]
      },
      options: {
        plugins: {
          title: {
            display: false,
            position: 'top'
          },
          tooltip: { 
            callbacks: {
              label: function(context) {
                let label = context.label; // Название текущего элемента
                let value = context.dataset.data[context.dataIndex] || 0; // Значение текущего элемента
                console.log(label,value)
                return label + ': ' + value;
              },
              title: function() { 
                return '' // Убираю заголовок в подсказках
              }
            }
          }  
        },
      }
    });
  }