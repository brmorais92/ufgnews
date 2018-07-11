$.ajaxSetup ({
    cache: false
});

function modal_add_article_ajax() {
    $('#add_article_form').on('submit', function (e) {
      e.preventDefault();
      $.post('/add_article', $('#add_article_form').serialize(), function(data, status, xhr) {
          //encontrou algum erro ao criar o artigo
          if ($(data).find(".alert").length) {
              $('.alert-danger').remove();
              $('#modal_add_article_body').prepend($(data).find('#add_article_error_list').html());
              $('#inputTitle').trigger('focus');
              modal_add_article_ajax();
          }
          else {
              location.reload();
          }
          return false;
      });
    });
    $('#modal_add_article').on('shown.bs.modal', function () {
        $('#inputTitle').trigger('focus');
    });
}

$(function() {
  $('#modal_add_article').load('/add_article .modal-dialog', modal_add_article_ajax);
});