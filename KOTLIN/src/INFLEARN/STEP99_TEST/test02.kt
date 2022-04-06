package INFLEARN.STEP99_TEST

/*
우리는 알파벳을 "a", "b", "c"의 세 글자로 간주한다. 연속된 세 글자가 같지 않으면 문자열은 다양하다고 불립니다. 다시 말해, 다양한 문자열은 "aa", "bbb", "ccc" 중 어떤 문자열도 포함할 수 없다.

함수 쓰기:

솔루션(A: Int, B: Int, C: Int): 문자열

이것은 3개의 정수 A, B, C가 주어졌을 때 최대 A 문자 'a', 최대 B 문자 'b', 최대 C 문자 'c'를 포함하는 가능한 가장 긴 다양한 문자열을 반환한다. 문자열을 작성할 수 없는 경우 빈 문자열을 반환합니다.

예:

1. A = 6, B = 1, C = 1이 주어지면 함수는 "aabaaca"를 반환할 수 있습니다. "aacaabaa" 또한 정답일 수 있습니다. 이 함수는 정답을 반환할 수 있습니다.

2. A = 1, B = 3 및 C = 1이 주어지면 함수는 "abbcb", "bcb", "bcbb" 또는 다른 여러 문자열을 반환할 수 있습니다.

3. A = 0, B = 1, C = 8이 주어지면 함수는 이 경우 유일한 정답인 "ccbcc"를 반환해야 합니다.

다음과 같이 가정한다.

A, B, C는 [0] 범위 내의 정수입니다.100];
A + B + C > 0.
해결책에서는 정확성에 초점을 맞추십시오. 솔루션의 성과는 평가의 초점이 아닙니다.
* */
fun main(){

    val t1 = "?ab??a"
    val t2 = "bab??a"
    val t3 = "?a?"

    println(solution(6,1,1))
    println(solution(1,3,1))
    println(solution(0,1,8))
}

private fun solution(A: Int, B: Int, C: Int): String {
    var answer = ""
    val len = A+B+C
    var cntA = Pair("A", A)
    var cntB = Pair("B", B)
    var cntC = Pair("C", C)

    // 문자열에서 일단 cntA B C 가 0보다 크면 하나씩 감소 하고, for 안에 while > 3 까지 answer 더한다.
    //
    for(i in 0 until len) {
        // val cur = answer[i]
        if(cntA.component2() > 0) {
           answer += cntA.component1()
        }
    }

    return answer.toString()
}