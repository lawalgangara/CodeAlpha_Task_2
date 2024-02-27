$(document).ready(function(){

    var current_fs, next_fs, previous_fs; // Fieldsets
    var current = 1;
    var steps = $("fieldset").length;

    setProgressBar(current);

    $(".next").click(function(){
        // Get the current and next fieldsets
        current_fs = $(this).parent();
        next_fs = $(this).parent().next();

        // Add "active" class to the progress bar
        $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

        // Show the next fieldset with fade effect
        next_fs.fadeIn();
        // Hide the current fieldset with fade effect
        current_fs.hide();

        // Update the progress bar
        setProgressBar(++current);
    });

    $(".previous").click(function(){
        // Get the current and previous fieldsets
        current_fs = $(this).parent();
        previous_fs = $(this).parent().prev();

        // Remove "active" class from the progress bar
        $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

        // Show the previous fieldset with fade effect
        previous_fs.fadeIn();
        // Hide the current fieldset with fade effect
        current_fs.hide();

        // Update the progress bar
        setProgressBar(--current);
    });

    function setProgressBar(curStep){
        // Calculate the progress percentage
        var percent = parseFloat(100 / steps) * curStep;
        percent = percent.toFixed();
        // Update the progress bar width
        $(".progress-bar").css("width", percent + "%");
    }

    $(".submit").click(function(){
        // Implement form validation
        var isValid = true;

        // Example validation: Check if all input fields are filled
        $("input[type='text'], input[type='date']").each(function(){
            if(!$(this).val()){
                isValid = false;
                // Add error styling or message for empty fields
                $(this).addClass("error");
            }
            else{
                $(this).removeClass("error");
            }
        });

        // Return true to allow form submission if validation passes
        return isValid;
    });

});
