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