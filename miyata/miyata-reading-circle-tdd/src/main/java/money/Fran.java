package money;

public class Fran extends Money {
    Fran(int amount) {
        this.amount = amount;
    }
    Fran times(int multiplier) {
        return new Fran(amount * multiplier);
    }

}
