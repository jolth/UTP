$(document).ready(function () {

    function isFormValid() {
        return $('#inputName').val() != '' && $('#inputEmail').val() != '' && $('#inputMessage').val() != '';
    }

    function toggleEnableContinue() {
        $('#btn_send').prop('disabled', !isFormValid());
    }

    $('#inputName, #inputEmail, #inputMessage').keyup(toggleEnableContinue);

    $('#form_contact').submit(function(e) {
        e.preventDefault();
        $(this).hide();
        $('#message').show();
    });

});
