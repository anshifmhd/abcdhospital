
$(document).ready(function () {
        $('#personalDetails').hide();
        $('#logOut').hide();
    if(request.session['userid'] = user.id){
        $('#personalDetails').show();
        $('#logOut').show();
    }

})
