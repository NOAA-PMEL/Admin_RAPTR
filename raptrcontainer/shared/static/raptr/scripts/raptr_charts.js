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
                    var dataset = data.datasets[tooltipItem.datasetIndex];
                    //calculate the total of this data set
                    var total = dataset.data.reduce(function(previousValue, currentValue, currentIndex, array) {
                    return previousValue + currentValue;
                    });
                    //get the current items value
                    var currentValue = dataset.data[tooltipItem.index];
                    //calculate the precentage based on the total and current item, also this does a rough rounding to give a whole number
                    var percentage = Math.floor(((currentValue/total) * 100)+0.5);

                    return percentage + "%";
            },
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
                    var dataset = data.datasets[tooltipItem.datasetIndex];
                    //calculate the total of this data set
                    var total = dataset.data.reduce(function(previousValue, currentValue, currentIndex, array) {
                    return previousValue + currentValue;
                    });
                    //get the current items value
                    var currentValue = dataset.data[tooltipItem.index];
                    //calculate the precentage based on the total and current item, also this does a rough rounding to give a whole number
                    var percentage = Math.floor(((currentValue/total) * 100)+0.5);

                    return percentage + "%";
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
          backgroundColor: "#4472C4",
          data: defaultData
        }]
      },
      options: {
      title: {
          display: false,
          text: '(in thousands)'
        },
        legend: {
          display: false
        },
        scales:{
          yAxes: [{
            ticks: {
              beginAtZero: true,
              callback: function(value, index, values){
                return  '$' + value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");}
            },
          }]
        },
        tooltips: {
           callbacks: {
            label: function(tooltipItem, data) {
              return '$' + data['datasets'][0]['data'][tooltipItem['index']].toLocaleString();
            },
          }
        }
      }
    })
}