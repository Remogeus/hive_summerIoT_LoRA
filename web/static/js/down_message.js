function create_table_head() {
  var head = ''
  head += '    <tr>'
  head += '        <th>Time</th>'
  head += '        <th>Record ID</th>'
  head += '        <th>Temperature (°C)</th>'
  head += '        <th>Humidity (%)</th>'
  head += '        <th>Pressure (hPa)</th>'
  head += '        <th>Hive weight (kg)</th>'
  head += '        <th>Battery voltage (V)</th>'
  head += '        <th>Device status</th>'
  head += '        <th>Network status</th>'
  head += '    </tr>'
  return head
}

function create_table_content(data) {
  var table_content = ''
  for (var i in data) {
    table_content += '<tr>'
    table_content += '<td> ' + data[i].time + ' </td>'
    table_content += '<td> ' + data[i].frame_id + ' </td>'
    table_content += '<td> ' + data[i].temperature + ' </td>'
    table_content += '<td> ' + data[i].humidity + ' </td>'
    table_content += '<td> ' + data[i].pressure + ' </td>'
    table_content += '<td> ' + data[i].hive_weight + ' </td>'
    table_content += '<td> ' + data[i].bat_voltage + ' </td>'
    table_content += '<td> ' + data[i].device_status + ' </td>'
    table_content += '<td> ' + data[i].network_status + ' </td>'
    table_content += '</tr>'
  }
  return table_content
}

function create_table(data) {
  var table = ''
  table += '<table class=\"center\">'
  table += create_table_head()
  table += create_table_content(data)
  table += '</table>'
  $('#package').html(table)
}

function error_message(data) {
  var content = ''
  content += '<div id=\"error\">'
  content += '<h1> Error ' + data.error_code + ' - ' + data.user_msg + '</h1>'
  content += '<p>' + data.dev_msg + ' ' + data.msg_more + '</p>'
  content += '<p><code> Application code: ' + data.app_code + '</code></p>'
  content += '</div>'

  $('#package').html(content)
}

function create_xy(data, x_name, y_name) {
  var xy = Array()
  for (var i in data) {
    xy.push({
      'x': data[i][x_name],
      'y': data[i][y_name]
    })
  }
  return xy
}

function create_array(data, name) {
  var values = Array()
  for (var i in data) {
    values.push(data[i][name])
  }
  return values.reverse()
}


function update_chart(chart_name, x, y, line_color, label) {
  var myChart = new Chart($('#' + chart_name), {
    type: 'line',
    data: {
      labels: x,
      datasets: [{
        label: label,
        data: y,
        borderColor: line_color,
        fill: false,
      }]
    },
    options: {
      responsive: false,
      animation: {
        duration: 0, // general animation time
      },
      hover: {
        animationDuration: 0, // duration of animations when hovering an item
      },
      responsiveAnimationDuration: 0, // animation duration after a resize
      scales: {
        xAxes: [{
          ticks: {
            beginAtZero: true
          },
          stacked: true
        }],
        yAxes: [{
          ticks: {
            beginAtZero: true
          },
          stacked: true
        }]
      }
    }
  })
}

$(document).ready(function() {
  function get_json_message() {
    $.getJSON("/api/message", function(data) {

      if ('data_is_valid' in data) {
        if (!data['data_is_valid']) {
          error_message(data)
          return
        }
      } else {
        create_table(data)
        // var xy= create_xy(data, 'time', 'temperature')
        var x = create_array(data, 'time')
        var y = create_array(data, 'temperature')
        update_chart('temp_chart', x, y, 'red', 'temperature')
        y = create_array(data, 'humidity')
        update_chart('hum_chart', x, y, 'blue', 'humidity')
      }

    })
    setTimeout(get_json_message, 30000)
  }

  setTimeout(get_json_message, 1000) //
})
