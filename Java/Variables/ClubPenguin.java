import java.util.Scanner;

public class ClubPenguin {
    public static void main(String[] args) {
        double valueUSDcoins = 0.0045; // Valor de 1 moeda em dólares
        Scanner scanner = new Scanner(System.in); // Scanner para entrada do usuário
        System.out.print("Quantas moedas você deseja converter? "); // Solicita ao usuário o número de moedas
        double coins = scanner.nextDouble(); // Lê o número de moedas inserido pelo usuário
        double convertedValue = valueUSDcoins * coins; // Converte moedas para dólares
        System.out.println(coins + " moedas equivalem a " + convertedValue + " dólares."); // Exibe o resultado da conversão
        scanner.close(); // Fecha o scanner
    }
}