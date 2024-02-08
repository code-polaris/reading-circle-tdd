package org.codepolaris.tdd.chapter2;

public class TestResult {

  private int runCount;
  private int errorCount;

  public TestResult() {
    this.runCount = 0;
    this.errorCount = 0;
  }

  public void testStarted() {
    this.runCount++;
  }

  public void testFailed() {
    this.errorCount++;
  }

  public String summary() {
    return String.format("%d run, %d failed", this.runCount, this.errorCount);
  }
}
