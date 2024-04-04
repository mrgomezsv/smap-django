
    function openFileExplorer() {
        document.getElementById('image-input').click();
    }

    document.getElementById('image-input').addEventListener('change', function() {
        var file = this.files[0];
        var reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('selected-image').setAttribute('src', e.target.result);
        };
        reader.readAsDataURL(file);
    });

