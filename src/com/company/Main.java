package com.company;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Main
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String n1 = Integer.toString(n);
        for(int i = 1; i <= 10; i++)
        {
            System.out.println(n1 + " X " + Integer.toString(i) + " = " + Integer.toString(n*i));
        }
    }
}