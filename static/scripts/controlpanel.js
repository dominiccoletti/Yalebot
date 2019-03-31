document.getElementById('accept').onclick = function() {
    document.getElementById('add').disabled = !this.checked;
}

onclick = function(e) {
    if (e.target.tagName == 'BUTTON' && e.target.classList.contains('delete')) {
        if (confirm('Really delete bot?')) {
            var req = new XMLHttpRequest();
            req.open('POST', '/delete');
            req.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
            req.send(JSON.stringify({
                'bot_id': this.getAttribute('bot_id'),
                // TODO: this is not a very elegant way to get the token.
                'access_token': document.getElementsByName('access_token')[0].value,
            }));
        }
    }
}
