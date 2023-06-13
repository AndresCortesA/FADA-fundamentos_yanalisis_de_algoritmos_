import java.lang.Math;

public class MetodoIteracionTaller {
    public static void main(String[] args) {
        double n;
        for (int i = 0; i < 10; i++) {
            n = Math.pow(4, i);
            System.out.println(n + " " + T(n) + " " + f(n));
        }
    }

    public static double T(double n) {
        if (n == 1) {
            return 20;
        } else {
            return 7 * T(n / 4) + Math.pow(n, 2);
        }
    }

    public static double f(double n) {
        return 20 * Math.pow(n, Math.log(7) / Math.log(4)) + (Math.pow(n, 2) * Math.pow(7 / 4, Math.log(n) / Math.log(4)) - Math.pow(n, 2)) / (3.0 / 4);
    }
}
