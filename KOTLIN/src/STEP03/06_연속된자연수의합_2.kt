package STEP03

import java.util.*

// https://cote.inflearn.com/contest/10/problem/03-05
// 연속된 자연수의 합으로 입력값 n이 되는 경우를 출력 - 수학적으로 풀기
/*
in
15

out
3
*/

private fun solution(n: Int): Int {
    var n = n
    var answer = 0
    var cnt = 1
    n--
    while (n > 0) {
        cnt++
        n = n - cnt
        if (n % cnt == 0) answer++
    }
    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()
    print(solution(n))
}