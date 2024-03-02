class Result {

    /*
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     Given an array of integers, calculate the ratios of its 
     elements that are positive, negative, and zero. 
     Print the decimal value of each fraction on a new line with
     places after the decimal.

    Note: This challenge introduces precision problems. 
    The test cases are scaled to six decimal places, though 
    answers with absolute error of up to
    are acceptable.

    
    ## EXAMPEL ##
    arr = [1, 1, 0, -1, -1]
    arrLength = 5
    postive integers = 2 / arrLength -> 0.400000
    negative integers = 2 / arrLength -> 0.400000
    zeros = 1 / arrLength -> 0.200000
     */

    public static void plusMinus(List<Integer> arr) {
    // Write your code here
    int negTotal = 0;
    int postTotal = 0;
    int zeroTotal = 0;
    int arrLength = arr.size();
    for(int i = 0; i < arr.size(); i++) {
        if (arr.get(i) < 0 ) {
            negTotal += 1;
        } else if (arr.get(i) > 0 ) {
            postTotal += 1;     
        } else {
            zeroTotal += 1;
        }
    }
    
    float negRatio = (float) negTotal / arrLength;
    float postRatio = (float) postTotal / arrLength;
    float zeroRatio = (float) zeroTotal / arrLength;
    
    System.out.println(postRatio);
    System.out.println(negRatio);
    System.out.println(zeroRatio);
    
    

    }

}
