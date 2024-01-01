package org.codepolaris.tdd.chapter2;

import lombok.Getter;
import lombok.extern.slf4j.Slf4j;

import java.lang.reflect.Method;

@Slf4j
@Getter
public class TestCase {

  protected String testName;
  protected boolean setUp;

  public TestCase(String testName) {
    this.testName = testName;
    this.setUp = false;
  }

  public void setUp() {
    // empty method
  }

  public void tearDown() {
    // empty method
  }

  public void run() {
    try {
      setUp();
      // this is java way to call method from the test name
      Method method = this.getClass().getDeclaredMethod(this.testName);
      method.invoke(this);
    } catch (NoSuchMethodException ex) {
      log.error("The provided method name " + this.testName + "not found");
    } catch (Exception ex) {
      log.error("Error during the method call of " + this.testName + ". The actual error is:" + ex.getMessage());
    }
    tearDown();
  }
}
