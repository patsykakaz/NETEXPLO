


$(document).ready(function(){
    // NavBar();
    FullScreen();
    fillNET(customColor);
    fillOBS(customColor);
    $('.navbar-toggle').click(function(){
        if($('.navbar').hasClass('navbar-deploy')){
            console.log('fake-deploy');
            if($(document).scrollTop() < navbarTrigger){
                $('.navbar').addClass('navbar-fake-deploy');
                DefaultExploColor();
            }else{
                $('.navbar').removeClass('navbar-fake-deploy');
            }
        }
        else if(!$('.navbar').hasClass('navbar-fake-deploy')){
            $('.navbar').addClass('navbar-fake-deploy');
            fillEXPLO('#373d40');
        }else{
            $('.navbar').removeClass('navbar-fake-deploy');
            DefaultExploColor();
        }
    });
});

$(window).resize(function(){
    FullScreen();
});

function NavBar(){
    // if($(window).scroll
}

function FullScreen(){
    $('.fullScreen').height($(window).height()).width('100%');
}



// NAVBAR FOLD && UNFOLD
    navbarTrigger = 120;
    if($('#main').length > 0){
        small_width = $('#main').width()+'px';
    }else{
        small_width = '1000px';
    }
    // On appelle une fois la fonction au debut avant scroll()
    // -> evite les conflits css ultérieurs
    $(document).ready(function(){
        if($(document).scrollTop() < navbarTrigger){
            $('.navbar').removeClass('navbar-deploy');
            if($('.navbar-collapse').hasClass('in')){
                $('.navbar').addClass('navbar-fake-deploy');
                FillDark();
            }
        }else{
            $('.navbar').addClass('navbar-deploy');
        }
        if($(document).outerWidth() >= 1150 && $('.navbar').hasClass('navbar-deploy')){
            $('.navbar .container-fluid').css('max-width',small_width);
        }
    });

    $(document).scroll(function(){
        if($(document).scrollTop() < navbarTrigger){
            $('.navbar').removeClass(' navbar-deploy');
            $("video").get(0).play();
            // $("video").css('opacity',1);
            if($('.navbar-collapse').hasClass('in')){
                $('.navbar').addClass('navbar-fake-deploy');
                FillDark();
            }
        }else{
            $('.navbar').addClass('navbar-deploy');
            if($(document).scrollTop() > navbarTrigger+$(window).height()*.5){
                $("video").get(0).pause();
                // $("video").css('opacity',.3);
            }else{
                $("video").get(0).play();
                // $("video").css('opacity',1);
            }
        }
        // !Gestion du LOGO
    });
// !NAVBAR FOLD && UNFOLD




// SVG FUNCTIONS
function fillNET(color){
    // console.log($('._NET_').length);
    $('._NET_').css('fill',color);
}
function fillEXPLO(color){
    // console.log($('._EXPLO_').length);
    $('._EXPLO_').css('fill',color);
}
function fillOBS(color){
    // console.log($('._OBS_').length);
    $('._OBS_').css('fill',color);
}
function FillDark(){
    fillEXPLO('#373d40');
}
function FillWhite(){
    fillEXPLO('#FFFFFF');
}
function DefaultExploColor(){
    if($('.navbar-collapse').hasClass('dark')){
        fillEXPLO('#373d40');
        // console.log('filling with black');
    }else{
        fillEXPLO('#FFFFFF');
        // console.log('filling with white');
    }
}
// !SVG FUNCTIONS