/*================== scroll reveal =====================*/
ScrollReveal({
    
    /*reset: true,*/
    distance:'80px',
    duration: 1500,
    delay: 100

});

ScrollReveal().reveal('.home-content', { origin: 'top' });
ScrollReveal().reveal('.about-img', { origin: 'right' });
ScrollReveal().reveal('.home-content h1', { origin: 'right' });

/*================== typed js =====================*/

const typed = new Typed('.multiple-text',{
    strings: ['Frontend Developer', 'Backend Developer'],
    typeSpeed:50,
    backSpeed:50,
    backDelay:50,
    loop:true

})


