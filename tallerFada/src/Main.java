public class Main {

    //sin optimizar
    public static double problema1(long n){
        long contador = 0;
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
    public static double  problema1_1(long n){
        long linea1 = 1;
        long linea2 = 2*n+2;
        long linea3 = 2*n*(2*n+1)/2 + 4*n + 2;
        long linea4 = 2*n*(2*n+1)/2 + 2*n + 1;
        return linea1+linea2+linea3+linea4;
    }

    //sin optimizar
    public static double problema2(long n){
        long cnt = 0;
        int t = 0;

        cnt++;
        for(long i = 0; i <= n*n; i+=2){
            cnt++;
            for (long j=1; j <= i; j++){
                cnt++;
                t ++;
                cnt++;
            }
            cnt++;
        }
        cnt++;
        return cnt;
    }

    /*
    valor optimo (n^4+2n^2)/4
    * */
    public static double problema2_1(long n){
        long linea1 = 1;
        long linea2 = n*n/2+2;
        long linea3 = (n*n/2+1)*(n*n/2+1);
        long linea4 = (n*n/2+1)*(n*n/2+1)-(n*n/2+1);
        return linea1+linea2+linea3+linea4;
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