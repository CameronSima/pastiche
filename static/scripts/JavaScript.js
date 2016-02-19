var selectLinesAABB = document.getElementById('selectLinesAABB');
var selectLinesABAB = document.getElementById('selectLinesABAB');
var ABABBox = document.getElementById('ABABBox');
var AABBBox = document.getElementById('AABBBox');

// Allow only one poetic form to be selected. If 'free verse'
// is selected, show the dropdown allowing the user to choose
// how many lines should be generated.

$('input.poeticForms').on('change', function () {
    $('input.poeticForms').not(this).prop('checked', false);
    if (AABBBox.checked) {
        
        selectLinesAABB.style.visibility = 'visible';
    } else {
        selectLinesAABB.style.visibility = 'hidden';
    };

    if (ABABBox.checked) {
        
        selectLinesABAB.style.visibility = 'visible';
    } else {
        selectLinesABAB.style.visibility = 'hidden';
    };
});

// Show animated loading image while 
function loading() {
    var loading_message = document.getElementById("loading_message");
    loading_message.innerText = "Please wait while your poem is being written...";
    
    function pulsate() {
        
        $("#loading_message").animate({ opacity: 0.4 }, 1000, 'linear')
                             .animate({ opacity: 1 }, 1000, 'linear', pulsate);
        
    }
    pulsate();
}

// Make sure the user has selected input
// submit button is pressed
function ensure_selection() {
        
}

function mark_voted(id) {
    
}

function display_votes(votes, id) {
    var likes = document.getElementById('count' + id);
    likes.innerText = 'Likes: ' + votes;
}

function vote(id, direction) {
    var element = document.getElementById('count' + id);
    if (element.className === 'upvoted') {
        if (direction == 'up') {
            direction = 'down';
            element.className = 'unvoted';
        } else if (direction == 'down') {
            direction = 'downdown';
            element.className = 'downvoted';
            }
    } else if (element.className == 'downvoted') {
        if (direction == 'down') {
            direction = 'up';
            element.className = 'unvoted';
        } else if (direction == 'up') {
            direction = 'upup';
            element.className = 'upvoted';
        }
    } else if (element.className == 'unvoted') {
        if (direction == 'up') {
            element.className = 'upvoted';
        } else if (direction == 'down') {
            element.className = 'downvoted';
        }
    }
        var req = new XMLHttpRequest();
        req.onreadystatechange = function () {
            if (req.readyState === XMLHttpRequest.DONE) {
                display_votes(req.responseText, id);
            }
        }
        req.open("PUT", "http://localhost:8000/vote/" + id + "/" + direction, true);
        req.send();
        lastVote = direction;
}

function randomAuthors() {
    var authors = document.getElementsByClassName('authors');
    for (var i = 0; i < authors.length; i++) {
        if (authors[i].name != 'Random') {
            authors[i].checked = false;
        }
    }
}

function notRandom() {
    var random = document.getElementById("Random");
    random.checked = false;
}


