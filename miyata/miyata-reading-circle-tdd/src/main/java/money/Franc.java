package money;

public class Franc extends Money {

    Franc(int amount) {
        this.amount = amount;
        this.currency = "CHF";
    }
    Money times(int multiplier) {
        return new Franc(amount * multiplier);
    }

}
