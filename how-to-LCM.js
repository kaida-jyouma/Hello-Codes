function lcm(x, y){
    y = y || 1;
    var c = 1;
    while (true){
        if ((x * c) % y === 0) return x * c;
        c ++;
    }
}
console.log(lcm(10, 18));
