package com.company;

import java.util.ArrayList;
import java.util.List;

//Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
//cannot use additional data structures?
public class Main {

    public static void main(String[] args) {

        isUnique("Teseract");
        isUnique("Hey");
    }

    public static void isUnique(String stringname){
        ArrayList <String> isUnique = new ArrayList<>();
        if (stringname.length() > 128){
            System.out.println("This is a non-unique string as it contains more than 128 chars ");
        }
        for (int i =0; i<stringname.length(); i++)
        {
            if (isUnique.contains(String.valueOf(stringname.charAt(i))) ){
                System.out.println("This is a non-unique string");
            }
            else {

                isUnique.add(String.valueOf(stringname.charAt(i)));
            }
        }

    }
}

// .get is the access method for accessing array indicies