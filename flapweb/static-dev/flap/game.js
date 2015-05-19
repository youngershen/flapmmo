(function(document, window){
    //var config = window.CONFIG;
    //
    //var renderer = new PIXI.WebGLRenderer(800, 600);
    //document.body.appendChild(renderer.view);
    //var stage = new PIXI.Container();
    //var birdTexture = PIXI.Texture.fromImage(config.asserts.bird);
    //var bird = new PIXI.Sprite(birdTexture);
    //
    //bird.position.x = 0;
    //bird.position.y = 0;
    //bird.scale.x = 2;
    //bird.scale.y = 2;
    //stage.addChild(bird);
    //
    //
    //var animate = function()
    //{
    //    requestAnimationFrame(animate);
    //
    //    bird.position.x += 1;
    //    renderer.render(stage);
    //};
    //
    //animate();


    if(!window.Flap)
    {
        window.Flap = {};
    }

    var flap = window.Flap;

    flap.init = function(width, height)
    {
        this.sprites = {};

        for(var i in this.asserts)
        {
            var src = this.asserts[i];
            this.sprites[i] = PIXI.Texture.fromImage(src);
        };

        this.render = PIXI.WebGLRenderer(width, height);
        this.stage = new PIXI.Container();
        document.appendChild(this.render.view);
    };

    flap.create_game = function(width, height)
    {
        this.init(width, height);
    }


})(document, window);