window.onload=function colorBlocks() {
    var colors=new Array("#4D785C","#495A6A","#677564","#B87423","#6F3B2E","#DC661E");
    var max=colors.length - 1;
    var blocks=document.getElementsByClassName('block');
    for (var i = 0; i < blocks.length; i++) {
        blocks[i].style.color=colors[Math.floor(Math.random() * (max + 1))];
    }
};

function showSolution() {
if (document.getElementById("solution").style.display=="block") {
    document.getElementById("solution").style.display="none";
    }
else {
    document.getElementById("solution").style.display="block";
    }
};

$(function() {
    updatePhrases();
    setInterval(updatePhrases,5000);
});

LATEST_PHRASES_URL = '/blockbuilder/api/latest-phrases/'

function updatePhrases() {
    $.getJSON(LATEST_PHRASES_URL, function(data){
        var latestPhrases = $('#latestPhrases')
        latestPhrases.empty();
        $.each(data, function(i,items){
            var latestPhrase = $('<div class="phrase"></div>');
            latestPhrase.append('<a class="phrase-link" href="/blockbuilder/phrase/'+ items.pk + '">' + items.fields.phrase_text + '</a>');
            latestPhrases.append(latestPhrase);
        });
    });
}