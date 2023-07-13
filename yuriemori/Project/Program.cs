// Dollarクラス

namespace Project
{    

    public class Dollar
    {
        
        // Timesメソッドをコールする静的Mainメソッドを追加
        public static void Main(string[] args)
        {
            var dollar = new Dollar(5);
            dollar.Times(2);            
        }

        public int Amount { get; private set; }

        public Dollar(int amount)
        {
            Amount = amount;
        }

        public void Times(int multiplier)
        {
            Amount *= multiplier;
        }        
    }
}