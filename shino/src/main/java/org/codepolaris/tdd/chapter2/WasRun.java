package org.codepolaris.tdd.chapter2;

public class WasRun extends TestCase {

  private boolean hasRun;

  public WasRun(String testName) {
    super(testName);
    hasRun = false;
  }

  public void testMethod() {
    hasRun = true;
  }

  public boolean getHasRun() {
    return hasRun;
  }
}
