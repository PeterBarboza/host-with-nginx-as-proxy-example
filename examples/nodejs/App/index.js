const express = require('express')
const cors = require('cors')

const app = express()

app.use(cors({
    origin: '*'
}))

app.get('/hello', (req, res) => {
    res.json({
        hello: 'world',
        timestamp: new Date().toISOString()
    })
})

app.listen(3000, () => {
    console.log('Server is running on port 3000')
})