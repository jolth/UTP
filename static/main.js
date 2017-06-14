$(document).ready( function() {
    //var _validFileExtensions = [".jpg", ".jpeg"];
    var reg = /\.(jpg|jpeg)/g;

    $(document).on('change', '.btn-file :file', function() {
	    var input = $(this),
			label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
            //console.log(input[0].type == 'file');
            //console.log(input)
            //console.log(label);
            //'jorge.jpeg'.match(/\.(jpg|jpeg)/g)
            if (input[0].type == 'file') {
                if (!label.match(reg)) {
                    alert("No es un jpg/jpeg");
                    return; 
                }
            } else {
                return;
            }
		input.trigger('fileselect', [label]);
    });

    //Set file name
	$('.btn-file :file').on('fileselect', function(event, label) {
        var input = $(this).parents('.input-group').find(':text'),
		    log = label;
		    
		if( input.length ) {
		    input.val(log);
		} else {
		    if( log ) alert(log);
		}
	    
	});
});
