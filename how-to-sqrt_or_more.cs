using System;
public class program{
	// べき乗を関数化
	public static double pow(double x, int y){
		return Math.Pow(x, y);
	}
	// 開平法 (x => n乗根を求めたい数, y => n);
	public static double rt(int x, int y){
		var num = x;
		double prm = 0;
		for (var i=0;i<16;i++){
			double ct = pow(10, -(i));
			while (pow(prm, y) < num){
				prm += ct;
			}
			prm -= ct;
		}
		return prm;
	}
	// 出力
	public static void Main(){
		//入力値は "2 3" <=2の3条を求める
		var j = Console.ReadLine();
		Console.WriteLine(" in: " + j);
		string[] nums = j.Split(' ');
		Console.WriteLine("out: " + rt(int.Parse(nums[0]), int.Parse(nums[1])));
	}
}
