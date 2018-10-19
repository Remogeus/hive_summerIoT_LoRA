$(document).ready(function() {
  function GetHiveData() {
    $.getJSON("/api/device", function(data) {
      $("#hive_name").text(data.name);
      $("#hive_weight").text(data.weight);
      $("#hive_battery").text(data.battery);
    });
    setTimeout(GetHiveData, 1000);
  };
  setTimeout(GetHiveData, 1000);
});
