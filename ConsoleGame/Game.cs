using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    public new static void UpdatePosition(string key, out int x, out int y){
      switch(key){
        case "DownArrow":
          y = +1;
          x = 0;
          break;
        case "UpArrow":
          y = -1;
          x = 0;
          break;
        case "LeftArrow":
          x = -1;
          y = 0;
          break;
        case "RightArrow":
          x = +1;
          y = 0;
          break;
        default:
          x = 0;
          y = 0;
          break;
      }
    }

    public new static char UpdateCursor(string keyPressed){
      switch (keyPressed){
        case "DownArrow":
          return 'v';
        case "UpArrow":
          return '^';
        case "LeftArrow":
          return '<';
        case "RightArrow":
          return '>';
        default:
          return '^';
      }
    }

    public new static int KeepInBounds(int coord, int maxVal){
      if(coord < 0){
        return 0;
      } else if (coord >= maxVal){
        return maxVal -1;
      } else {
        return coord;
      }
    }

    public new static bool DidScore(int x, int y, int fruitx, int fruity){
      if(x == fruitx && y == fruity){
        return true;
      } else {
        return false;
      }
    }

  }

}