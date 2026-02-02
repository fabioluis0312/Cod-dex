import java.util.Scanner;

public class EscapeRoom {
    public static void main(String[] args) {
        

        System.out.println("Eu falo sem boca e ouço sem ouvidos. Não tenho corpo, mas ganho vida com o vento. O que sou eu?");
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite a resposta: ");
        String name = scanner.nextLine();
        scanner.close();

        System.out.println("Parabens");
    }
}
