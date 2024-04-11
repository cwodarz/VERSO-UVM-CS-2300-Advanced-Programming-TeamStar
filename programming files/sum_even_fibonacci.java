// Bugs introduced: if statement & int temp declaration
// By IC

public class sum_even_fibonacci {
    public static void main(String[] args) {
        int a = 0, b = 1;
        int sumEven = 0;
        while (b < 4000000) {
            if if (b % 2 == 0) {  // should be: if (b % 2 == 0) {
                sumEven += b;
            }
            int temp = b;  // should be int temp = b;
            b = a + b;
            a = temp;
        }
        System.out.println(sumEven);
    }
}

// answer should be 4613732
