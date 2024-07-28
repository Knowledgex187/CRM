document.addEventListener('DOMContentLoaded', function() {
    const movieThumbnails = document.querySelectorAll('.customer-list');

    movieThumbnails.forEach(thumbnail => {
        const videoSrc = thumbnail.getAttribute('data-video');
        const video = document.createElement('video');

        if (videoSrc) {
            video.src = videoSrc;
            video.loop = true;
            video.muted = true;
            thumbnail.appendChild(video);
            
            thumbnail.addEventListener('mouseover', () => {
                video.style.display = 'block';
                video.play();
            });

            thumbnail.addEventListener('mouseout', () => {
                video.style.display = 'none';
                video.pause();
            });
        }
    });
});
