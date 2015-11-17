$(function() {
    $("#login-form").submit(function (event) {
        event.preventDefault();

        var data = $("#login-form input").serializeArray();
        var post_dict = {};

        for (var element in data) {
            if (data[element]['name'] && data[element]['value']) {
                post_dict[data[element]['name']] = data[element]['value'];
            }
        }

        console.log(post_dict);
        $.post('/auth/login', post_dict, function(resp){
            //resp = JSON.parse(resp);
            console.log(resp);
            if (!resp.success){
                var errorbox = $('#login-form .errors-box');
                errorbox.html(resp.errors);
                //TODO parse json response
                //JSON.parse(resp.errors, function(key, val){
                //    alert('in json parser');
                //    var sel ='#login-form #' + key.toString();
                //    if ($(sel).length){
                //        console.log('in s');
                //        for (var err in val) {
                //            $(sel).find('.error-label').html(err.message);
                //            alert(sel + err.message);
                //        }
                //    }
                //})
            } else {
                location.reload();
            }
        });

        return false
    })
});