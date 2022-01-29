//This is an example of unit testing in JS
describe('My Test Suite', () => {
    //each of these "it" blocks are individual test cases
  it('should add numbers', () => {
    const sum = adder(2, 3);
    //"expect" in JS is equivalent to "assert" in Python
    expect(sum).toBe(5);
  });

  //we expect this test to fail
  it('should add negative numbers', () => {
    expect(adder(1, -1)).toBe(99);
  });
});

//Even though we have written these unit tests in a certain order, Jasmine runs
//them in a randomized order.