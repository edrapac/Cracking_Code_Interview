package com.company;

import java.util.Scanner;

// is with a URL, any string that contains a white space should have that whitespace replaced by a %20
public class Main {

    public static void main(String [] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please type in some string: ");
        String output = scanner.nextLine();
        URLify(output);
    }

    public static void URLify( String inputstring){
        StringBuilder stringBuild = new StringBuilder();
        for ( int i = 0; i<inputstring.length(); i++){
            if (String.valueOf(inputstring.charAt(i)).equalsIgnoreCase(" ")){
                stringBuild.append("%20");
            }
            else{
                stringBuild.append(inputstring.charAt(i));

            }

        }

        System.out.println(stringBuild);
    }
}