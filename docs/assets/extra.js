// Umami analytics loader for SafeAI-Aus.
(function () {
    'use strict';

    function loadAnalytics() {
        if (document.querySelector('script[src="https://cloud.umami.is/script.js"]')) {
            return;
        }

        const script = document.createElement('script');
        script.defer = true;
        script.src = 'https://cloud.umami.is/script.js';
        script.setAttribute('data-website-id', 'f228fe92-e13d-456d-92f8-018fac9d587c');

        const target = document.head || document.querySelector('head') || document.documentElement;
        target.appendChild(script);
    }

    loadAnalytics();

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', loadAnalytics, { once: true });
    }
})();
