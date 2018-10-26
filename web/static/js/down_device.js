function error_message(data) {
  var content = '';
  content += '<div id=\"error\">';
  content += '<h1> Error ' + data.error_code + ' - ' + data.user_msg + '</h1>';
  content += '<p>' + data.dev_msg + ' ' + data.msg_more + '</p>';
  content += '<p><code> Application code: ' + data.app_code + '</code></p>';
  content += '</div>';

  $('#package').html(content);
}

$(document).ready(function() {
  function get_json_device() {
    $.getJSON("/test_api/device", function(data) {
      if ('data_is_valid' in data) {
        if (!data['data_is_valid']) {
          error_message(data);
          return;
        }
      }
    });
    setTimeout(get_json_device, 1000);
  };
  setTimeout(get_json_device, 1000);
});
