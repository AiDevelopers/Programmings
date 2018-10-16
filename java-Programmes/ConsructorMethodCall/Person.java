package com.company;

public class Person {
    private String Fname;
    private String Sname;
    private String Tname;
    private String addr1;
    private String addr2;
    private String addr3;


    public Person(String fn,String fa,String sn,String sa,String tn,String ta){
        Fname = fn;
        addr1 = fa;
        Sname = sn;
        addr2 = sa;
        Tname = tn;
        addr3 = ta;
    }

    public void displaydetails(){
        System.out.println("first name " + Fname + " address " + addr1);
        System.out.println("Sconed name " + Sname + " address " + addr2);
        System.out.print("third name " + Tname +  " address " + addr3);

    }
}
