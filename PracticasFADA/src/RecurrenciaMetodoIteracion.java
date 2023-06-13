public class RecurrenciaMetodoIteracion {
    public static double T(double n, int C) {
        if (n == 1) {
            return C;
        } else {
            return 3 * T(n / 4, C) + n;
        }
    }

    public static long f(int n, int C) {
        C = (int) (Math.pow(n, Math.log(3) / Math.log(4)) - 4 * (n * Math.pow(n, Math.log(3 / 4) / Math.log(4)) - n));
        return C;
    }

    public static void main(String[] args) {
        int[] cte = {1, 2, 3, 4, 5};
        int[] lst = new int[5];
        for (int i = 0; i < 5; i++) {
            lst[i] = (int) Math.pow(4, i);
        }

        for (int C : cte) {
            for (int n : lst) {
                System.out.println("cte=" + C + " n=" + n + " val:" + T(n, C) + " " + f(n, C));
            }
        }
    }
}
