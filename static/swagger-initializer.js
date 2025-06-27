window.onload = function () {
    const initAudio = new Audio('/static/init.mp3');
    const successAudio = new Audio('/static/success.mp3');
    const failAudio = new Audio('/static/fail.mp3');

    let audioEnabled = false;

    function enableAudioOnce() {
        audioEnabled = true;
        //initAudio.play();
        window.removeEventListener('click', enableAudioOnce);
    }
    window.addEventListener('click', enableAudioOnce);

    // Patch fetch to play sounds on API response
    const origFetch = window.fetch;
    window.fetch = async function () {
        try {
            const response = await origFetch.apply(this, arguments);
            console.log("Fetch intercepted:", response.status);
            if (audioEnabled) {
                if (response.ok) {
                    console.log("Success sound should play");
                    successAudio.currentTime = 0;
                    successAudio.play();
                } else {
                    console.log("Fail sound should play");
                    failAudio.currentTime = 0;
                    failAudio.play();
                }
            }
            return response;
        } catch (err) {
            if (audioEnabled) {
                console.log("Network fail sound should play");
                failAudio.currentTime = 0;
                failAudio.play();
            }
            throw err;
        }
    };

    SwaggerUIBundle({
        url: '/openapi.json',
        dom_id: '#swagger-ui',
        presets: [
            SwaggerUIBundle.presets.apis,
            SwaggerUIStandalonePreset
        ],
        layout: "StandaloneLayout"
    });
};
