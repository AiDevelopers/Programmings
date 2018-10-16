package com.company;

public class outerclass {

    int inner = 6;
    static int staticvar = 50;

    static class f1{
        public void Static(){
            System.out.print("Static Class " + staticvar);
        }
    }
    class f2{
        public void inner(){
            System.out.print(" inner class " + inner);
        }
    }


}
