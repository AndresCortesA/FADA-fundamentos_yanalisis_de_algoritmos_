/*
    Andres Arias
    Complejidad iterativa
    FADA
 */

public class Main {

    public static long sumatoria1(long n, long u){
        long suma = 0;
        for(long i=0; i<=n; i++){
            suma = i*u;
        }
        return suma;
    }



    public static long algoritmo1(long n){
        long i = 0;
        long res = 0;


        while (i < n) {
            long j=0;
            long u = 1;
            long p ;
            System.out.println("por fuera");

            while (j <= n) {
                j +=1;
                p = (j*j+ j +1);
                u += 2*j;

                System.out.println(j + " por dentro: " + u + " transformacion: " + p);
            }
            i++;
            res += u;


            System.out.println("resultado por fuera: " + res +" valor por fuera: "+ sumatoria1(i, u)+"\n");
        }


        return res;
    }

    public static void main(String[] args) {
        long alg = algoritmo1(5);
        System.out.println(alg);
    }
}