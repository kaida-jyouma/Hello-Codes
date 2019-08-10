using System;
using static System.Console;
public class lcm{
    public static int lcm2(int x, int y = 1){
        var c = 1;
        while (true){
            if ((x * c) % y == 0){
                return x * c;
                break;
            }
            c ++;
        }
    }
    public static void Main(){
        WriteLine(lcm2(20, 35));
    }
}
