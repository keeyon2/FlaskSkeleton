function high_var(){
    console.log("Time for Ajax Call");
    var interest_word = document.getElementById('interestingtextfield').value;
    console.log("Ajax call on " + interest_word);
    var request = $.ajax({
        type: "GET",
        url: "http://localhost:5000/HighVar/" + interest_word,
        contentType: "application/json",
        success: function(data)
        {
           start_display(data);
        },
    }); 
}


function start_display(info){
    console.log("In Start Display");
    console.log(info);
    document.getElementById('interestingtextfield').value = 'DOOD';
    console.log(info);
}
