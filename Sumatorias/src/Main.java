public class Main {
    public static long f_sum(int n) {
        long suma = 0;
        for (int i = -40; i <= 2 * n ; i++) {
            for (int j = 40; j <= n*n ; j++) {
                suma += (2 * i * j) + (8 * j);
            }
        }
        return suma;
    }
    public static double sol_sum(int n) {
        double x = ((n * n * (n * n + 1)) / 2) - (39 * 20);
        double parte1 = (-40 * 41) + (2 * n * (2 * n + 1));
        double parte2 = 8 * (2 * n + 41);
        return x * (parte1 + parte2);
    }
    public static void main(String[] args) {
        ;
        for (int valor: new int[]{10, 20, 40, 60, 80, 100}) {
            System.out.printf("%d %d %.0f\n", valor, f_sum(valor), sol_sum(valor));
        }
    }
}