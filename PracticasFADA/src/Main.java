public class Main {

    public static double problema(long n){
        long i = 1;
        long contador = 1;
        while (i <= n) {
            contador +=1; //entrada
            long k = i;
            contador +=1; //k = i
            while (k <= n) {
                contador +=1; //entrada
                k += 2;
                contador +=1; // k +=2
            }
            contador +=1; //salida
            k=1;
            contador +=1; // k= 1
            while (k <= i) {
                contador +=1; // entrada
                k = k + 1;
                contador +=1; // k = k +1
            }
            contador +=1; //salida
            i +=2;
            contador +=1; // i += 2
        }
        contador +=1; //Salida
        return contador;
    }
    public static void main(String[] args) {
        long[] lista = {21,33,41,91,101,201};
        for(long valor:lista){
            System.out.println(problema(valor));
        }
    }
}