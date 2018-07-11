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
$(document).on('click', '.update_article_button', function() {
    let article_id = $(this).data('article-id');
    $('#modal_update_article').load('/update_article/' + article_id + ' .modal-dialog', function() {
        $('#update_article_form_button').click(function() {
            console.log('HEY');
            var dict = Object.assign({}, {'id': article_id}, $('#update_article_form').serialize());
            console.log(dict);
            $.post('/update_article', $('#update_article_form').serialize(), function(data) {
                location.reload();
            });
            return false;
        });
        $('#modal_update_article').modal('show');
    });
    return false;
});