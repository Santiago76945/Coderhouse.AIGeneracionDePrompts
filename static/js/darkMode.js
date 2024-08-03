document.getElementById('darkModeToggle').addEventListener('click', function() {
    const currentTheme = document.querySelector('link[rel="stylesheet"][href="/static/css/styles.css"]');
    if (currentTheme) {
        currentTheme.href = '/static/css/darkmode.css';
        document.getElementById('darkModeToggle').innerText = '🌞 Toggle Light Mode';
    } else {
        const lightTheme = document.querySelector('link[rel="stylesheet"][href="/static/css/darkmode.css"]');
        lightTheme.href = '/static/css/styles.css';
        document.getElementById('darkModeToggle').innerText = '🌙 Toggle Dark Mode';
    }
});

