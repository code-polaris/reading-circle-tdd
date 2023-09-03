package money;

public class Dollar extends Money {

    Dollar(int amount) {
        this.amount = amount;
    }
    Money times(int multiplier) {
        return new Dollar(amount * multiplier);
    }

    @Override
    String currency() {
        return "USD";
    }

}
