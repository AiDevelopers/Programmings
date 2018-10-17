package com.company.multipleInterface;


class multipleCatch
{
        public static void main(String... ar)
        {
            try
            {
                int arr[]= {1,2,3,4};
                System.out.println("Value ="+arr[5]);   //ArrayIndexOutOfBoundsException thrown, invalid index 5.
            }
            catch(ArrayStoreException exp)     //catch block to handle/catch ArrayStoreException
            {
                System.out.println(exp);
            }
            catch(ArrayIndexOutOfBoundsException exp)   //catch block to handle/catch ArrayIndexOutOfBoundsException
            {
                System.out.println("Exception Caught - "+ exp);
            }
            catch(Exception exp)   //catch block to handle/catch Exception
            {
                System.out.println(exp);
            }

        }
}


