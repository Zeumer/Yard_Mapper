var i2c = require('i2c');

var address = 0x68;
var wire = new i2c(address, {device: '/dev/i2c-1'});

//wire.scan(function(err, data) { console.log(data[1])}); 

//wire.on('data', function(data){console.log(data)});

//wire.readByte(0x75, function(err,res){console.log(res)});

//wire.read(6, function(err, data){ 
//	console.log(data[0]);
//	console.log(data[4]);
//});

wire.readBytes(0x75,6,function(err,res){console.log(res)});
