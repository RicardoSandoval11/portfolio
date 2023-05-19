document.addEventListener('DOMContentLoaded', function(event) {

    const menuBtn = document.querySelector('#menu-btn');

    const navBar = document.querySelector('#nav-menu');

    const navBarOpenClose = () => {
        const navBarHeight = window.innerHeight - 60;
        navBar.style.height = `${navBarHeight}px`;
        if(navBar.style.display === 'none' || navBar.style.display === ''){
            navBar.classList.remove('animate__animated', 'animate__fadeOutLeft', 'animate__faster');
            navBar.classList.add('animate__animated', 'animate__fadeInLeft', 'animate__faster');
            navBar.style.display = 'flex';
        }else{
            navBar.classList.remove('animate__animated', 'animate__fadeInLeft', 'animate__faster');
            navBar.classList.add('animate__animated', 'animate__fadeOutLeft', 'animate__faster');
            setTimeout(() => {
                navBar.style.display = 'none';
            },500);
        }
    }

    menuBtn.addEventListener('click', navBarOpenClose);

    
    // projects
    const projectBtn = document.querySelector('#project-btn');
    const projectOptions = document.querySelector('#project-categories');

    const onOpenProjectsMenu = () => {
        console.log('hola');
        const projectOptionsHeight = window.innerHeight - 60;
        projectOptions.style.height = `${projectOptionsHeight}px`;
        projectOptions.classList.remove('animate__animated', 'animate__fadeOutLeft', 'animate__faster');
        projectOptions.classList.add('animate__animated', 'animate__fadeInLeft', 'animate__faster');
        projectOptions.style.display = 'flex';
        
    }

    const pick = document.querySelector('.pick');
    const menu = document.querySelector('.project-menu');
    let timeout;

    const onOpenProjectsMenuByHover = () => {

        pick.style.display = 'block';
        menu.style.display = 'flex';
        clearTimeout(timeout);
    }

    const onHideProjectMenu = () => {
        timeout = setTimeout(() => {
            pick.style.display = 'none';
            menu.style.display = 'none';
          }, 500);
    }

    // project details event
    const imgBackground = document.querySelector('#bg-zoom-img');
    const image = document.querySelector('#image-zoom');
    const closeImgBtn = document.querySelector('#close-img-btn');
    const projectViewImgs = document.querySelectorAll('#img-details');

    const closeImgZoom = () => {
        imgBackground.style.display = 'none';
        image.src = '';
        image.alt = '';
    }

    closeImgBtn.addEventListener('click', closeImgZoom);


    const onIncreaseImageSizeByHover = (event) => {
        const imgUrl = event.target.src;
        const imgAlt = event.target.alt;

        imgBackground.style.display = 'flex';
        image.src = imgUrl;
        image.alt = imgAlt;
    }

    // set initial state when window is resieze
    const setInitialState = () => {
        const windowWidth = window.innerWidth;

        if(windowWidth > 800){
            navBar.classList.remove('animate__animated', 'animate__fadeOutLeft', 'animate__faster');
            menu.classList.remove('animate__animated', 'animate__fadeOutLeft', 'animate__faster');
            navBar.style.display = 'flex';
            menu.style.display = 'none';
            menu.style.height = 'max-content';
        }else{
            navBar.style.display = 'none';
            navBar.classList.remove('initialStateHeader');
            const navBarHeight = window.innerHeight - 60;
            navBar.style.height = `${navBarHeight}px`;
        }

        if(window.innerWidth > 800){
            projectBtn.removeEventListener('click', onOpenProjectsMenu);
            projectBtn.addEventListener('mouseover', onOpenProjectsMenuByHover);
            menu.addEventListener('mouseover', onOpenProjectsMenuByHover);
            projectBtn.addEventListener('mouseout', onHideProjectMenu);
            menu.addEventListener('mouseout', onHideProjectMenu);
        }else{
            projectBtn.removeEventListener('mouseover', onOpenProjectsMenuByHover);
            menu.removeEventListener('mouseover', onOpenProjectsMenuByHover);
            projectBtn.removeEventListener('mouseout', onHideProjectMenu);
            menu.removeEventListener('mouseout', onHideProjectMenu);
            projectBtn.addEventListener('click', onOpenProjectsMenu);
        }

        // project details images
        if(projectViewImgs != null && window.innerWidth > 800){
            projectViewImgs.forEach(projectImg => {
                projectImg.addEventListener('mouseover', onIncreaseImageSizeByHover);
            });
        }else if(projectViewImgs != null && window.innerWidth < 800){
            projectViewImgs.forEach(projectImg => {
                projectImg.removeEventListener('mouseover', onIncreaseImageSizeByHover);
            });
        }

    }

    // initial state
    if(window.innerWidth > 800){
        // projects menu
        projectBtn.removeEventListener('click', onOpenProjectsMenu);
        projectBtn.addEventListener('mouseover', onOpenProjectsMenuByHover);
        menu.addEventListener('mouseover', onOpenProjectsMenuByHover);
        projectBtn.addEventListener('mouseout', onHideProjectMenu);
        menu.addEventListener('mouseout', onHideProjectMenu);

        // project image zoom effect
        if(projectViewImgs != null){
            projectViewImgs.forEach(projectImg => {
                projectImg.addEventListener('mouseover', onIncreaseImageSizeByHover);
            });
        }

    }else{
        // projects menu
        projectBtn.removeEventListener('mouseover', onOpenProjectsMenuByHover);
        menu.removeEventListener('mouseover', onOpenProjectsMenuByHover);
        projectBtn.removeEventListener('mouseout', onHideProjectMenu);
        menu.removeEventListener('mouseout', onHideProjectMenu);
        projectBtn.addEventListener('click', onOpenProjectsMenu);

        if(projectViewImgs != null){
            projectViewImgs.forEach(projectImg => {
                projectImg.removeEventListener('mouseover', onIncreaseImageSizeByHover);
            });
        }

    }


    window.addEventListener('resize', setInitialState);

    const returnNavBarOptions = document.querySelector('#return-navbar-btn');

    const onReturnNavBarOptions = () => {
        projectOptions.classList.remove('animate__animated', 'animate__fadeInLeft', 'animate__faster');
        projectOptions.classList.add('animate__animated', 'animate__fadeOutLeft', 'animate__faster');
        setTimeout(() => {
            projectOptions.style.display = 'none';
        },500);
    }

    returnNavBarOptions.addEventListener('click', onReturnNavBarOptions);



});

