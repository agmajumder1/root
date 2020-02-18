const node_xml_stream = require('node-xml-stream');
const parser = new node_xml_stream();
const fs = require('fs');
const lineReader = require('line-reader');
//const createCsvWriter = require('csv-writer').createObjectCsvWriter;
/*const csvWriter = createCsvWriter({
  path: 'output/output.csv',
  header: [
    {id: 'filename', title: 'File Name'},
    {id: 'apiname', title: 'API Name'},
    {id: 'labelname', title: 'Label Value'}
  ]
});*/

async function searchTransValue(api, val){
/* CUSTOM LABELS */
	console.log('Creating Output File ---> C:/BuildHughes/translation-tool/output/output.txt');
// Label Search starts in translation file
	fs.writeFile('output/output.txt','<==========NOT FOUND IN TRANSLATION FILE==========>', (err) => {
		if (err) throw err;});
		lineReader.eachLine('tmp/ConsoleLabels.txt', function(line) {
		fs.readFile('rhs/es_CO.translation', (err, data) => {
			if (err) throw err;
			if(!(data.includes(line))){
				//console.log(line+'-----> PRESENT\n');
					fs.appendFile('output/output.txt','\nAPI NAME ===> '+line, (err) => {
					if (err) throw err;
					});
				// success case, the file was saved
				}
			});	
		});	
}
	
/*	
const data = [
  {
    name: 'John',
    surname: 'Snow',
    age: 26,
    gender: 'M'
  }, {
    name: 'Clair',
    surname: 'White',
    age: 33,
    gender: 'F',
  }, {
    name: 'Fancy',
    surname: 'Brown',
    age: 78,
    gender: 'F'
  }
];

csvWriter
  .appendRecords(data)
  .then(()=> console.log('The CSV file was written successfully')); */