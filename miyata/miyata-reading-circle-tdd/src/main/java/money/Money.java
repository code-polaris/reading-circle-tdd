package money;

public abstract class Money {
    protected int amount;
    abstract Money times(int multiplier);
    abstract String currency();

    public boolean equals(Object object) {
        if (object instanceof Money money) {
            return amount == money.amount
                    && getClass().equals(money.getClass());
        }
        return false;
    }
    static Money dollar(int amount) {
        return new Dollar(amount);
    }
    static Money franc(int amount) {
        return new Franc(amount);
    }
}
