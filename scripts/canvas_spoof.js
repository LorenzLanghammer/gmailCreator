(function() {
    const offset = {offset};

    const originalToDataURL = HTMLCanvasElement.prototype.toDataURL;

    HTMLCanvasElement.prototype.toDataURL = function(...args) {
        const ctx = this.getContext("2d");
        const width = this.width;
        const height = this.height;
        const imageData = ctx.getImageData(0, 0, width, height);


        for (let i = 0; i < imageData.data.length; i += 4) {
            imageData.data[i]     = (imageData.data[i] + offset.r) & 255; // R
            imageData.data[i + 1] = (imageData.data[i + 1] + offset.g) & 255; // G
            imageData.data[i + 2] = (imageData.data[i + 2] + offset.b) & 255; // B
        }

        ctx.putImageData(imageData, 0, 0);
        return originalToDataURL.apply(this, args);
    };
})();
