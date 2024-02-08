package org.codepolaris.tdd.chapter2;

import lombok.Getter;

@Getter
public class WasRun extends TestCase {

  // name "log" is already used in TestCase. So storedLog will be used here instead of "log" in the book
  private final StringBuilder storedLog;

  public WasRun(String testName) {
    super(testName);
    storedLog = new StringBuilder();
  }

  @Override
  public void setUp() {
    super.setUp();
    storedLog.append("setUp ");
  }

  @Override
  public void tearDown() {
    super.tearDown();
    storedLog.append("tearDown ");
  }

  public void testMethod() {
    storedLog.append("testMethod ");
  }

  public void testBrokenMethod() {
    throw new RuntimeException("failed");
  }

  public String getStoredLog() {
    // return string instead of StringBuilder
    return storedLog.toString();
  }
}
