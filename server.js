'use strict';

const express = require('express');
const {exec} = require('child_process');
const bodyParser = require('body-parser');

const PORT = 8080;
const HOST = '0.0.0.0';

const app = express();
app.use(bodyParser.json());

app.get('/demo', (req, res) => {
	exec('sh ./commands/demo_command.sh', (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("executing demo");
});

app.post('/move', (req, res) => {
    exec(`sh ./commands/move.sh ${req.body.x} ${req.body.y} ${req.body.z} ${req.body.r}`, (error, stdout, stderr) => {
    console.log(`${req.body.x} ${req.body.y} ${req.body.z} ${req.body.r}`);
    console.log(stdout);
    console.log(stderr);
    });
    res.send("arm movement sent")
});

app.post('/screw', (req, res) => {
    exec(`sh ./commands/screw.sh ${req.body.deg}`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("arm screwing motion sent")
});

app.post('/wait', (req, res) => {
    exec(`sh ./commands/wait.sh ${req.body.time}`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Wait command sent")
});

app.get('/clearAlarms', (req, res) => {
    exec(`sh ./commands/clearAlarms.sh`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("clearing alarms")
});

app.get('/home', (req, res) => {
    exec(`sh ./commands/home.sh`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Homing Dobot")
});

app.get('/pose', (req, res) => {
    exec(`sh ./commands/getpose.sh`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    res.json(stdout.slice(0,-1));
    });
});

app.get('/at1', (req, res) => {
    exec(`sh ./commands/at1.sh`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Performing Assembly Task 1")
});

app.get('/at4', (req, res) => {
    exec(`sh ./commands/at4.sh`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Performing Assembly Task 4")
});

app.get('/grip', (req, res) => {
    exec(`sh ./commands/grip.sh`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Gripping")
});

app.get('/ungrip', (req, res) => {
    exec(`sh ./commands/ungrip.sh`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Ungripping")
});

app.post('/placePart', (req, res) => {
    exec(`sh ./commands/place.sh ${req.body.x1} ${req.body.y1} ${req.body.z1} ${req.body.r1}  ${req.body.x2} ${req.body.y2} ${req.body.z2} ${req.body.r2}`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Placing Part")
});

app.listen(PORT, HOST);
console.log(`running on http://${HOST}:${PORT}`);
