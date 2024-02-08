package org.codepolaris.tdd.chapter2;

import java.util.ArrayList;
import java.util.List;

public class TestSuite {

  List<TestCase> testCases = new ArrayList<>();

  public void add(TestCase test) {
    testCases.add(test);
  }

  public void run(TestResult result) {
    testCases.forEach(test -> test.run(result));
  }
}
