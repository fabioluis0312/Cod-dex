public class ErrorLogs {
    public static void main(String[] args) {

        System.err.println("Connecting to server…"); //O programa tenta estabelecer uma conexão com um servidor.
        System.err.println("Error: Connection timed out."); //A tentativa de se conectar ao servidor falhou porque a conexão demorou muito.
        System.err.println("Retrying…");  //O programa vai reiniciar.

        // System.err.println() is used to print error messages! 😵😵❌
        // It is similar to System.out.println() but is used to print error messages.

    }
}
