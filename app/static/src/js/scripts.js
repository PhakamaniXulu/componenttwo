$(document).ready(function() {
    $(".nav .nav-item").click(function () {
        $(".nav .nav-item").removeClass("btn-primary").addClass("btn-default");
        // $(".tab").addClass("active"); // instead of this do the below 
        $(this).removeClass("btn-default").addClass("btn-primary");   
    });
    });