// when DOM is ready & fully loaded!
$(document).ready(function () {
    // state of the rows, to see if all are open or closed
    // false = all closed
    // true = all open
    var are_all_open = false;

    $(".first_word").each(function () {
        var text = $(this).text(); // select text to edit
        var firstWord = text.trim().split(" ")[0]; // split the text in array of words and select first word
        var restOfText = text.substring(firstWord.length); // select all, except the selected word

        // set first word blue and add other part of the text to it
        $(this).html(
            '<b style="color: blue;">' + firstWord + "</b>" + restOfText // <b> = bold text!
        );
    });

    $(".scenario_word").each(function () {
        var text = $(this).text(); // select text to edit
        var firstWord = text.trim().split(" ")[0]; // split text in array of words and select first word
        var restOfText = text.substring(firstWord.length); // take the text, except the selected word

        // give red color to the first word, add the rest of the setence behind
        $(this).html(
            '<b style="color: red;">' + firstWord + "</b>" + restOfText // <b> = bold text!
        );
    });

    // open details of the row
    $(".main-row").click(function () {
        var classes = $(this).attr("class").split(" "); // select all classes of the row
        var lastClass = classes[classes.length - 1]; // last class = row indentification | example .row-1
        var openClass = ".detail-row." + lastClass; // element class wich needed to know, to find exact row to open
        var mainClass = ".main-row." + lastClass;  // element class wich needed to know, to indentify it as active or not.
        // if all rows are opened
        // are_all_open = state (see line 6)
        if (are_all_open) {
            $(".main-row").removeClass("active-row"); // remove active class on all rows when clicked one 
            $(".detail-row").removeClass("active-row");  // remove active class on all rows when clicked one 
            $(".detail-row").addClass("hidden"); // add hidden class to all detail-row elements
            are_all_open = false; // reset the state
            return; // end action/function
        }
        // Seleect all elements with the openClass
        var elements_to_open = $("#results-table-body").find(openClass);

        // Toggle .hidden class for detail row to open/close
        elements_to_open.toggleClass("hidden");

        // Toggle .active-row class
        $(this).toggleClass("active-row");
        elements_to_open.toggleClass("active-row");

        // close all open detail rows when opening another one (1 active class)
        $(".detail-row")
            .not(openClass)
            .addClass("hidden")
            .removeClass("active-row");
        $(".main-row").not(mainClass).removeClass("active-row");
    });

    // OPEN ALL details (button)
    $("#show_all_details").click(function () {
        are_all_open = true;
        $(".detail-row").each(function () {
            $(this).removeClass("hidden").addClass("active-row");
        });
        $(".main-row").each(function () {
            $(this).addClass("active-row");
        });
    });

    // CLOSE ALL details (button)
    $("#hide_all_details").click(function () {
        are_all_open = false;
        $(".detail-row").each(function () {
            $(this).addClass("hidden").removeClass("active-row");
        });
        $(".main-row").each(function () {
            $(this).removeClass("active-row");
        });
    });
});

var filterCheckboxes = $(".filter"); // select all filter checkboxes based on .filter class [Array of HTML elements]
filterCheckboxes.each(function () {
    // this = checkbox wich was been pressed
    $(this).change(function () {
        var resultType = $(this).attr("filter_status"); // status to filter
        var isChecked = $(this).is(":checked"); // is checked? [boolean]
        
        // select all elements with .row class, one by one [Array of HTML elements]
        $(".row").each(function () {
            var $row = $(this); // this = selected row [HTML element]
            // if row status and checkbox filter-status are equal, let's filter
            if ($row.attr("data-results").toLowerCase() === resultType.toLowerCase()) {
                if (isChecked) {
                    // if box is checked, then all the data wich contains same status will be shown
                    $row.removeClass("hidden");
                    if (!$row.next().hasClass("hidden")) {
                        $row.next().removeClass("hidden");
                    }
                    // keep the detail-row hidden when checking the box back on
                    if($row.hasClass("detail-row")){
                        $row.addClass("hidden");
                    }
                } else {
                    // when not checked, all the data wich doesn't follow the same status as the checkbox must be hidden
                    $row.addClass("hidden");
                    $row.removeClass("active-row");
                    $row.next().addClass("hidden");
                }
            }
        });
    });
});

