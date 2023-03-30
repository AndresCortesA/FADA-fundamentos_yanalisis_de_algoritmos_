public class Main {

    //sin optimizar
    public static double problema1(long n){
        long contador = 0;

        contador++;
        long s = 0;
        contador++;


        for(long i = 2*n; i >= 0; i--){
            contador++;
            for(long j = i; j >= 0; j--){
                contador++;
                s++;
                contador++;
            }
            contador++;
        }
        contador++;
        return contador;
    }
    /*
    * valor optimo (2n+1)(n+1)
    * 2n^2+3n+1
    * */
    public static double problema1_1(long n){
        return (2*(n*n) + 3*n + 1);
    }

    //sin optimizar
    public static double problema2(long n){
        int t = 0;
        for(long i = 0; i <= n*n; i+=2){
            for (long j=1; j <= i; j++){
                t ++;
            }
        }

        return t;
    }

    /*
    valor optimo (n^4+2n^2)/4
    * */
    public static double problema2_1(long n){
        double valor1 = Math.pow(n,4);
        double valor2 = Math.pow(n,2);
        return (valor1+(2*valor2))/4;
    }
    public static void main(String[] args) {
        long[] arr1 = {0,2, 4,6,8,10,20,40};
        for(long valor:arr1) {
            System.out.println(valor + " " + problema1(valor) + " " + problema1_1(valor));
        }
        System.out.println("*************************************** problemas ****************************");
        for(long valor:arr1){
            System.out.println(valor+" "+problema2(valor) + " " + problema2_1(valor));
        }
    }
}