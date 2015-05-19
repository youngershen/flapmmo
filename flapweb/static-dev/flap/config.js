(function(document, window){

    if(!window.Flap)
    {
        window.Flap = {};
    }

    var flap = window.Flap;
    var config = {};
    var asserts = {};
    flap.config = config;
    flap.asserts = asserts;

    asserts.bird = 'static/images/flap/bird.png';
    asserts.add_to_leaderboard = 'static/images/flap/add-to-leaderboard.png';
    asserts.background = 'static/images/flap/background.png';
    asserts.ground = 'static/images/flap/ground.png';
    asserts.logo = 'static/images/flap/logo.png';
    asserts.pipe = 'static/images/flap/pipe.png';
    asserts.restart = 'static/images/flap/restart.png';
    asserts.score = 'static/images/flap/score.png';
    asserts.share = 'static/images/flap/share.png';

})(document, window);