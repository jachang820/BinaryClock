function dec_to_grey_code(dec) {
	let tens = (Math.floor(dec / 10)).toString(2);
	let ones = (dec % 10).toString(2);
	return [tens, ones];
}


function time_to_grey_code() {
	let d = new Date();
	let hour = dec_to_grey_code(d.getHours());
	hour = ("00" + hour[0]).slice(-2) + 
				 ("0000" + hour[1]).slice(-4);

	let minute = dec_to_grey_code(d.getMinutes());
	minute = ("000" + minute[0]).slice(-3) + 
					 ("0000" + minute[1]).slice(-4);

	let second = dec_to_grey_code(d.getSeconds());
	second = ("000" + second[0]).slice(-3) + 
					 ("0000" + second[1]).slice(-4);

	return (hour + minute + second).split("");
}


var timer = setInterval(function() {
	let time = time_to_grey_code();
	time.forEach((element, index) => {
		if (element == "1") 
			$('#clock_' + index.toString()).addClass("active")
		else
			$('#clock_' + index.toString()).removeClass("active")
	});
}, 200);

