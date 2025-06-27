window.onload = function() {
    const successAudio = new Audio('/static/success.mp3');
    const failAudio = new Audio('/static/fail.mp3');

    // Patch fetch to play sounds on API response
    const origFetch = window.fetch;
    window.fetch = async function() {
        try {
            const response = await origFetch.apply(this, arguments);
            if (response.ok) {
                successAudio.currentTime = 0;
                successAudio.play();
            } else {
                failAudio.currentTime = 0;
                failAudio.play();
            }
            return response;
        } catch (err) {
            failAudio.currentTime = 0;
            failAudio.play();
            throw err;
        }
    };

    const ui = SwaggerUIBundle({
        url: '/openapi.json',
        dom_id: '#swagger-ui',
        presets: [
            SwaggerUIBundle.presets.apis,
            SwaggerUIStandalonePreset
        ],
        layout: "StandaloneLayout"
    });
};
