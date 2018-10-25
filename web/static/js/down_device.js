$(document).ready(function() {
  function GetDevData() {
    $.getJSON("/test_api/device", function(data) {
      //$("#hive_name").text(data.name);
      //$("#hive_weight").text(data.weight);
      //$("#hive_battery").text(data.battery);
      if($.text(data.data_is_valid) == true){
        $("#error_code").text(data.error_code);
        $("#user_msg").text(data.user_msg);
        $("#dev_msg").text(data.dev_msg);
        $("#msg_more").text(data.msg_more);
        $("#app_code").text(data.app_code);
      }
    });
    setTimeout(GetDevData, 1000);
  };
  setTimeout(GetDevData, 1000);
});
