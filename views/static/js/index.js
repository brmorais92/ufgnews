$(function() {
  console.log( 'ready!' );
  $('#login_form').on('submit', function (e) {
      e.preventDefault();
      $.post('/login', $('#login_form').serialize(), function(data, status, xhr) {
          $('#modal_login_body').html(data);
      });
      console.log('enviou');
  });
  $('#modalLogin').on('shown.bs.modal', function () {
      $('#modalLogin').html('<p>FAIL</p>');
    $('#inputUsuario').trigger('focus');
    console.log("APARECEU");
  });
});