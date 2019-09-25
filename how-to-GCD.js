function gcd(x, y){
    y = y || 1;
    var xdiv = [];
    var ydiv = [];
    for (var i=1;i<=x;i++) if (x % i === 0) xdiv.push(i);
    for (var j=1;j<=y;j++) if (y % j === 0) ydiv.push(j);
    var retgcd = 0;
    function isIndexOf(ln, ins){
        var ct = 0;
        for (i=0;i<ln.length;i++){if (ln[i] === ins){ct += 1;break;}}
        if (ct === 0){return false;}else{return true;}
    }
    for (var k=0;k<xdiv.length;k++){
        var k1 = xdiv[k];
        if (isIndexOf(ydiv, k1)){retgcd = k1;}
    }
    return retgcd;
}
