function sqrt(x, y){
    y = y || 2;
    var num = x;
    prm = 0;
    for (var i=0;i<16;i++){
		var ct = Math.pow(10, -(i));
		while (Math.pow(prm, y) < num) prm += ct;
		prm -= ct;
	}
	return prm;
}
console.log(sqrt(2));
