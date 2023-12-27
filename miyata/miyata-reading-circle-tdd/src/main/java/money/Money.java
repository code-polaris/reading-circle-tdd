package money;

public abstract class Money {

    protected int amount;
    protected String currency;

    Money(int amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }

    abstract Money times(int multiplier);
    public String currency() {
        return currency;
    };

    public boolean equals(Object object) {
        if (object instanceof Money money) {
            return amount == money.amount
                    && getClass().equals(money.getClass());
        }
        return false;
    }
    static Money dollar(int amount) {
        return new Dollar(amount, "USD");
    }
    static Money franc(int amount) {
        return new Franc(amount, "CHF");
    }
}
