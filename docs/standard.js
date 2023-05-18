const imgID = "mainPlayerVideo";
const thumbnailClass = "flow";
const floatButtonID = "FloatTop";
const notificationID = "ChangeNotification";
const videoTitleID = "videoname";
let sidebar = document.getElementById("stage-sidebar");
let floatButton = document.getElementById(floatButtonID);
let notification = document.getElementById(notificationID);
let videoTitle = document.getElementById(videoTitleID);
window.onscroll = function() {scrollFunction()};
window.onload = showImage('random');

function showImage(inim){
    console.log("inim: "+inim);
	let backFolder = "../"
    let chosen_one = document.getElementById(imgID);
    console.log("Getting Element... "+chosen_one);
    if (chosen_one == null) {
        console.log('top img element does not exist');
        return false;
        }
    if(inim == 'random') {
        let a = Math.floor(Math.random() * clipsList.length);
        let img = backFolder + video_source + clipsList[a] +".mp4";
        let imgthumb = backFolder + thumb_source + clipsList[a] + ".png";
        console.log("Random source is "+img);
        chosen_one.src = img;
        chosen_one.poster = imgthumb;
        insertTitle();
        return false;
    }
    chosen_one.src = backFolder + video_source + inim + ".mp4";
    chosen_one.poster = backFolder + thumb_source + inim + ".png";
    insertTitle();
    showChange();
}

function scrollFunction() {
    if (document.body.scrollTop > 360 || document.documentElement.scrollTop > 360) {
        floatButton.style.display = "block";
        return;
    }
    floatButton.style.display = "none";
    notification.style.display = "none";
    notification.style.animation = "initial";
}

function showChange() {
    if (document.body.scrollTop > 360 || document.documentElement.scrollTop > 360) {
        notification.style.display = "block";
        notification.style.opacity = "1";
        notification.style.animation = "fadeAway 3s ease 2s infinite both running";
    }
    return false;
}

function insertTitle() {
    const regeV = /\w+(?=.png)/i;
    const regeS = /([A-Z])/;
    let videoTitleName = document.getElementById(imgID).poster;
    let videoTitleInsert = regeV.exec(videoTitleName).toString();
    videoTitle.innerHTML = videoTitleInsert;
}
