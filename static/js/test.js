

$(document).ready(function(){

    // rapport = $(window).width()+$(window).height();
    // rapportVideo = $('#home_video video').width()/$('#home_video video').height();

    // $('#home_video').height($(window).height());

    // $('#home_video video').get(0).play();

    // if(){
// 
    // }

    // $.when(X).then(function(){
    //     // console.log($('#home_video video').height());
    //     console.log($('#home_video video').width());
    //     console.log(($('#home_video video').width()-$('#home_video').width())/2);
    //     // $('#home_video video').css('right',($('#home_video video').width()-$('#home_video').width())/2);
    // });
});



// var vid = document.getElementById("bgvid");
// var pauseButton = document.querySelector("#polina button");

// if (window.matchMedia('(prefers-reduced-motion)').matches) {
//     vid.removeAttribute("autoplay");
//     vid.pause();
//     pauseButton.innerHTML = "Paused";
// }

// function vidFade() {
//   vid.classList.add("stopfade");
// }

// vid.addEventListener('ended', function()
// {
// // only functional if "loop" is removed 
// vid.pause();
// // to capture IE10
// vidFade();
// }); 


// pauseButton.addEventListener("click", function() {
//   vid.classList.toggle("stopfade");
//   if (vid.paused) {
//     vid.play();
//     pauseButton.innerHTML = "Pause";
//   } else {
//     vid.pause();
//     pauseButton.innerHTML = "Paused";
//   }
// })


function fillNET(color){
    console.log($('._NET_').length);
    $('._NET_').css('fill',color);
}
function fillEXPLO(color){
    console.log($('._EXPLO_').length);
    $('._EXPLO_').css('fill',color);
}
function fillOBS(color){
    console.log($('._OBS_').length);
    $('._OBS_').css('fill',color);
}