// within every row, it's <tr class="detail-row"></tr> you can open/close extra log details in last sub row.
$(document).ready(function () {
    // click on the arrow (special utf8 text character), then open/close extra details
    $(".toggle-details").click(function () {
        var details = $(this).next(".more-details"); // select detail rows
        details.toggleClass("hidden");

        if (details.hasClass("hidden")) {
            $(this).html("&#9660;"); // Arrow down
        } else {
            $(this).html("&#9650;"); // Arrow up
        }
    });
});

// When DOM of document is fully loaded in, start JavaScript
$(document).ready(function () {
    // styles vars can be found within colors.css (public/css folder)
    var style = getComputedStyle(document.body); // select style within document
    var color_failed = style.getPropertyValue('--color-failed'); // search for style (css) variable
    var color_passed = style.getPropertyValue('--color-passed');
    var color_skipped = style.getPropertyValue('--color-skipped');
    var color_expected_failures = style.getPropertyValue('--color-expected-failures');
    var color_unexpected_passes = style.getPropertyValue('--color-unexpected-passes');
    var color_errors = style.getPropertyValue('--color-errors');
    var color_reruns = style.getPropertyValue('--color-reruns');
    var color_no_status = style.getPropertyValue('--color-no-status');

    // Data of the pie chart
    var data = {
        labels: ['Failed', 'Passed', 'Skipped', 'Expected failures', 'Unexpected passes', 'Errors', 'Reruns', 'No status'], // labels will be shown to us when hovering over the pie chart
        datasets: [{
            // legend of labels title
            label: 'Results',
            // select data
            data: [count_failed, count_passed, count_skipped, count_expected_failures, count_unexpected_passes, count_errors, count_reruns, count_nostatus],
            // set colors on data visuals
            backgroundColor: [
                color_failed,          
                color_passed,              
                color_skipped,          
                color_expected_failures,    
                color_unexpected_passes,    
                color_errors,               
                color_reruns,               
                color_no_status             
            ],
            borderWidth: 0 // no need to have (white) borders
        }]
    };

    // Opties voor de pie chart
    var options = {
        responsive: true,
        plugins: {
            legend: {
                display: false // no need to show the labels, when having the checkboxes showing us already kind of legend (+ count)
            },
            tooltip: { // if want to show the labels (legend)
                callbacks: {
                    label: function (tooltipItem) {
                        return tooltipItem.label + ': ' + tooltipItem.raw.toLocaleString();
                    }
                }
            }
        }
    };

    // Creëer een nieuw pie chart object
    var ctx = document.getElementById('myPieChart').getContext('2d'); // vanilla JS (not Jqeury) to select piechart element
    // build chart
    var myPieChart = new Chart(ctx, {
        type: 'pie',
        data: data,
        options: options
    });
});


// jQuery document ready function
$(document).ready(function() {
    // Selecteer alle elementen met de class '.total-duration'
    $('.total-duration').each(function() {
        var totalDurationElement = $(this);

        // Controleer of de tekst een decimaal bevat
        if (totalDurationElement.text().includes('.')) {
            // Haal het decimale deel op
            var text = totalDurationElement.text();
            var decimalPart = text.split('.')[1];

            // Controleer het aantal decimalen
            if (decimalPart.length > 2) {
                // Rond af naar 2 decimalen
                var roundedValue = parseFloat(text).toFixed(2);
                // Update de tekst in het element
                totalDurationElement.text(roundedValue);
            } else if (decimalPart === '0' || decimalPart === '00') {
                // Verwijder decimaal punt voor gehele getallen
                totalDurationElement.text(parseFloat(text));
            }
        }
    });
});
