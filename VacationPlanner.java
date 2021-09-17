// created by Jas on 2019/06/01 :)

// Input asked: user's name, travel destination, duration, budget, exchange rate of destination.
// Output: length of travel converted to hours + minutes, budget converted to
// destination's currency, budget that can be spent per day in local currency and converted
// to destination's currency, difference in timezone, size of destination country converted
// from square kilometres to square miles.
import java.util.Scanner;

public class VacationPlanner {
    public static void main(String[] args) {
        intro();
        TravelBudget();
        TimeDifference();
        CountryArea();

        }

        //Introduction
        public static void intro() {
            Scanner input = new Scanner(System.in);
            System.out.println("Welcome to vacation planner!");
            System.out.print("What is your name? ");
            String name = input.nextLine();
            System.out.print("Nice to meet you " + name + "," + " " + "where are you travelling to? ");
            String travelDestination = input.nextLine();
            System.out.println("Great! " + travelDestination + " " + "sounds like a great trip.");
            System.out.println("**************");
            System.out.println();
        }

        //Calculation of traveller's budget
        public static void TravelBudget() {
            Scanner input = new Scanner(System.in);
            System.out.print("How many days are you going to spend travelling? ");
            int TripLength = input.nextInt();
            System.out.print("How much money, in USD, are you planning to spend on your trip? ");
            double TripBudget = input.nextDouble();
            System.out.print("What is the three letter currency symbol for your travel destination? ");
            String CurrencySymbol = input.next();
            System.out.print("How many " + CurrencySymbol + " " + "are there in 1 USD? ");
            double CurrencyConversion = input.nextDouble();
            double ConvertedCurrency = TripBudget * CurrencyConversion;
            System.out.println();
            System.out.println();
            int RoundedBudgetPerDay = (int) ((TripBudget / TripLength * 100) / 100.0);
            int RoundedBudgetConverted = (int) ((ConvertedCurrency / TripLength * 100) / 100.0);

            System.out.println("If you are travelling for " + TripLength + " days that is the same as " + TripLength * 24 + " hours or " + TripLength * 24 * 60 + " minutes");
            System.out.println("If you are going to spend $" + TripBudget + " USD " + "that means per day you can spend up to " + RoundedBudgetPerDay + " USD");
            System.out.println("Your total budget in " + CurrencySymbol + " is " + ConvertedCurrency + ", which per day is " + RoundedBudgetConverted + " " + CurrencySymbol);
            System.out.println("**************");
            System.out.println();

        }

        //Calculation of time difference between home and destination timezone
        public static void TimeDifference() {
            Scanner input = new Scanner(System.in);
            System.out.println("What is the time difference, in hours, between your home and your destination?");
            int TimeDifference = input.nextInt();
            int NoonConversion = ((24 + TimeDifference) % 24);
            int MidnightConversion = ((12 + TimeDifference) % 12);
            System.out.println("That means that when it is midnight at home it will be " + MidnightConversion + ":00 in your travel destination");
            System.out.println("and when it is noon at home it will be " + NoonConversion + ":00");
            System.out.println("**************");
            System.out.println();
        }

        public static void CountryArea() {
            Scanner input = new Scanner(System.in);
            System.out.print("What is the square area of your destination country in km2? ");
            double SquareArea = input.nextInt();
            double AreaConversion = (int) (((SquareArea / 2.59)) * 100 / 100);
            System.out.println("In miles2 that is " + AreaConversion);
            System.out.println("**************");


        }



    }


