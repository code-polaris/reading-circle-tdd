package money;

public class Fran {
    private int amount;
    Fran(int amount) {
        this.amount = amount;
    }
    Fran times(int multiplier) {
        return new Fran(amount * multiplier);
    }

    public boolean equals(Object object) {
        if (object instanceof Fran fran) {
            return amount == fran.amount;
        }
        return false;
    }
}
