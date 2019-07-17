/**
 * Created by x-gamer on 7/11/18.
 */

$(function () {

  $(".js-create-driver").click(function () {
    $.ajax({
      url: "{% url 'drivercreate' %}",
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-driver").modal("show");
      },
      success: function (data) {
        $("#modal-driver .modal-content").html(data.html_form);
      }
    });
  });

});