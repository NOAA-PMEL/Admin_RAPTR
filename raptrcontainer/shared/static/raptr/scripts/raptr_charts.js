function byDivisionChart(byDivisionChart) {
      var ctx = document.getElementById('byDivisionChart').getContext('2d');
      var byDivisionChart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ["ED","OE", "OC", "AD"],
          datasets: [{
            label: "Funds Received",
            backgroundColor: ["#4472C4", "#ED7D31", "#A5A5A5", "#FFC000", "#008000"],
            data: [235000, 46476, 33126, 15000]
          }]
        },
        options: {
          title: {
            display: false,
            text: 'FY19 New Funds Received'
          },
          legend: {
            position: 'right'
          },
          tooltips: {
            callbacks: {
              label: function(tooltipItem, data) {
                return data['labels'][tooltipItem['index']] + ': $' + data['datasets'][0]['data'][tooltipItem['index']].toLocaleString();
              },
              afterLabel: function(tooltipItem, data) {
                var dataset = data['datasets'][0];
                var percent = Math.round((dataset['data'][tooltipItem['index']] / dataset["_meta"][0]['total']) * 100)
                return '(' + percent + '%)';
              }
            }
          }
        }
      })
}

function byResearchProgramChart(byResearchProgramChart) {
      var ctx = document.getElementById('byResearchProgramChart').getContext('2d');
      var byResearchProgramChart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ["ED","CO2", "EOI", "AD", "Arctic"],
          datasets: [{
            label: "Funds Received",
            backgroundColor: ["#4472C4", "#ED7D31", "#A5A5A5", "#FFC000", "#008000"],
            data: [235000, 33126, 31476, 15000, 15000]
          }]
        },
        options: {
          title: {
            display: false,
            text: 'FY19 New Funds Received'
          },
          legend: {
            position: 'right'
          },
          tooltips: {
            callbacks: {
              label: function(tooltipItem, data) {
                return data['labels'][tooltipItem['index']] + ': $' + data['datasets'][0]['data'][tooltipItem['index']].toLocaleString();
              },
              afterLabel: function(tooltipItem, data) {
                var dataset = data['datasets'][0];
                var percent = Math.round((dataset['data'][tooltipItem['index']] / dataset["_meta"][0]['total']) * 100)
                return '(' + percent + '%)';
              }
            }
          }
        }
      })
}
