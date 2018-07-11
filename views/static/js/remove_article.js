$.ajaxSetup ({
    cache: false
});

$(document).on('click', '.remove_article_button', function() {
    let article_id = $(this).data('article-id');
    $('#modal_remove_article').load('/remove_article/'+ article_id + ' .modal-dialog',
       function() {
            $('#remove_article_button').click(function() {
                $.post('/remove_article', {'id': article_id}, function(data) {
                    location.reload();
                });
            });
            $('#modal_remove_article').modal("show");
       });
    return false;
});

$(function() {
  //$('#modal_remove_article').load('/remove_article/5 .modal-dialog', modal_remove_article_ajax);
});