// import json array file to elasticsearch using bulk api
// adapted from stiekel/jsonArrayToElasticsearch.js
// https://gist.github.com/stiekel/b183b5473ac7e9031c5428a0be138e69

// url of elasticsearch index's bulk endpoint
let endpoint = 'localhost:9200/singers_2/_bulk'
// json file with object array
let jsonFile = 'singers_si.json'

const fs = require('fs')
const { exec } = require("child_process");

console.log('json', jsonFile)
let data
try {
    data = JSON.parse(fs.readFileSync(jsonFile))
} catch (e) {
    console.log('read json file failed')
    process.exit()
}

console.log('read', data.length, 'line(s)')

let dataBinary = []

data.forEach((d, index) => {
    let idx = { index: { _id: index + 1 } }
    dataBinary.push(JSON.stringify(idx))
    dataBinary.push(JSON.stringify(d))
})

dataBinary = dataBinary.join('\n')
dataBinary += '\n'

fs.writeFileSync('result.json', dataBinary)

let cmd = `curl -s -H "Content-Type: application/x-ndjson" -XPOST ${endpoint} --data-binary '@result.json'`

console.log(cmd)
// exec(cmd)
exec(cmd, (error, stdout, stderr) => {
    if (error) {
        console.log(`error: ${error.message}`);
        return;
    }
    if (stderr) {
        console.log(`stderr: ${stderr}`);
        return;
    }
    console.log(`stdout: ${stdout}`);
})
