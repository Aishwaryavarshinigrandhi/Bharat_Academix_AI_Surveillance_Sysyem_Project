setInterval(() => {
    fetch('/alerts')
        .then(response => response.json())
        .then(data => {
            location.reload();
        });
}, 5000);
