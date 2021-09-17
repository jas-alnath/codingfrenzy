import java.util.Scanner;

public class LongestName {
    public static void main(String[] args) {
        Longest();
    }


    private static void Longest(Scanner console, int num) {
        Scanner console = new Scanner(System.in);
        String longest = ("");
        boolean isTie = false;

        for (int i = 1; i <= num; i++) {
            System.out.print("Name # " + i + "? ");
            String name = console.next();
            if (name.length() == longest.length()) {
                isTie = true;
            } else if (name.length() > longest.length()) {
                isTie = false;
                longest = name;
            }


        }
        String capitalizedName = longest.substring(0, 1).toUpperCase() + longest.substring(1).toLowerCase();
        System.out.println(capitalizedName + "'s name is longest");
        if(isTie)
            System.out.println("(There was a tie!)");

    }
}
