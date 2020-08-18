public class Magic8{
    public static void main(String[] args){
    int ranNum = (int)Math.round(Math.random()*10);
    switch(ranNum){
      case 0:
          System.out.println("It's not certain.");
          break;
      case 1:
          System.out.println("Maybe so.");
          break;
      case 2:
          System.out.println("Yes.");
          break;
      case 3:
          System.out.println("No.");
          break;
      case 4:
          System.out.println("I do not see it.");
          break;
      case 5:
          System.out.println("Do not count on it.");
          break;
      case 6:
          System.out.println("Not for certain.");
          break;
      case 7:
          System.out.println("It may not be so.");
          break;
      case 8:
          System.out.println("The future is foggy");
          break;
      case 9:
          System.out.println("Not yet.");
          break;
      default:
        System.out.println("Come back later.");
    }
    }
  }