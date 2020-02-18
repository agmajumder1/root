const node_xml_stream = require('node-xml-stream');
const parser = new node_xml_stream();
const fs = require('fs');
const path = require('path');
require('events').EventEmitter.prototype._maxListeners = 1000;


//const srch = require('./SearchString.js');
//const lineReader = require('line-reader');

const fullname = [];
const value = [];
const commvalue = [];

/* CUSTOM LABELS */
//Parsing source XML to prog readable format
//function sourceXMLParse() {

function sourceXMLParse(){
	// Label Reading starts in custom labels   //To be updated to read any files
	try{
		
	fs.readdir('C:/BuildHughes/translation-tool/inputs/source_meta/standardValueSets', function(err,list){
    if(err) throw err;
    for(var i=0; i<list.length; i++)
    {
		let stream = fs.createReadStream('C:/BuildHughes/translation-tool/inputs/source_meta/standardValueSets/'+list[i], 'UTF-8');
		stream.pipe(parser);

		// temporary variables to construct final array
		let fname, vname, attr, t_name;

		// callback contains the name of the node and any attributes associated
		parser.on('opentag', function(name, attrs) {
			if(name === 'labels') {
				attr = attrs;
			}
			t_name = name;
		});

		// callback contains the API name within the node.
		parser.on('text', function(text) {
			if(t_name === 'fullName') {
				fname = text;
			}    
		});
		
		// callback contains the label value within the node.
		parser.on('text', function(text) {
			if(t_name === 'value') {
				vname = text;
			}    
		});

		// Creating the arrays
		parser.on('closetag', function(name) {
			if(name === 'labels') {
				fullname.push(fname);
				value.push(vname);
				commvalue.push('<!-- '+vname+' -->');
			}
		});
		
		// callback to create a temporary file after stream has finished
		let wstream = fs.createWriteStream('C:/BuildHughes/translation-tool/temp/StdValueSet.txt','UTF-8');
		parser.on('finish', function() {
		var i = 0;
		for (i=0;i<fullname.length;i++){
			wstream.write('API = '+fullname[i]+'\n');
			wstream.write('VAL = '+value[i]+'\n');
			wstream.write('COMM= '+commvalue[i]+'\n');
		}
		wstream.end();
		console.log('Parsed File created ---> translation-tool/temp/StdValueSet.txt');
		//Starting search in translation file
		searchTransValue(err,list[i]);
		console.log(list[i]);
		});
	}
	});
	
	} 	catch (e) {
			throw e;
		}
}

// Method to search whether API name is absent or whether label value is commented.
function searchTransValue(err,list){
	if (err) throw err;
	console.log('***Ashin'+list);
//	parser.on('finish', function() {
	console.log('Creating Output File ---> translation-tool/output/ Folder....');
// Label Search starts in translation file

var filepath = 'output/StdValueSet_Translation_Search_Errors.xls';
fs.createWriteStream(filepath);
var out = fs.createWriteStream(filepath,{ flags : 'a' });
out.write('Metadata Type\tTranslation Filename\tAPI Name\tValue\tError\tSuggested Fix\n', 'UTF-8');
		//Reading translation file
		fs.readdir('inputs/translation_files/standardValueSetTranslations', (err, files) => {
		files.forEach(file => {
			console.log('Ashin'+file+'///'+list);
			if(file.includes(list)){
				console.log('Ashin'+file);
			fs.readFile('inputs/translation_files/standardValueSetTranslations/'+file, (err, data) => {
			var j = 0;
				for(j=0;j<fullname.length;j++){
				var api = fullname[j];
				var val = value[j];
				var cval = commvalue[j];
				if (err) throw err;
				
				//API name absent in translation.
				else if(!(data.includes(api))){
						var str = 'Custom Label\t'+file+'\t'+api+'\t'+val+'\tAPI Name not found in translation file\tPlease add to translation file\n';
						out.write(str, 'UTF-8');
					}
				//Label value commented.
				else if(data.includes(cval)){
						var str = 'Custom Label\t'+file+'\t'+api+'\t'+val+'\tValue commented in translation file\tPlease update translation in translation file\n';
						out.write(str, 'UTF-8');
					}
				//label value commented with API name as commented label value.
				else if(data.includes('<!-- '+api+' -->')){
						var str = 'Custom Label\t'+file+'\t'+api+'\t'+val+'\tAPI name or Value commented in translation file\tPlease update translation file\n';
						out.write(str, 'UTF-8');
					}
				}
				});
			}
			});
		});
		return;
}

sourceXMLParse();


// Label Checking starts in translation file
/*

sourceXMLParse().then(()=>{
}).catch((e)=>console.log(e));


let lhsstream = fs.createReadStream('tmp/ConsoleLabels.txt', 'UTF-8');
lhsstream.pipe(parser);
parser.on('text', function(text) {
	//console.log(text);
	fs.readFile('rhs/es_CO.translation', function (err, data) {
		if (err) throw err;
		if(data.includes(text)){
			//SKIP
		}
		else{
		console.log(text+'----->NOT PRESENT');
		}
	});	
});
*/