import java.util.Scanner;

public class P1 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		int cases = input.nextInt();
		for (int i = 0; i < cases; i++) {
            int value = input.nextInt();
            if (value > -1){
                value -= 1
            }
            System.out.println(value)
		}
	}
}