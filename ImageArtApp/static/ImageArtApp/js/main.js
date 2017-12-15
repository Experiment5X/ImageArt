// this is the id of the form
$(document).ready(function() {
    $("#image-gen-form").submit(function (e) {
        $.ajax({
            type: "POST",
            url: "/",
            data: $("#image-gen-form").serialize(), // serializes the form's elements.
            /*beforeSend: function () {
                $("#image-art").attr("src", "/static/ImageArtApp/ball-interwind-preloader.svg");
            },*/
            success: function (data) {
                d = new Date();
                $("#image-art").attr("src", "/static/ImageArtApp/image.png?" + d.getTime());
            }
        });
        e.preventDefault(); // avoid to execute the actual submit of the form.
    });
});