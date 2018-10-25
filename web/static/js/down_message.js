$(document).ready(function() {
  function GetHiveMessage() {
    $.getJSON("/test_api/message", function(data) {
      $.each(data.results, function(key, val) {
    console.log(val.time);
    })
    }
  );
  setTimeout(GetHiveMessage, 1000);
};
setTimeout(GetHiveMessage, 1000);
});
