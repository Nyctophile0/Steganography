//Encode File validation
function encodefilevalidation() {
    var file = document.getElementById('encodefile').files[0];
    var fileinput = document.getElementById('encodefile');
    var filepath = fileinput.value;
    var allowedextension = /(\.jpg|\.jpeg)$/i;

    var height = file.naturalHeight;
    console.log(height)
    if (!allowedextension.exec(filepath)) {
        alert('PLease upload only jpg/jpeg files.');
        fileinput.value = '';
        return false;
    }

    else {
        //Image Preview
        if (fileinput.files && fileinput.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                document.getElementById('encodeimagePreview').innerHTML = '<br/><p><strong>Image Preview</strong></p><img src="'+e.target.result+'">';
            };
            reader.readAsDataURL(fileinput.files[0]);
        }
    }
    // write it before preview so that image does not preview if any error
    /*var reader = new FileReader();
    reader.onload = function(event) {
        var image = new Image();
        image.onload = function() {
            var width = this.naturalWidth;
            var height = this.naturalHeight;
            if (width > 100 || height > 100) {
                alert('The image must be at least 100 pixels wide and 100 pixels tall.');
                fileinput.value = '';
                return false;
            } 
            else {
                alert('Image dimensions: ' + width + ' x ' + height);
            }
        };
        image.src = event.target.result;
    };
    reader.readAsDataURL(file);*/
}

// Decode File validation
function decodefilevalidation() {
    var file = document.getElementById('decodefile').files[0];
    var fileinput = document.getElementById('decodefile');
    var filepath = fileinput.value;
    var allowedextension = /(\.jpg|\.jpeg|\.png)$/i;

    if (!allowedextension.exec(filepath)) {
        alert('Please upload only jpg/jpeg/png files.');
        fileinput.value = '';
        return false;
    }

    else {
        //Image Preview
        if (fileinput.files && fileinput.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                document.getElementById('decodeimagePreview').innerHTML = '<br/><p><strong>Image Preview</strong></p><img src="'+e.target.result+'">';
            };
            reader.readAsDataURL(fileinput.files[0]);
        }
    }
}

function formvalidation() {
    
    console.log("validation function.")
    msg = document.getElementById('textarea1').value;
    file = document.getElementById('encodefile').files[0];
    
    if (file == null || file == undefined) {
        alert("Please upload any file.");
        event.preventDefault();
        return false;
    }
    
    else if(msg.trim() == "") {
        alert('Message box cannot be empty.');
        event.preventDefault();
        return false;
    }

    return true;
}

/* remove return from view first
document.getElementById('encode_button').onclick = function() {
    document.getElementById('encodeimagePreview').style.display = "none";
}; */

/*
// preventdefault used to prevent the form from being submitted automatically, as we want to perform our validation first
document.getElementById('form1').addEventListener("submit", function(event) {
    event.preventDefault();*/