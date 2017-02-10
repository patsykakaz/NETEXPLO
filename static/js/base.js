


$(document).ready(function(){
    // NavBar();
    FullScreen();
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
            $("#home_video video").get(0).play();
        }else{
            $('.navbar').addClass('navbar-deploy');
            $("#home_video video").get(0).pause();
        }
        // !Gestion du LOGO
    });
// NAVBAR FOLD && UNFOLD