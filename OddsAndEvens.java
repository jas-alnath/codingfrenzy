//created by Jas on 2019/06/07

import java.util.*;
public class OddsAndEvens {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        //Introduction to game, initializing player choice:

        System.out.println("Let's play a game called \"Odds and Evens\"");
        System.out.print("What is your name? ");
        String playerName = input.next();
        System.out.print("Hi " + playerName + ", which do you choose? (O)dds or (E)vens? ");
        String choice = input.next();


        if (choice.equals("O")) {
            System.out.println(playerName + " has picked odds! Computer will be evens.");
        } else {
            System.out.println(playerName + " has picked evens! Computer will be odds.");
        }
        System.out.println("----------------------------");

        //Gameplay:

        System.out.print("How many \"fingers\" do you put out? ");
        int playerFingers = input.nextInt();
        Random rand = new Random();
        int computerFingers = rand.nextInt(6);
        System.out.println("The computer plays " + computerFingers + " \"fingers\"");
        System.out.println("----------------------------");

        // Determining the winner:

        int fingersSum = playerFingers + computerFingers;
        System.out.println(playerFingers + " + " + computerFingers + " = " + fingersSum);
        boolean oddOrEven = fingersSum % 2 == 0;
        if (oddOrEven && choice.equals("E")) {
            System.out.println(fingersSum + " is... even!");
            System.out.println("That means " + playerName + " wins! :)");
        } else {
            System.out.println(fingersSum + " is... odd!");
            System.out.println("That means the computer wins!");
        }









    }
}
