$(document).ready(function(){
    $(document).on('click', '.changeStatus', function() {
        var br_id = $(this).attr('data-id');
        var this_row = $(this);
        $.ajax({
            url: '/invest-status/',
            type: "post",
            data: {
              'borrower_id': br_id
            },
            dataType: 'json',
            success: function (data) {
                if (data.status) {
                    this_row.html(data.data);
                }
            }
        });
    });
});