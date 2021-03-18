profile = document.querySelector(".pp");

new fullpage('#fullpage', {
	//options here
    autoScrolling:true,
    sectionsColor: ['#34495e', '#2C3A47', '#3B3B98', '#EAB543', '#34e5eb'],
    navigation: true,
    onLeave: (origin,destination,direction)=> {
        const section = destination.item;
        TweenMax.fromTo(section, 1, {opacity: 0}, {opacity: 1},'+=700');
        // const title = section.querySelector("h1");
        // const tl = new TimelineMax({delay : 0.5});
        // tl.fromTo(title, 0,5, { y : "50", opacity 0}, {y: 0, opacity: 1});
        }
});

window.onload = function() {

    var timeline = new TimelineMax();
    
    timeline.from(".name", 1, {x:-100},0)
            .from(".job", 1, {x:100, autoAlpha:0})
            .from(profile, 1, { scale: 0, ease: Back.easeOut.config(5)  })
            .from("#html", 0.5, {x:100, autoAlpha:0})
            .from("#css", 0.5, {x:100, autoAlpha:0})
            .from("#js", 0.5, {x:100, autoAlpha:0})
            .from("#python", 0.5, {x:100, autoAlpha:0})


}



