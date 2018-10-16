package com.company;

class TwoDArray{
public static void main(String args[]){
int ar[][]=new int[4][5];
int i,j,k=0;
for(i=0;i<4;i++){
for(j=0;j<5;j++){
ar[i][j]=k;
k++;
}
}

for(i=0;i<4;i++){
for(j=0;j<5;j++){
System.out.print(ar[i][j] + " ");
}
System.out.println();
}
}
}