$(document).ready(function() {
    setProfilePicture();
    unload();

    $.get('https://api.github.com/users/' + username, function(resp) {
        $('.company').text(resp.company);
        $('.location').text(resp.location);
    });

    $('.profile-picture-container').click(function() {
        $('#image-upload').click();
    });

    $("#image-upload").change(function() {
        load();
        // Read the input image
        var reader = new FileReader();
        reader.readAsDataURL(document.querySelector('#image-upload').files[0]);
        reader.onload = function() {
            var b64 = reader.result;
            // Send it over to the server
            $.post('/api_predict/' + username + '/predict', data={'image': b64}, function(jwt) {
                payload = jwt_decode(jwt);
                console.log("Brain prediction:", classes[payload.prediction]);
                localStorage.predictionToken = jwt;
                localStorage.profilePicture = b64;
                setProfilePicture();
                unload();
            });
        }
    });

});

function setProfilePicture() {
    if (localStorage.profilePicture && localStorage.predictionToken) {
        $(".profile-picture-container").css("background-image", "url('" + localStorage.profilePicture + "')");
    }
}

function load() {
    $('.profile-picture-container').addClass('dimmed');
}

function unload() {
    $('.profile-picture-container').removeClass('dimmed');
}
