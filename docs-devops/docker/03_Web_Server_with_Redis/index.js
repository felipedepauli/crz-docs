const express = require('express')
const redis = require('redis')
const process = require('process')

const app = express()
const client = redis.createClient({
    host: 'redis-server',
    port: 6379
})
client.set('visits', 0)

app.get('/', (req, res) => {
    client.get('visits', (err, visits) => {
        client.set('visits', parseInt(visits) + 1)
        if (visits == 1) {
            process.exit(1)
        }
        res.send('Number of visits is ' + visits)
    })
})

app.listen(8081, () => {
    console.log('Listening on port 8081')
})

client.on('connect', () => {
    console.log('Redis client connected');
});

client.on('error', (err) => {
    console.log('Redis client error:', err);
});
