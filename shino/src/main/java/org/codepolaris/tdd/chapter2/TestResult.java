package org.codepolaris.tdd.chapter2;

public class TestResult {

  int runCount;

  public TestResult() {
    this.runCount = 0;
  }

  public void testStarted() {
    this.runCount++;
  }

  public String summary() {
    return String.format("%d run, 0 failed", this.runCount);
  }
}
