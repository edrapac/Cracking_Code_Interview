//There are three types of edits that can be performed on strings: insert a character,
//remove a character, or replace a character. Given two strings, write a function to check if they are
//one edit (or zero edits) away
//pale, ple -> true
//pales, pale -> true
//pale, bale -> true
//pale, bae -> false
package com.company;

import static com.sun.javafx.fxml.expression.Expression.not;

public class Main {

    public static void main(String[] args){

        oneAway("Green","Greens");
    }

    public static void oneAway(String startString, String endString){
        int lenCounter = (startString.length() - endString.length());

        if((lenCounter == 1 || lenCounter == -1 || lenCounter ==0))
        {
            switch (lenCounter){
                case(1):{ // if the result is 1 meaning we deleted a character
                    int originalLength = 0;
                    for (int i =0 ; i<endString.length(); i++){
                        if (startString.contains(String.valueOf(endString.charAt(i)))){
                            originalLength++;
                        }
                    }
                    if(originalLength == endString.length()){
                        System.out.println("This is a valid change, one character removed");
                    }
                }
                case(-1):{
                    int originalLength = 0;
                    for (int i =0; i< startString.length(); i++){
                        if(endString.contains(String.valueOf(startString.charAt(i)))){
                            originalLength++;
                        }
                    }
                    if (originalLength == startString.length()){
                        System.out.println("This is a valid change, one character added");
                    }

                }
                case(0):{
                    int lengthCoutner = 0;
                    for (int i =0; i<startString.length(); i++){
                        
                    }
                }
            }

        }

        else {
            System.out.println("The given strings have had too many edits performed");
        }
    }
}