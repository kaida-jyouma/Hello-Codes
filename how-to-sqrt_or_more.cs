using System;
public class program{
	// tofunction "Math.Pow()"
	public static double pow(double x, double y){
		return Math.Pow(x, y);
	}
	// sqrt
	public static double rt(int x, int y = 2){
		var num = x;
		double prm = 0;
		for (var i=0;i<16;i++){
			double ct = pow(10, -(i));
			while (pow(prm, y) < num) prm += ct;
			prm -= ct;
		}
		return prm;
	}
	// 出力
	public static void Main(){
		var j = Console.ReadLine();
		Console.WriteLine(" in: " + j);
		string[] nums = j.Split(' ');
		Console.WriteLine("out: " + rt(int.Parse(nums[0]), int.Parse(nums[1])));
	}
}
