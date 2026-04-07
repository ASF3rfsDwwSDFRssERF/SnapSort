document.addEventListener('DOMContentLoaded', () => {
    // Intersection Observer for scroll animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Select all elements that need formatting
    const elementsToAnimate = document.querySelectorAll('.fade-in');
    
    elementsToAnimate.forEach(el => {
        observer.observe(el);
    });
    
    // Download button click animation (only on download page)
    const dlBtn = document.getElementById('direct-download-btn');
    if (dlBtn) {
        dlBtn.addEventListener('click', function(e) {
            // Optional: visual feedback
            const originalText = this.innerHTML;
            this.innerHTML = '<i class="fa-solid fa-spinner fa-spin" style="margin-right: 8px;"></i> Downloading...';
            this.style.pointerEvents = 'none';
            
            setTimeout(() => {
                this.innerHTML = '<i class="fa-solid fa-check" style="margin-right: 8px;"></i> Downloaded';
                this.style.background = 'linear-gradient(90deg, #10b981, #34d399)';
            }, 1500);
            
            setTimeout(() => {
                this.innerHTML = originalText;
                this.style.background = '';
                this.style.pointerEvents = 'auto';
            }, 4000);
        });
    }
});
