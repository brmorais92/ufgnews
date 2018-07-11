$.ajaxSetup ({
    cache: false
});

function modal_update_article_ajax() {
    $('#update_article_form').on('submit', function (e) {
      e.preventDefault();
      $.post('/update_article', $('#update_article_form').serialize(), function(data, status, xhr) {
          //encontrou algum erro ao criar o artigo
          if ($(data).find(".alert").length) {
              $('.alert-danger').remove();
              $('#modal_update_article_body').prepend($(data).find('#update_article_error_list').html());
              $('#inputTitle').trigger('focus');
              modal_update_article_ajax();
          }
          else {
              location.reload();
          }
          return false;
      });
    });
    $('#modal_update_article').on('shown.bs.modal', function () {
        $('#inputTitle').trigger('focus');
    });
}

$(function() {
  $('#modal_update_article').load('/update_article .modal-dialog', modal_update_article_ajax);
});