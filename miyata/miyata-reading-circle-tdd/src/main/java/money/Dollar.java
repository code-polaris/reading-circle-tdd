package money;

public class Dollar {

    int amount;
    Dollar(int amount) {
        this.amount = amount;
    }
    Dollar times(int multiplier) {
        return new Dollar(amount * multiplier);
    }

    public boolean equals(Object object) {
        if (object instanceof Dollar dollar) {
            return amount == dollar.amount;
        }
        return false;
    }
}
