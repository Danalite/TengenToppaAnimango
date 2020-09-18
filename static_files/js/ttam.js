/* Custom javascript for the site */

/* Archive image resize detection */
/* This function is used in the archive app to check if an image has been resized. */
function archiveSizeCheck() {
    let image = document.getElementById('archiveImage');
    if (image) {
        /* If image was null then archive item was a video. Video's can be viewed fullscreen via the controls, so
        * a re-size notification isn't needed. */
        if (image.clientWidth !== image.naturalWidth) {
            let messagesDiv = document.getElementById('messagesDiv');
            let resizeMessage = document.createElement('div');
            let messageText = 'This image has been re-sized! <a href="' + image.src + '">Click here</a> for the original image.'
            resizeMessage.className = 'alert alert-primary';
            resizeMessage.innerHTML = messageText;
            messagesDiv.appendChild(resizeMessage);
        }
    }
}

/* Error page divergence meter */
/* This function will generate a divergence meter string in the format 0.XXXXXX, it's used in the error pages. */
function writeDivergenceMeter() {
    let divergenceMeter = document.getElementById('divergenceMeter');
    let divergenceNumber = Math.random();
    divergenceMeter.innerText = divergenceNumber.toString().slice(0, 8);
}