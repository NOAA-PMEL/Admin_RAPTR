function setbyDivisionChart(labels, defaultData){
    var ctx = document.getElementById('byDivisionChart').getContext('2d');
    var byDivisionChart = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: labels,
        datasets: [{
          label: "Funds Received",
          backgroundColor: ["#4472C4", "#ED7D31", "#A5A5A5", "#FFC000", "#008000"],
          data: defaultData
        }]
      },
      options: {
        title: {
          display: false,
        },
        legend: {
          position: 'right'
        },
        tooltips: {
          callbacks: {
            label: function(tooltipItem, data) {
              return data['labels'][tooltipItem['index']] + ': $' + data['datasets'][0]['data'][tooltipItem['index']].toLocaleString();
            },
//            afterLabel: function(tooltipItem, data) {
//              var dataset2 = data['datasets'][0];
//              var percent2 = Math.round((dataset['data'][tooltipItem['index']] / dataset["_meta"][0]['total']) * 100)
//              return '(' + percent2 + '%)';
//            }
          }
        }
      }
    })
}

function setbyResearchProgramChart(labels, defaultData){
    var ctx2 = document.getElementById('byResearchProgramChart').getContext('2d');
    var byResearchProgramChart = new Chart(ctx2, {
      type: 'pie',
      data: {
        labels: labels,
        datasets: [{
          label: "Funds Received",
          backgroundColor: ["#4472C4", "#ED7D31", "#A5A5A5", "#FFC000", "#008000"],
          data: defaultData
        }]
      },
      options: {
        title: {
          display: false,
        },
        legend: {
          position: 'right'
        },
        tooltips: {
          callbacks: {
            label: function(tooltipItem, data) {
              return data['labels'][tooltipItem['index']] + ': $' + data['datasets'][0]['data'][tooltipItem['index']].toLocaleString();
            },
          }
        }
      }
    })
}

function setHistoryChart(labels, defaultData){
    var ctx2 = document.getElementById('byHistoryChart').getContext('2d');
    var byHistoryChart = new Chart(ctx2, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: "Funds Received",
          backgroundColor: ["#4472C4", "#4472C4", "#4472C4", "#4472C4", "#4472C4" ],
          data: defaultData
        }]
      },
      options: {
      title: {
          display: false
        },
        legend: {
          display: false
        },
        tooltips: {
          callbacks: {
            label: function(tooltipItem, data) {
              return data['labels'][tooltipItem['index']] + ': $' + data['datasets'][0]['data'][tooltipItem['index']].toLocaleString();
            },
          }
        }
      }
    })
}