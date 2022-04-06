package INFLEARN.STEP99_TEST

/*
* 문자 'a'와 'b'로 구성된 문자열 S가 주어집니다. 비어 있지 않은 세 부분으로 나누려고 합니다. 부품의 길이는 서로 다를 수 있습니다.
S를 세 부분으로 나눠서 각 부분이 같은 숫자의 'a'를 포함하도록 할 수 있는 방법은?
함수 쓰기:
클래스 솔루션 {public int 솔루션(String S); }
길이가 N인 문자열 S가 주어지면 위에서 설명한 것처럼 S를 분할하는 가능한 방법의 수를 반환합니다.
*
예:
1. S = "babaa"가 주어지면 함수는 2를 반환해야 합니다. 가능한 분할은  "ba | ba | a" and "bab | a | a". 이다.
2. S = "ababa"가 주어지면 함수는 4를 반환해야 한다. 가능한 분할은 다음과 같다: "a | ba | ba", "a | bab | a", "ab | a | ba" and "ab | ab | a".
3. S = "aba"가 주어지면 함수는 0을 반환해야 한다. S를 필요에 따라 분할하는 것은 불가능합니다.
4. S = "bbbbb"가 주어지면 함수는 6을 반환해야 합니다. 가능한 분할은 다음과 같다: "b | b | bbb", "b | bb | bb", "b | bbb | b", "bb | b | bb", "bb | bb | b" and "bbb | b | b". 각 부분에는 동일한 수의 문자 'a' 즉, 0이 포함되어 있습니다.
*
다음 가정을 위한 효율적인 알고리즘을 작성하십시오.
N은 [1..] 범위 내의 정수입니다.40,000];
문자열 S에는 문자 'a'와 'b'만 포함됩니다.
* */
fun main () {
    println(solution(""))
}

private fun solution(S: String): Int {
    // write your code in Kotlin 1.3.11 (Linux)

    return 0
}
