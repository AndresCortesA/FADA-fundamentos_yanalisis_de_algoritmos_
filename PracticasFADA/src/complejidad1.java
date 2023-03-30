public class complejidad1 {

    public static double problema(long n){
        long contador = 0;

        contador++;
        long s = 0;

        contador++;
        for (long i=n; i>=0; i--){
            contador++;

            for (long j = i; j >= 0; j--){
                contador++;
                s++;
                contador++;
            }
            contador++;
        }
        contador++;
        return contador;
    }

    public static double problema2(long n){
        return Math.pow(n,2) + 5*(n)+7;
    }
    public static void main(String[] args) {
        long[] arr = {1,2,3,4,5,6,7,8};
        for (long valor : arr){
            System.out.println(valor+" " + problema(valor) + " "  + problema2(valor));
        }
    }
}
