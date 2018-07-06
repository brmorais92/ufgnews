$.ajaxSetup ({
    cache: false
});

function modal_login_ajax() {
    $('#login_form').on('submit', function (e) {
      e.preventDefault();
      $.post('/login', $('#login_form').serialize(), function(data, status, xhr) {
          //encontrou algum erro no login
          if ($(data).find(".alert").length) {
              $('.alert-danger').remove();
              $('#modalLogin #modal_login_body').prepend($(data).find('#error_list').html());
              $('#inputUsuario').trigger('focus');
              modal_login_ajax();
          }
          else {
              $('body').load('/');
          }
          return false;
      });
    });
    $('#modalLogin').on('shown.bs.modal', function () {
        $('#inputUsuario').trigger('focus');
    });
}

$(function() {
  $('#modalLogin').load('/login .modal-dialog', modal_login_ajax);
});