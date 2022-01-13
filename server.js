'use strict';

const express = require('express');
const {execSync} = require('child_process');
const {exec} = require('child_process');
const bodyParser = require('body-parser');

const PORT = 8080;
const HOST = '0.0.0.0';

const app = express();
app.use(bodyParser.json());

app.get('/demo', (req, res) => {
	execSync('python3 ./commands/demoCommand.py', (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Executing demo");
});

app.post('/move', (req, res) => {
    execSync(`python3 ./commands/move.py ${req.body.x} ${req.body.y} ${req.body.z} ${req.body.r}`, (error, stdout, stderr) => {
    console.log(`${req.body.x} ${req.body.y} ${req.body.z} ${req.body.r}`);
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Arm movement sent")
});

app.post('/screw', (req, res) => {
    execSync(`python3 ./commands/screw.py ${req.body.deg}`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Arm screwing motion sent")
});

app.post('/wait', (req, res) => {
    execSync(`python3 ./commands/wait.py ${req.body.time}`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Wait command sent")
});

app.get('/clearAlarms', (req, res) => {
    execSync(`python3 ./commands/clearAlarms.py`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Clearing alarms")
});

app.get('/home', (req, res) => {
    execSync(`python3 ./commands/home.py`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Homing Dobot")
});

app.get('/pose', (req, res) => {
    exec(`python3 ./commands/getPose.py`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    res.json(stdout.slice(0,-1));
    });
});

app.get('/at1', (req, res) => {
    execSync(`python3 ./commands/at1.py`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Performing Assembly Task 1")
});

app.get('/at4', (req, res) => {
    execSync(`python3 ./commands/at4.py`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Performing Assembly Task 4")
});

app.get('/grip', (req, res) => {
    execSync(`python3 ./commands/grip.py`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Gripping")
});

app.get('/ungrip', (req, res) => {
    execSync(`python3 ./commands/ungrip.py`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Ungripping")
});

app.post('/placePart', (req, res) => {
    exec(`sh ./commands/placePart.sh ${req.body.x1} ${req.body.y1} ${req.body.z1} ${req.body.r1}  ${req.body.x2} ${req.body.y2} ${req.body.z2} ${req.body.r2}`, (error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    });
    res.send("Placing part")
});

app.listen(PORT, HOST);
console.log(`running on http://${HOST}:${PORT}`);
