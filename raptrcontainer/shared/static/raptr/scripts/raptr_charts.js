function get_bgColors(){
  bgColorSet =[
    'rgba(255, 99, 132, 0.2)',
    'rgba(54, 162, 235, 0.2)',
    'rgba(255, 206, 86, 0.2)',
    'rgba(75, 192, 192, 0.2)',
    'rgba(153, 102, 255, 0.2)',
    'rgba(255, 159, 64, 0.2)',
    'rgba(54, 162, 235, 0.45)',
    'rgba(255, 206, 86, 0.45)',
    'rgba(75, 192, 192, 0.45)',
    'rgba(153, 102, 255, 0.45)',
    'rgba(255, 159, 64, 0.45)',
    'rgba(255, 99, 132, 0.45)',
  ];
  return bgColorSet;
}

function get_borderColors(){
  borderColorSet = [
    'rgba(255,99,132,1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
    'rgba(153, 102, 255, 1)',
    'rgba(255, 159, 64, 1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
    'rgba(153, 102, 255, 1)',
    'rgba(255, 159, 64, 1)',
    'rgba(255,99,132,1)',
  ];
  return borderColorSet
}

function setbyDivisionChart(labels, defaultData){
    var ctx = document.getElementById('byDivisionChart').getContext('2d');
    var byDivisionChart = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: labels,
        datasets: [{
          label: "Funds Received",
          data: defaultData,
            backgroundColor: get_bgColors(),
            borderColor: get_borderColors(),
            borderWidth: 1,
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
                    //calculate the percentage based on the total and current item, also this does a rough rounding to give a whole number
                    var dollars = currentValue.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                    var percentage = Math.floor(((currentValue/total) * 100)+0.5);

                    return "$" + dollars + " (" + percentage + "%)";
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
            backgroundColor: get_bgColors(),
            borderColor: get_borderColors(),
            borderWidth: 1,
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
                    //calculate the percentage based on the total and current item, also this does a rough rounding to give a whole number
                    var dollars = currentValue.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                    var percentage = Math.floor(((currentValue/total) * 100)+0.5);

                    return "$" + dollars + " (" + percentage + "%)";
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
          backgroundColor: 'rgba(54, 162, 235, 0.2)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1,
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
                return  '$' + value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") +'K';
                }
            },
          }]
        },
        tooltips: {
           callbacks: {
            label: function(tooltipItem, data) {
              return '$' + data['datasets'][0]['data'][tooltipItem['index']].toLocaleString() + 'K';
            },
          }
        }
      }
    })
}

function setbySponsorTypeChart(labels, defaultData){
    var ctx2 = document.getElementById('bySponsorTypeChart').getContext('2d');
    var bySponsorTypeChart = new Chart(ctx2, {
      type: 'horizontalBar',
      data: {
        labels: labels,
        datasets: [{
          label: "Funds Received",
            backgroundColor: get_bgColors(),
            borderColor: get_borderColors(),
            borderWidth: 1,
          data: defaultData
        }]
      },
      options: {
        title: {
          display: false,
        },
        legend: {
          display: false,
        },
                scales:{
          xAxes: [{
            ticks: {
              beginAtZero: true,
              callback: function(value, index, values){
                return  '$' + value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                }
            },
          }]
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
                    var dollars = currentValue.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                    return "$" + dollars + " {" + percentage + "%)";
            },
          }
        }
      }
    })
}
