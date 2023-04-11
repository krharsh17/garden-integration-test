const { app } = require('./index');

app.listen(process.env.PORT, '0.0.0.0', () => console.log('Frontend service started'));