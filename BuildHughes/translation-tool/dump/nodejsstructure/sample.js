const node_xml_stream = require('node-xml-stream');
const parser = new node_xml_stream();
const fs = require('fs');

/*
var trueLog = console.log;
console.log = function(msg) {
    fs.appendFile("tmp/ConsoleLabels.log", msg, function(err) {
        if(err) {
            return trueLog(err);
        }
    });
    //trueLog(msg); //uncomment if you want logs
}*/

// Label Reading starts in custom labels

// temporary variables to construct final object
let label = { 'labels': [] };
let fname/*,lang, protect, sdescription, val*/, attr, t_name;

// callback contains the name of the node and any attributes associated
parser.on('opentag', function(name, attrs) {
    if(name === 'labels') {
        attr = attrs;
    }
    t_name = name;
	//console.log('1st method : '+t_name);
});

// callback contains the name of the node.
parser.on('closetag', function(name) {
    if(name === 'labels') {
        label['labels'].push({ "fullName": fname/*, "language": lang, "protected": protect, "shortDescription": sdescription, "value": val*/ });
    }
});

// callback contains the text within the node.
parser.on('text', function(text) {
    if(t_name === 'fullName') {
        fname = text;
    }    
/*	if(t_name === 'language') {
        lang = text;
    }    
	if(t_name === 'protected') {
        protect = text;
    }    
	if(t_name === 'shortDescription') {
        sdescription = text;
    }    
	if(t_name === 'value') {
        val = text;
    }*/
});

// callback to do something after stream has finished
parser.on('finish', function() {
    console.log(label);
});

let stream = fs.createReadStream('lhs/CustomLabels.labels', 'UTF-8');
stream.pipe(parser);

/*
// Label Checking starts in translation file
parser.on('opentag', function(name, attrs) {
    if(name === 'labels') {
        attr = attrs;
    }
    t_name = name;
	//console.log('1st method : '+t_name);
});
*/


