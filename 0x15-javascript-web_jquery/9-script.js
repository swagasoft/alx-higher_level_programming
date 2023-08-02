#!/usr/bin/node

$(document).ready(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('div#hello').text(data.hello);
  });
});
