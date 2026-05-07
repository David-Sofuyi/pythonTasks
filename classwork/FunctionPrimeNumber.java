public class FunctionPrimeNumber{
    public static boolean isPrime(int number){
        if (number ==1){
            return false;
        }
    int num = number/2;
    int count = 0;
    for (count = 2; count <= num; count++){
       return false; 
    }
    
    return true;    
        }
        
    public static void main(String [] args){        
        System.out.println(FunctionPrimeNumber(21));
        
      }  
    }
