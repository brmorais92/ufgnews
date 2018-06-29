$.ajaxSetup ({
    cache: false
});

$(function() {
  $('#modalLogin').load('/login .modal-dialog', function() {
    $('#login_form').on('submit', function (e) {
      e.preventDefault();
      $.post('/login', $('#login_form').serialize(), function(data, status, xhr) {
          //encontrou algum erro no login
          if($(data).find(".alert").length) {
              $('#modalLogin').html(data);
              $('#inputUsuario').trigger('focus');
          }
          else {
              $('body').load('/');
          }
      });
    });
    $('#modalLogin').on('shown.bs.modal', function () {
        $('#inputUsuario').trigger('focus');
    });
  });
});