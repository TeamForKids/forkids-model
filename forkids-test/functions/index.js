const functions = require("firebase-functions");

const app = require('express')();
app.get('/test/', (req, resp) => {
    resp.json({ type: 'test', data: 'Testdata' });
});

const api = functions.https.onRequest(app);

module.exports = {
    api
}