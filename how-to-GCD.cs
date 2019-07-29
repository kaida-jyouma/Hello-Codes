using System;
using System.Collections.Generic;
public class Programs{
    public static int gcd(int x, int y = 1){
        var xdiv = new List<int>();
        var ydiv = new List<int>();
        for (var i=1;i<=x;i++) if (x % i == 0) xdiv.Add(i);
        for (var j=1;j<=y;j++) if (y % j == 0) ydiv.Add(j);
        int retgcd = 0;
        foreach(int k in xdiv) if (ydiv.Contains(k)) retgcd = k;
        return retgcd;
    }
    public static void Main(){
        Console.WriteLine(gcd(15, 20));
    }
}
